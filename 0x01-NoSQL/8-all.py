#!/usr/bin/env python3
"""
Task: List all documents in Python
"""


def list_all(mongo_collection):
    """
    Function that lists all documents in a collection.
    """
    return [doc for doc in mongo_collection.find()]
