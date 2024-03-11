"""
@author: sta
"""


from utils.configuration import conf
from utils.logger import logger
from utils.gcp import stream_download_upload
from utils.data_sources import data_sources


bucket_name = "effidic-open-data"
for data_source in data_sources:
    logger.info(f"Traitement de la Data_source : {data_source}")
    stream_download_upload(
        bucket_name= conf.GCP_BUCKET_NAME,
        destination_blob_name=data_source.destination_blob_name,
        source_url = data_source.url
    )
logger.info("job etl terminé")
