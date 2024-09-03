#!/usr/bin/env python3
"""
Basic auth module
"""
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str
    ) -> str:
        if authorization_header is None or\
            not isinstance(authorization_header, str) or\
                not authorization_header.startswith("Basic" + " "):
            return None
        else:
            return authorization_header[6:]
