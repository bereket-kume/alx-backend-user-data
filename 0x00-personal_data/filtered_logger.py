#!/usr/bin/env python3
"""
Filter_datum
"""
import re


def filter_datum(fields, redaction, message, seprator):
    """
    function returns the log message obfuscated
    """
    pattern = '|'.join([f"{fields}=.*?(?={seprator}|$)" for field in fields])
    return re.sub(
        pattern, lambda m: m.group(0).split('=')[0] + f'={redaction}', message
    )
