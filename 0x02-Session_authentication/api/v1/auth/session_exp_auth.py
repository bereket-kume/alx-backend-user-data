#!/usr/bin/env python3
"""
Session Expiration Module
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """
    Session Expiration Class
    """
    def __init__(self) -> None:
        """
        init method
        """
        super().__init__()
        try:
            duration = int(os.getenv("SESSION_DURATION"))
        except ValueError:
            duration = 0
        self.session_duration = duration


    def create_session(self, user_id: str = None) -> str:
        """
        function to create session
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        session_info = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        print(session_info)
        self.user_id_by_session_id[session_id] = session_info
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        function for user id for session id
        """
        if session_id is None:
            return None

        session_info = self.user_id_by_session_id.get(session_id)
        created_at = session_info.get("created_at")
        user_id = session_info.get("user_id")

        print(f"created at {created_at}")
        if self.session_duration > 0:
            exp_time = created_at + timedelta(seconds=self.session_duration)
            if exp_time < datetime.now():
                del self.user_id_by_session_id[session_id]
                return None
        return user_id
