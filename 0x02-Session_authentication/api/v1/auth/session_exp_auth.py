#!/usr/bin/env python3
"""
Session Expiration Module
"""
import os
from datetime import datetime, timedelta
from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    Session Expiration Class that adds an expiration date to a session ID.
    """
    def __init__(self):
        """
        Initialize the class with session duration.
        """
        super().__init__()
        self.session_duration = self._get_session_duration()

    def _get_session_duration(self) -> int:
        """
        Retrieve and validate the session duration from environment variables.
        Returns:
            int: Session duration in seconds.
        """
        try:
            duration = int(os.getenv('SESSION_DURATION', 0))
        except ValueError:
            duration = 0
        return duration

    def create_session(self, user_id: str = None) -> str:
        """
        Create a new session ID for a given user_id.

        Args:
            user_id (str): The user ID to associate with the session.

        Returns:
            str: The session ID or None if session creation fails.
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_info = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_info
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieve the user ID for a given session ID,
        considering session expiration.

        Args:
            session_id (str): The session ID to look up.

        Returns:
            str: The user ID or None if session is expired or invalid.
        """
        if session_id is None:
            return None

        session_info = self.user_id_by_session_id.get(session_id)
        if session_info is None:
            return None

        created_at = session_info.get("created_at")
        if created_at is None:
            return None

        if self.session_duration > 0:
            expiration_time = created_at + timedelta(seconds=self.session_duration)
            if datetime.now() > expiration_time:
                del self.user_id_by_session_id[session_id]
                return None

        return session_info.get("user_id")
