"""
@author: sta
"""
import logging
import os

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOGGER_LEVEL", logging.INFO))

formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(os.environ.get("LOGGER_LEVEL", logging.INFO))
logger.addHandler(stream_handler)
