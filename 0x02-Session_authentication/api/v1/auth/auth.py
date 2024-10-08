#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import TypeVar, List
import os


class Auth:
    """
    Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        determine if given path require authentication
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        path = path.rstrip('/')
        for excluded_path in excluded_paths:
            excluded_path = excluded_path.rstrip('/')
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            else:
                if excluded_path == path or\
                        path.startswith(excluded_path + '/'):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        function that handel current user
        """
        return None

    def session_cookie(self, request=None):
        """
        method to return a cookie value from a request
        """
        if request is None:
            return None

        session_name = os.getenv("SESSION_NAME", "_my_session_id")
        return request.cookies.get(session_name)
