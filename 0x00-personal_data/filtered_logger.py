#!/usr/bin/env python3
"""
Module for handling personal data
"""
from typing import List
import re


def filter_datum(
        fields: List[str], redaction: str,
        message: str, seprator: str
) -> str:
    """
    function returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(f'{i}=.*?{seprator}',
                         f'{i}={redaction}{seprator}', message)
    return message
