#!/usr/bin/env python3
"""
Session Db auth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime


class SessionDBAuth(SessionExpAuth):
    """
    Session Db Auth Class
    """
    def create_session(self, user_id: str = None) -> str:
        """
        function for create session and return
        session id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        info = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        user = UserSession(**info)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        function which return user_id depened on the
        session id
        """
        user_id = UserSession.search({"session_id": session_id})
        if user_id:
            return user_id

        return None

    def destroy_session(self, request=None):
        """
        function used for destorying session from user session
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
