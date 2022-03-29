"""Flask application init"""
import os
from pickle import load

from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_cors import CORS

from handle_tennis_data import DataPopulator

# instantiate the app
application = Flask(__name__)
application.config.from_object("configuration.TestingConfig")
mongo = PyMongo(application)
db = mongo.db
api = Api(application)

# enable CORS, very permissive
CORS(application, resources={r"/api/*": {"origins": "*"}})

# populate db
data_populator = DataPopulator.from_dir("/var/www/data/")
data_populator.parse()
data_populator.populate(db.matches)

from apis import Match, Matches, Winner, Results  # pylint: disable=wrong-import-position

api.add_resource(Match, "/api/match")
api.add_resource(Winner, "/api/winner")
api.add_resource(Matches, "/api/matches")
api.add_resource(Results, "/api/results")
