import sys
import logging

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver as get_libcloud_driver

from pod_manager.settings import LOG_LEVEL, LOG_FORMAT
from pod_manager.settings import PROVIDER, PROVIDER_CREDENTIALS, PROVIDER_KWARGS

__all__ = [
    'get_logger',
    'get_driver'
]

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.__stdout__)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_driver():
    cls = get_libcloud_driver(PROVIDER)
    driver = cls(*PROVIDER_CREDENTIALS, **PROVIDER_KWARGS)
    return driver
