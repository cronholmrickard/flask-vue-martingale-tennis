"""
Flask Application configuration
"""
import os


class Config:  # pylint: disable=too-few-public-methods
    """
    Configuration base, for all environments.
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.urandom(24)
    CSRF_ENABLED = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):  # pylint: disable=too-few-public-methods
    """Production config"""

    ENV = "production"
    DEBUG = False
    MONGO_URI = (
        f"""mongodb://{os.getenv("MONGODB_USERNAME", default="tennis")}:"""
        f"""{os.getenv("MONGODB_PASSWORD", default="tennis")}@"""
        f"""{os.getenv("MONGODB_HOSTNAME", default="mongodb")}:"""
        f"""{os.getenv("MONGODB_PORT", default="27017")}/"""
        f"""{os.getenv("MONGODB_DATABASE", default="tennisdb")}"""
    )


class TestingConfig(Config):  # pylint: disable=too-few-public-methods
    """Testing Config"""

    ENV = "testing"
    TESTING = True
    DEBUG = True
    MONGO_URI = "mongodb://tennis:tennis@172.17.0.1:27017/tennisdb"
