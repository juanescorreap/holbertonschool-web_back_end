#!/usr/bin/env python3
"""DB module to create, find and update an user
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base, User


class DB:
    """DB class to manage the database
    """

    def __init__(self):
        """Constructor to initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
            creates a new session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Method that saves an user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Takes in arbitrary keyword arguments and returns
        the first row found in the users table as filtered
        by the method's input arguments
        """
        if kwargs is None:
            raise InvalidRequestError
        query_result = self._session.query(User).filter_by(**kwargs).first()
        if query_result is None:
            raise NoResultFound
        return query_result
