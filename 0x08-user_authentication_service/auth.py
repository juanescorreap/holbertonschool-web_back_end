#!/usr/bin/env python3
"""
Method that takes in a password string
arguments and returns bytes
"""
from xmlrpc.client import Boolean
from db import DB
import bcrypt
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Method that takes in a password string
    arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Method to register a new user in the database
        """
        try:
            registered_user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            registered_user = self._db.add_user(email, hashed_password)
            return registered_user
        else:
            raise ValueError

    def valid_login(self, email: str, password: str) -> bool:
        """
        Method that locates the user by email.
        If the password matches returns True,
        otherwise returns False.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            hashed_password = _hash_password(password)
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
