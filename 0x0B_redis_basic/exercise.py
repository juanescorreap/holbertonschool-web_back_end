#!/usr/bin/env python3
""""
Class that uses redis as a simple chache
"""
import redis
from typing import Union
from uuid import uuid4


class Cache():
    """"
    Class that uses redis as a simple chache
    """
    def __init__(self):
        """
        Constructor method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Method that stores data in redis
        using a randomly generated key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
