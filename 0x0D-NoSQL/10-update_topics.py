#!/usr/bin/env python3
"""
Python function that changes all topics
of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics
    of a school document based on the name
    """
    return mongo_collection.update({"name": name}, {'$set': {"topics": topics}})
