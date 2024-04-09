"""
Fichier principale
@author: sta
"""

import sys
from utils.configuration import Configuration
from utils.logger import logger
from utils.gcp import stream_download_upload, local_upload
from utils.data_sources import data_sources


BUCKET_NAME = "effidic-open-data"


def main():
    """Fonction principale du script python."""
    for data_source in data_sources:
        logger.info("Traitement de la Data_source : %s", data_source)
        if data_source.file_type == 'stream':
            stream_download_upload(
                bucket_name=Configuration.GCP_BUCKET_NAME,
                destination_blob_name=data_source.destination_blob_name,
                source_url=data_source.url,
            )
        elif data_source.file_type == 'local':
            local_upload(
                source_path=data_source.url,
                bucket_name=Configuration.GCP_BUCKET_NAME,
                destination_blob_name=data_source.destination_blob_name,
                )
        else:
            raise KeyError()
    logger.info("job etl terminé")

    sys.exit(0)


if __name__ == "__main__":
    main()
