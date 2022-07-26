#!/usr/bin/env python3
"""
Python script that provides some stats
about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def method_requester(method_dict: dict) -> int:
    """
    Makes a request to the database
    """
    client = MongoClient('https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip')
    logs = client.logs.nginx
    return logs.count_documents(method_dict)


def printer():
    """
    Prints stats about Nginx
    logs stored in MongoDB
    """
    print(f"{method_requester({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {method_requester({'method': 'GET'})}")
    print(f"\tmethod POST: {method_requester({'method': 'POST'})}")
    print(f"\tmethod PUT: {method_requester({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {method_requester({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {method_requester({'method': 'DELETE'})}")
    print(f"{method_requester({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    printer()
