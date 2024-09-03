#!/usr/bin/env python3
"""
Basic auth module
"""
import base64
from .auth import Auth
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Basic Auth Class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """
        method extract base64 authorization header
        """
        if authorization_header is None or\
            not isinstance(authorization_header, str) or\
                not authorization_header.startswith("Basic" + " "):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
    ) -> str:
        """
        decode base64 authorization header
        """
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_val = base64.b64decode(base64_authorization_header)
            val = decode_val.decode('utf-8')
            return val
        except Exception:
            return None

    def extract_user_credentials(
            self, decode_base64_authorization_header: str
    ) -> Tuple:
        """
        extract user credentials from header
        """
        if decode_base64_authorization_header is None or\
            not isinstance(decode_base64_authorization_header, str) or\
                ":" not in decode_base64_authorization_header:
            return (None, None)
        email, password = decode_base64_authorization_header.split(':')
        return (email, password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        """
        returns the user instance based on the email
        and password
        """
        if user_email is None or not isinstance(user_email, str) or\
                user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None
        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user
        return None
