import logging

__all__ = [
    'get_logger'
]

def get_logger(name):
    logger = logging.getLogger(name)
    # TODO: set level, add handler
    return logger
