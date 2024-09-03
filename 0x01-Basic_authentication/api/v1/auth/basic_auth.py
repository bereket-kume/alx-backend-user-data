#!/usr/bin/env python3
"""
Basic auth module
"""
import base64
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        """
        method extract base64 authorization header
        """
        if authorization_header is None or\
            not isinstance(authorization_header, str) or\
                not authorization_header.startswith("Basic" + " "):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str
    ) -> str:
        """
        decode base64 authorization header
        """
        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None
        try:
            decode_val = base64.b64decode(base64_authorization_header)
            val = decode_val.decode('utf-8')
            return val
        except Exception:
            return None
