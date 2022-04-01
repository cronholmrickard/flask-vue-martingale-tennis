"""WSGI entrypoint"""

import sys
import os
import argparse
from martingale_backend import version
from martingale_backend.app import create_app


def get_args(args: list) -> argparse.Namespace:
    """Parse arguments passed in from shell."""
    return get_parser().parse_args(args)


def get_parser() -> argparse.ArgumentParser:
    """Return ArgumentParser for martingale backend."""
    _defaults = {
        "host": "0.0.0.0",
        "port": int(os.getenv("APP_PORT", default="5000")),
        "config": "Production",
    }
    parser = argparse.ArgumentParser(allow_abbrev=True, description="martingale_backend")
    parser.add_argument(
        "--host",
        dest="host",
        default=_defaults["host"],
        help=f"""The IP of the application host. [{_defaults["host"]}]""",
    )
    parser.add_argument(
        "--port",
        dest="port",
        default=_defaults["port"],
        help=f"""Port on which to run application on host. [{_defaults["port"]}]""",
    )
    parser.add_argument(
        "--config",
        dest="config",
        default="Production",
        help=f"""Configuration mode of application. [{_defaults["config"]}]""",
    )
    parser.add_argument(
        "--version",
        action="version",
        help="Echo version number.",
        version=f"{version()}",
    )
    return parser


def start(*args):
    """Initiates the application"""
    if not args:
        try:
            args = sys.argv[1:]
        except IndexError:
            args = []

    parsed_args = get_args(args)
    app = create_app(config=parsed_args.config)
    app.run(
        host=parsed_args.host,
        port=parsed_args.port
    )

# call start
start()
