"""Flask application init"""
import os
from pickle import load

from flask import Flask
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError
from flask_restful import Api
from flask_cors import CORS


def populate_db(filename="/var/www/data/wimbledon.pickle"):
    """populate the db"""
    if os.path.isfile(filename):
        with open(filename, "rb") as picklefile:
            items = load(picklefile)
        for _id, item in enumerate(items):
            try:
                db.matches.insert_one(dict(item, **{"_id": _id}))
            except DuplicateKeyError:
                pass
        print(f"Items: {db.matches.estimated_document_count()}")
        try:
            os.unlink(filename)
        except FileNotFoundError:
            pass


# instantiate the app
application = Flask(__name__)
application.config.from_object("configuration.TestingConfig")
mongo = PyMongo(application)
db = mongo.db
# populate the db
populate_db()
api = Api(application)

# enable CORS, very permissive
CORS(application, resources={r"/*": {"origins": "*"}})

from apis import Match, Matches, Winner  # pylint: disable=wrong-import-position

api.add_resource(Match, "/api/match")
api.add_resource(Winner, "/api/winner")
api.add_resource(Matches, "/api/matches")
