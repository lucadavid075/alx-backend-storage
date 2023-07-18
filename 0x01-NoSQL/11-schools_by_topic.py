#!/usr/bin/env python3
"""
Task: Where can I learn Python? Ans: ALX
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns a list of school having a specific topic.
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
