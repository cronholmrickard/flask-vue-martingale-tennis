"""
Defining all flask extensions
"""

from flask_pymongo import PyMongo
from flask_restful import Api
from flask_cors import CORS

mongo = PyMongo()
api = Api()
cors = CORS()
