

from dataclasses import dataclass

@dataclass
class Datasource:
    url: str
    destination_blob_name: str


data_sources= [
    Datasource(
        url = 'https://www.data.gouv.fr/fr/datasets/r/98f3161f-79ff-4f16-8f6a-6d571a80fea2',
        destination_blob_name = 'sante/finess.csv'
    ),
    Datasource(
        # pylint: disable-next=line-too-long
        url = 'https://opendata.datainfogreffe.fr/api/explore/v2.1/catalog/datasets/chiffres-cles-2021/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B',
        destination_blob_name = 'infogreffe/chiffre_cle_2021.csv'
    )
]