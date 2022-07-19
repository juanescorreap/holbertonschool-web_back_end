#!/usr/bin/env python3
""""
Class that uses redis as a simple chache
"""
import redis
from typing import Union, Optional, Callable
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

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float]:
        """
        Method to get data from redis and
        convert it back to the desired format
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """"
        Method to get data from redis
        and parametrize Cache.get to str
        """
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """"
        Method to get data from redis
        and parametrize Cache.get to str
        """
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data
