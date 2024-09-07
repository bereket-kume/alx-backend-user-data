#!/usr/bin/env python3
"""
user session model
"""
from .base import Base


class UserSession(Base):
    """
    User session class
    """
    def __init__(self, *args: list, **kwargs: dict):
        """
        init method for usersession
        user_id = user_id
        session_id = session_id
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
