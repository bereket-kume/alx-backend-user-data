#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from typing import ByteString


def _hash_password(password: str) -> ByteString:
    """
    Hash password:
        return salted ofthe input password
    """
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(password.encode(), salt)
    return hash_pass
