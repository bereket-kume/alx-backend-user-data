#!/usr/bin/env python3
"""
Main file
"""

import logging

get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS

# print(get_logger.__annotations__.get('return'))
# print("PII_FIELDS: {}".format(len(PII_FIELDS)))
logger = get_logger()
logger.info("name=Alice;email=alice@example.com;password=secret123;ssn=123-45-6789;phone_number=555-555-5555;")
