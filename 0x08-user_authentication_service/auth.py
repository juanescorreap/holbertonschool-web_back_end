#!/usr/bin/env python3
"""
Method that takes in a password string
arguments and returns bytes
"""
from cmath import e
from xmlrpc.client import Boolean
from db import DB
import bcrypt
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Method that takes in a password string
    arguments and returns bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Method that generates an UUID
    """
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """
        Method that creates a user's session ID
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
