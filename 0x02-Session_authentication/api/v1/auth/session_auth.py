#!/usr/bin/env python3
"""
Session Auth module
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Session Auth Class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create session as key of the dictionary
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id
