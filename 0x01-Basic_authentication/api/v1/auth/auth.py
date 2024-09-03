#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import TypeVar


class Auth:
    """
    Auth Class
    """
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """
        function used as auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        function that handel current user
        """
        return None
