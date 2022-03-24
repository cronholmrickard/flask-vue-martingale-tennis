"""Defines RESTful routes"""

from random import shuffle

from flask import jsonify
from flask_restful import Resource, abort, reqparse

from app import db


class Winner(Resource):
    """Get the winner of a match"""

    def get(self):  # pylint: disable=no-self-use
        """get method"""
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True)
        pargs = parser.parse_args()

        match = db.matches.find_one({"_id": pargs.id})
        if not match:
            abort(404, message=f"No match with id {pargs.id} in database")
        return jsonify(match[match["Winner"]])


class Match(Resource):
    """Defines the match resource"""

    def get(self):  # pylint: disable=no-self-use
        """get method"""
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int, required=True)
        pargs = parser.parse_args()

        match = db.matches.find_one({"_id": pargs.id})
        _ = match.pop("Winner")  # we don't want you sneek peaking at winners
        if not match:
            abort(404, message=f"No match with id {pargs.id} in database")
        return jsonify(match)


class Matches(Resource):
    """Get indices of a number of matches"""

    def get(self):  # pylint: disable=no-self-use
        """get method"""
        parser = reqparse.RequestParser()
        parser.add_argument("number", type=int, required=True)
        pargs = parser.parse_args()
        _n_matches = db.matches.count_documents(filter={})
        if pargs.number > _n_matches:
            abort(
                406,
                message=f"Too many mathces selected. Database contains {_n_matches} matches",
            )
        data = list(db.matches.find())
        shuffle(data)
        return jsonify([x["_id"] for x in data[:pargs.number]])
