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