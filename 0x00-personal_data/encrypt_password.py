#!/usr/bin/env python3
"""
Module password encrypting
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    encrypting passwords
    """
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check valid password
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
