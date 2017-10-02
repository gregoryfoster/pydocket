"""PyDocket package root."""

import os
import requests

DATA_GOV_API_KEY = os.environ.get('DATA_GOV_API_KEY', None)


class APIKeyMissingError(Exception):
    """Exception for handling a missing Data.gov API Key."""

    pass


if DATA_GOV_API_KEY is None:
    raise APIKeyMissingError(
        'All methods require a Data.gov API key. Signup at '
        'https://api.data.gov/signup/ and export the value in your '
        'environment as DATA_GOV_API_KEY.'
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = DATA_GOV_API_KEY

from .regulation_docket import RegulationDocket
from .regulation_document import RegulationDocument
from .regulation_document_search import RegulationDocumentSearch
