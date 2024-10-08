#!/usr/bin/env python3
"""
Session Auth module
"""
from .auth import Auth
import uuid
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        User id for session id in the dictionary
        """
        if session_id is None and not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        method to return current user depend on user id
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """
        method for destroy session
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        if not self.user_id_by_session_id.get(session_id):
            return False
        del self.user_id_by_session_id[session_id]
        return True
