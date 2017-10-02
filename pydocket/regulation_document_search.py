"""
RegulationDocumentSearch Class.

Swagger documentation for Regulations.gov documents endpoint:
https://github.com/regulationsgov/developers/blob/gh-pages/api-docs/documents.json
"""

from . import session

ENDPOINT = 'https://api.data.gov/regulations/v3/documents.json'


class RegulationDocumentSearch(object):
    """RegulationDocumentSearch Class."""

    def __init__(self):
        """Constructor."""
        pass

    @staticmethod
    def number_of_records(docket_id, document_type=''):
        """Retrieve number of records in a docket."""
        parameters = 'dktid={}&countsOnly={}'.format(docket_id, 1)

        # Retrieve all document types by default
        if document_type != '':
            document_type_parameter = '&dct={}'.format(document_type)
            parameters += document_type_parameter

        path = ENDPOINT + '?' + parameters
        response = session.get(path)
        return response.json()['totalNumRecords']

    @staticmethod
    def by_docket_id(docket_id, document_type='',
                     results_per_page=10, offset=0,
                     sort_by='postedDate', sort_order='ASC'):
        """Search and retrieve records by docket ID."""
        parameter_string = 'dktid={}&rpp={}&po={}&sb={}&so={}'
        parameters = parameter_string.format(docket_id,
                                             results_per_page, offset,
                                             sort_by, sort_order)

        # Retrieve all document types by default
        if document_type != '':
            document_type_parameter = '&dct={}'.format(document_type)
            parameters += document_type_parameter

        path = ENDPOINT + '?' + parameters
        response = session.get(path)
        return response.json()

    @staticmethod
    def all_comments_by_docket_id(docket_id,
                                  sort_by='postedDate', sort_order='ASC'):
        """Search and retrieve all public submissions by docket ID."""
        # Determine total number of public submissions in docket.
        params = {'docket_id': docket_id, 'document_type': 'PS'}
        total_records = RegulationDocumentSearch.number_of_records(**params)

        # Use the maximum page size to download all public submissions.
        documents = []
        for page in range(total_records // 1000 + 1):
            parameters = {
                'docket_id': docket_id,
                'document_type': 'PS',
                'results_per_page': 1000,
                'offset': page * 1000,
                'sort_by': sort_by,
                'sort_order': sort_order
            }
            response = RegulationDocumentSearch.by_docket_id(**parameters)
            documents.extend(response['documents'])

        return documents
