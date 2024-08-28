#!/usr/bin/env python3
"""
Filter_datum
"""
import re


def filter_datum(fields, redaction, message, seprator):
    """
    function returns the log message obfuscated
    """
    for i in fields:
        message = re.sub(f'{i}=.*?{seprator}',
                         f'{i}={redaction}{seprator}', message)
    return message
