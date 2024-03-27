import requests

from google.cloud import storage
from google.oauth2 import service_account

from utils.configuration import Configuration as conf
from utils.logger import logger



def stream_download_upload(source_url, bucket_name, destination_blob_name):
    """
    Télécharge un fichier depuis une URL donnée et le charge dans un bucket Google Cloud Storage.

    Cette fonction récupère le contenu situé à l'URL source spécifiée, puis le charge directement dans un blob
    au sein d'un bucket Google Cloud Storage, sans nécessiter de stockage intermédiaire sur le disque local.
    Le téléchargement et le chargement se font par morceaux pour gérer efficacement la mémoire et la bande passante.

    Parameters:
    - source_url (str): L'URL du fichier source à télécharger.
    - bucket_name (str): Le nom du bucket Google Cloud Storage où le fichier sera chargé.
    - destination_blob_name (str): Le nom du blob dans le bucket où le fichier sera stocké.

    La fonction utilise les informations d'identification du compte de service définies dans le module `conf`
    pour authentifier la session Google Cloud Storage.

    Raises:
    - Exception: Provoque une exception si la requête HTTP échoue ou si d'autres erreurs surviennent pendant
      le téléchargement ou le chargement du fichier.
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
    chunk_size=200 * 1024 * 1024

    blob.chunk_size = chunk_size

    with requests.get(source_url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with blob.open("wb") as blob_file:
            for chunk in r.iter_content(
                chunk_size=chunk_size
            ):
                if chunk:
                    blob_file.write(chunk)
