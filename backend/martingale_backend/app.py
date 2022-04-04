"""Flask application init"""

from flask import Flask

from martingale_backend.exts import mongo, api, cors
from martingale_backend.apis import (
    Match,
    Matches,
    Winner,
    Results,
    Tournament,
)
from martingale_backend import DataPopulator


def register_extensions(app) -> None:
    """Register all extensions"""
    mongo.init_app(app)
    api.init_app(app)
    # very permissive cors, but this is handled by restrictive whitelisting in nginx
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})


def register_endpoints() -> None:
    """register api endpoints"""
    api.add_resource(Match, "/api/match")
    api.add_resource(Winner, "/api/winner")
    api.add_resource(Matches, "/api/matches")
    api.add_resource(Results, "/api/results")
    api.add_resource(Tournament, "/api/tournament")


def populate_db() -> None:
    """Initial database population"""
    data_populator = DataPopulator.from_dir("/var/www/data/")
    data_populator.parse()
    data_populator.populate(mongo.db.matches)


def create_app(config: str="Testing") -> Flask:
    """Create the application"""
    app = Flask(__name__)
    app.config.from_object(f"martingale_backend.configuration.{config}Config")
    register_endpoints()
    register_extensions(app)
    populate_db()
    return app
