"""
RegulationDocument Class.

Swagger documentation for Regulations.gov document endpoint:
https://github.com/regulationsgov/developers/blob/gh-pages/api-docs/documents.json
"""

from . import session

ENDPOINT = 'https://api.data.gov/regulations/v3/document.json'


class RegulationDocument(object):
    """RegulationDocument Class."""

    def __init__(self, docket_id, document_id):
        """Constructor."""
        self.docket_id = docket_id
        self.document_id = document_id

    def get(self):
        """GET method."""
        path = ENDPOINT + '?docketId={}&documentId={}'.format(self.docket_id,
                                                              self.document_id)
        response = session.get(path)
        return response.json()
