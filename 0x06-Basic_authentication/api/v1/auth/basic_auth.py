#!/usr/bin/env python3
"""
Class to Class to manage basic API authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class to Class to manage basic API authentication
    """
