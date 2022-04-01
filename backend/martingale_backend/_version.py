"""Defines the version of martingale_backend"""

__author__ = "rc"

_MAJOR = 0
_MINOR = 1
_BUILD = "dev0"


if not isinstance(_BUILD, str):
    _BUILD = str(_BUILD)
__version__ = f"{_MAJOR}.{_MINOR}.{_BUILD}"
__version_short__ = f"{_MAJOR}.{_MINOR}"


def get_version(form="full"):
    """
    Get function for version

    Args
        form : str ; defines the version type. Acceptable values are\n
                    full, short, info, product
    Returns
        the version in the specified format
    Raises
        ValueError if not in accepted list
    """

    value = None

    if form == "full":
        value = __version__
    elif form == "short":
        value = __version_short__
    elif form == "build":
        value = _BUILD
    else:
        raise ValueError("Incompatible version format requested")
    return value
