#!/usr/bin/env python3
"""
Class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks whether the end point being
        accessed requires authentication or not
        """
        pass

    def authorization_header(self, request=None) -> str:
        """
        Validates all requests to secure the API
        """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        pass
