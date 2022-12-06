import os
import sys
import certifi
from pymongo import MongoClient


def get_client():
    with open(os.path.join(sys.path[0], "config.ini"), "r") as f:
        content = f.readlines()
    client = MongoClient(
        "mongodb+srv://Aoishi:" + content[0] + "@cluster0.zpuftvw.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=certifi.where())

    return client
