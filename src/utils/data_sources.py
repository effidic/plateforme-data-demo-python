"""Module de gestion des source de données"""

# flake8: noqa

from dataclasses import dataclass


@dataclass
class Datasource:
    """Class contenant l'url et la destination de la donnée."""

    def __init__(self, url: str, destination_blob_name: str, file_type:str = 'stream'):
        self.url = url
        self.destination_blob_name = destination_blob_name
        self.file_type = file_type


# Liste des sources de données à charger
data_sources = [
    # Datasource(
    #     url="https://www.data.gouv.fr/fr/datasets/r/98f3161f-79ff-4f16-8f6a-6d571a80fea2",
    #     destination_blob_name="sante/finess.csv",
    # ),
    # Datasource(
    #     url="https://opendata.datainfogreffe.fr/api/explore/v2.1/catalog/datasets/chiffres-cles-2021/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
    #     destination_blob_name="infogreffe/chiffre_cle_2021.csv",
    # ),
    # # Datasource(
    # #     url="https://www.data.gouv.fr/fr/datasets/r/ba6a4e4c-aac6-4764-bbd2-f80ae345afc5",
    # #     destination_blob_name="geo/GeolocalisationEtablissement_Sirene.csv",
    # # ),
    # Datasource(
    #     url="https://data.paysdelaloire.fr/api/explore/v2.1/catalog/datasets/120027016_base-sirene-v3-ss/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
    #     destination_blob_name="PDL/base-sirene-v3.csv",
    # ),
    # Datasource(
    #     url="https://data.paysdelaloire.fr/api/explore/v2.1/catalog/datasets/234400034_observatoire2g-3g-4g-2018/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
    #     destination_blob_name="PDL/observatoire2g-3g-4g.csv",
    # ),
    # Datasource(
    #     url="https://data.paysdelaloire.fr/api/explore/v2.1/catalog/datasets/234400034_-bornes-de-recharge/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B",
    #     destination_blob_name="PDL/bornes-de-recharge.csv",
    # ),
    # Datasource(
    #     url="https://files.data.gouv.fr/geo-dvf/latest/csv/2023/departements/49.csv.gz",
    #     destination_blob_name="immo/demande-valeur-fonciere-49.csv.gz",
    # ),
    Datasource(
        url="../data/immo/mandats.csv",
        destination_blob_name="immo/mandats.csv",
        file_type='local'
    ),
    Datasource(
        url="../data/olympics/dictionary.csv",
        destination_blob_name="olympics/dictionary.csv",
        file_type='local'
    ),
    Datasource(
        url="../data/olympics/summer.csv",
        destination_blob_name="olympics/summer.csv",
        file_type='local'
    ),
    Datasource(
        url="../data/olympics/winter.csv",
        destination_blob_name="olympics/winter.csv",
        file_type='local'
    ),

]
