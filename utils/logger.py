import logging
import sys


def get_logger(log_type, name):
    """Get a logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    if log_type:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
    else:
        file_handler = logging.FileHandler('system.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
