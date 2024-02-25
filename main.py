"""
@author: sta
"""

import requests

from google.cloud import storage
from google.oauth2 import service_account
from utils.configuration import Configuration
from utils.logger import logger

conf = Configuration()


def stream_download_upload(source_url, bucket_name, destination_blob_name):
    """
    Télécharge un fichier et le recharge en streaming sur un bucket gcp
    """
    service_account_info = {
        "type": "service_account",
        "project_id": conf.KEYFILE_PROJECT_ID,
        "private_key_id": conf.KEYFILE_PRIVATE_KEY_ID,
        "private_key": conf.KEYFILE_PRIVATE_KEY,
        "client_email": conf.KEYFILE_CLIENT_EMAIL,
        "client_id": conf.KEYFILE_CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": conf.KEYFILE_CLIENT_X509_CERT_URL,
    }

    credentials = service_account.Credentials.from_service_account_info(
        service_account_info
    )
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Taille des morceaux de fichier
    blob.chunk_size = 50 * 1024 * 1024  # Définir la taille du chunk à 5MB

    # Requête GET en streaming et upload au bucket
    with requests.get(source_url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with blob.open("wb") as blob_file:
            for chunk in r.iter_content(
                chunk_size=20 * 1024 * 1024
            ):  # Taille du morceau à 1MB
                if chunk:  # Filtrer les keep-alive new chunks
                    blob_file.write(chunk)

logger.info(conf.KEYFILE_PRIVATE_KEY)
logger.info(f"longueur : {len(conf.KEYFILE_PRIVATE_KEY)}")
# pylint: disable-next=line-too-long
chiffre_cle_2022_url = """https://opendata.datainfogreffe.fr/api/explore/v2.1/catalog/datasets/chiffres-cles-2022/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"""
infogreffe_bucket_name = "effidic-open-data"
chiffre_cle_2022_destination_blob_name = "infogreffe/chiffre_cle_2022.csv"
logger.info(
    "Téléchargement de chiffre_cle_2022.csv et chargement en streaming dans le bucket %s",
    infogreffe_bucket_name,
)
stream_download_upload(
    chiffre_cle_2022_url, infogreffe_bucket_name, chiffre_cle_2022_destination_blob_name
)
logger.info("Téléchargement terminé")
