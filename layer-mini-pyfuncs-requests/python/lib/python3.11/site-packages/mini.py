#!/usr/bin/env python3
"""
Functions in module 'mini.py' called by a Lambda function.will be
used to exercise some functions in module 'pyfuncs.py'.
"""
import datetime
import inspect
import logging
import sys
import time


from pyfuncs import (
    eb_time_local,
    eb_time_utc,
    is_dt_today_a_weekday,
)


# 'import sys' REQUIRED to force:
# logging StreamHandler to use 'stdout" instead of 'stderr'

# Name the logger '__name__'
logger = logging.getLogger(name=__name__)
# log via 'logger.info; instead of 'logging.info'.
# Establish which severity of messages to pass to the handler
logger.setLevel(logging.INFO)
# Create a console handler OVERRIDE default '(sys.stderr)'
stream_handler = logging.StreamHandler(stream=sys.stdout)
# Establish which severity of messages to respond to
stream_handler.setLevel(logging.INFO)
# Creat a message format
stream_format = logging.Formatter(
    '%(asctime)s %(levelname)s:%(name)s'
    ':%(message)s', datefmt='%Y-%m-%d %H:%M:%S %Z')
# Add this format to the handler
stream_handler.setFormatter(stream_format)
# Convert loggint time to UTC
logging.Formatter.converter = time.gmtime
# Add handler to the logger
logger.addHandler(stream_handler)
# Disable progation to root logger - eliminate duplicate messages.
logger.propagate = False


def test_eb_time_local_zone_false():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    eb_time_local(False)


def test_eb_time_utc_zone_false():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    eb_time_utc(False)


def test_eb_time_local_zone_true():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    eb_time_local(True)


def test_eb_time_utc_zone_true():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}'\n")
    eb_time_utc(True)


def test_dt_weekend():
    # get the frame object of the function
    frame = inspect.currentframe()
    frame_detail = frame.f_code.co_name
    logger.info(f"Executing: '{frame_detail}")
    is_dt_today_a_weekday()
# EOF
