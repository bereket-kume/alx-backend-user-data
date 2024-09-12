#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from typing import ByteString
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Optional


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        function to register user
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            hash_pass = _hash_password(password)
            user = db.add_user(email=email, hashed_password=hash_pass)
            return user
        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        function  for credentials validation
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode(), user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        function to create session:
            return session_id
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        get_user_from_session_id function
        """
        db = self._db
        try:
            user = db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """
        function to destory session
        """
        db = self._db
        db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        function to get_reset_password_token
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        db = self._db
        try:
            user = db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        db.update_user(user.id, hashed_password=_hash_password(password))


def _hash_password(password: str) -> bytes:
    """
    Hash password:
        return salted ofthe input password
    """
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(password.encode(), salt)
    return hash_pass


def _generate_uuid() -> str:
    """
    function to generate uuid
    """
    return str(uuid4())
