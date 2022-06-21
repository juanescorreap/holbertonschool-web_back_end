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
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return None
        if path[-1] != '/':
            path = path + '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        Validates all requests to secure the API
        """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user method"""
        pass
