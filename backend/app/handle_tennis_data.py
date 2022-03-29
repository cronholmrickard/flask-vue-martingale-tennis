"""
Module handling handling tennis data
Data shall be csv files from http://www.tennis-data.co.uk/
Datafiles will be parsed and entered to the db
"""


import os
from glob import glob
from csv import reader
from random import randint
from hashlib import sha256
from json import dumps

from pymongo.errors import DuplicateKeyError


def get_sha(info: dict, winner: str, loser: str) -> str:
    """Computes the sha256 hexdigest from input"""
    return sha256(
        dumps(dict(info, **{"Players": [winner, loser]}), sort_keys=True).encode(
            "utf-8"
        )
    ).hexdigest()


class DataPopulator:
    """A class for database population from csv files"""

    def __init__(self, csv_files):
        self.csv_files = csv_files
        self.data_items = []

    @classmethod
    def from_dir(cls, directory: str, recursive: bool = False):
        """creates instance by finding files in directory"""
        _searchpath = f"{directory}/**/*.csv" if recursive else f"{directory}/*.csv"
        csv_files = glob(_searchpath, recursive=recursive)
        return cls(csv_files)

    def parse(self):
        """Parse csv files to data items"""
        header = []
        rawdata = []
        for item in self.csv_files:
            with open(item, "r", encoding='utf-8') as csvfile:
                datareader = reader(csvfile)
                for row in datareader:
                    if not header:
                        header = row
                    else:
                        rawdata.append(dict(zip(header, row)))
            try:
                os.unlink(item)
            except (FileNotFoundError, PermissionError):
                pass

        # convert to useful structure
        for item in rawdata:
            try:
                _odds = sorted([float(item[x]) for x in ("PSW", "PSL")])
            except (ValueError, TypeError, KeyError):
                continue  # skip to next
            if _odds[0] < 1.15:
                # filter out extreme favourites
                continue
            if item["Comment"] == "Completed":
                # only keep Completed matches
                _winner = {
                    "Name": item["Winner"],
                    "Rank": int(item["WRank"]),
                    "Odds": float(item["PSW"]),
                }
                _loser = {
                    "Name": item["Loser"],
                    "Rank": int(item["LRank"]),
                    "Odds": float(item["PSL"]),
                }
                cointoss = randint(0, 1)
                _data = {
                    "Info": {
                        x: item[x]
                        for x in ("Date", "Tournament", "Round", "Court", "Surface")
                    },
                    "Home": _winner if cointoss == 0 else _loser,
                    "Away": _loser if cointoss == 0 else _winner,
                    "Winner": "Home" if cointoss == 0 else "Away",
                }
                _data["_id"] = get_sha(_data["Info"], item["Winner"], item["Loser"])
                self.data_items.append(_data)

    def populate(self, collection):
        """push data items to collection"""
        for item in self.data_items:
            try:
                collection.insert_one(item)
            except DuplicateKeyError:
                pass
        print(f"Items: {collection.estimated_document_count()}")
