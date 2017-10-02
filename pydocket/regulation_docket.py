"""
RegulationDocket Class.

Swagger documentation for Regulations.gov docket endpoint:
https://github.com/regulationsgov/developers/blob/gh-pages/api-docs/dockets.json
"""

from . import session

ENDPOINT = 'https://api.data.gov/regulations/v3/docket.json'


class RegulationDocket(object):
    """RegulationDocket Class."""

    def __init__(self, docket_id):
        """Constructor."""
        self.docket_id = docket_id

    def get(self):
        """GET method."""
        path = ENDPOINT + '?docketId={}'.format(self.docket_id)
        response = session.get(path)
        return response.json()
