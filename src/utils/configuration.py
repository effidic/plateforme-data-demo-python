"""
@author: sta
"""

import os

from dotenv import load_dotenv, find_dotenv

__all__ = ("Configuration",)

# Le chargement du dotenv doit ce faire avant la creation de la classe.
load_dotenv(dotenv_path=find_dotenv(), override=True)


class Configuration:
    """
    Get Ringover, and Snowflake connection information
    """

    LOG_FORMAT = os.environ.get("LOG_FORMAT")
    LOG_LEVEL = os.environ.get("LOG_LEVEL")
    KEYFILE_CLIENT_EMAIL = os.environ.get("KEYFILE_CLIENT_EMAIL")
    KEYFILE_CLIENT_ID = os.environ.get("KEYFILE_CLIENT_ID")
    KEYFILE_PROJECT_ID = os.environ.get("KEYFILE_PROJECT_ID")
    KEYFILE_CLIENT_X509_CERT_URL = os.environ.get(
        "KEYFILE_CLIENT_X509_CERT_URL",
    )
    KEYFILE_PRIVATE_KEY = os.environ.get("KEYFILE_PRIVATE_KEY")
    KEYFILE_PRIVATE_KEY_ID = os.environ.get("KEYFILE_PRIVATE_KEY_ID")
    GCP_BUCKET_NAME = os.environ.get("GCP_BUCKET_NAME")
