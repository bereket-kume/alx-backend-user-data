#!/usr/bin/env python3
"""Module for handling personal data"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Return filtered values from log records"""
        original_message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION, original_message, self.SEPARATOR)


PII_FIELDS = ('name', 'email', 'phone_number', 'ssn', 'password')


def filter_datum(
        fields: List[str], redaction: str,
        message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = '|'.join([f"{field}=.*?(?={separator}|$)" for field in fields])
    return re.sub(
        pattern, lambda m: m.group(0).split('=')[0] + f'={redaction}', message
        )


def get_logger() -> logging.Logger:
    """
    Function that takes no arguments
    return a logging.logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    streamHandler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    return logger
