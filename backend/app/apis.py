"""Defines RESTful routes"""

import os
from random import shuffle
from tempfile import TemporaryDirectory

from flask import jsonify, request, Response
from flask_restful import Resource, abort, reqparse
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequestKeyError

from app import db
from handle_tennis_data import DataPopulator


class MatchData(Resource):
    """Parent class for all Match related Resources"""

    def __init__(self):
        """constructor"""
        self.collection = db.matches
        super().__init__()


class Winner(MatchData):
    """Get the winner of a match"""

    def get(self):
        """get method"""
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=str, required=True)
        pargs = parser.parse_args()

        match = self.collection.find_one({"_id": pargs.id})
        if not match:
            abort(404, message=f"No match with id {pargs.id} in database")
        return jsonify(match[match["Winner"]])


class Match(MatchData):
    """Defines the match resource"""

    def get(self):
        """get method"""
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=str, required=True)
        pargs = parser.parse_args()

        match = self.collection.find_one({"_id": pargs.id})
        _ = match.pop("Winner")  # we don't want you sneek peaking at winners
        if not match:
            abort(404, message=f"No match with id {pargs.id} in database")
        return jsonify(match)


class Matches(MatchData):
    """Get indices of a number of matches"""

    def get(self):
        """get method"""
        parser = reqparse.RequestParser()
        parser.add_argument("number", type=int, required=True)
        pargs = parser.parse_args()
        _n_matches = self.collection.count_documents(filter={})
        if pargs.number > _n_matches:
            abort(
                406,
                message=f"Too many mathces selected. Database contains {_n_matches} matches",
            )
        data = list(self.collection.find())
        shuffle(data)
        return jsonify([x["_id"] for x in data[:pargs.number]])


class Tournament(MatchData):
    """Handle tournamet data"""

    def post(self):
        """post method"""
        try:
            _file = request.files["tournament"]
        except BadRequestKeyError:
            abort(
                400,
                message="No tournament file was supplied in the form."
            )
        if not _file.filename.endswith(".csv"):
            abort(
                415,
                message="Only csv files are accepted."
            )
        filename = secure_filename(_file.filename)
        with TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, filename)
            _file.save(filepath)
            populator = DataPopulator([filepath])
            populator.parse()
            populator.populate(self.collection)
        return Response(f"Tournament data from {filename} added to database\n", status=201)


class Results(Resource):
    """Handle results"""

    def __init__(self):
        """constructor"""
        self.collection = db.results
        super().__init__()

    def post(self):
        """post method"""
        parser = reqparse.RequestParser()
        parser.add_argument("roi", type=float, required=True)
        pargs = parser.parse_args()
        self.collection.insert_one({"roi": pargs.roi})

    def get(self):
        """get method"""
        data = [x["roi"] for x in self.collection.find()]
        _positive = len(list(filter(lambda x : x >= 0, data)))
        return jsonify(
            {
                "negative": len(data) - _positive,
                "positive": _positive
            }
        )

