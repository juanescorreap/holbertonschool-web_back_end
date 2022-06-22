#!/usr/bin/env python3
"""
Class to Class to manage basic API authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, encode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class to Class to manage basic API authentication
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        base_64 = authorization_header.split(' ')
        return base_64[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded = b64decode(encoded)
            decoded_base = decoded.decode('utf-8')
            return decoded_base
        except Exception:
            return None
