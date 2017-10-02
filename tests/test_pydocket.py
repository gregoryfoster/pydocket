"""Test the pydocket module."""
import json
from pytest import fixture
import vcr
from pydocket import RegulationDocument, RegulationDocket, \
    RegulationDocumentSearch

DOCKET_ID = 'FDA-2017-N-4515'
DOCUMENT_ID = 'FDA-2017-N-4515-3417'

#    print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))


@fixture
def docket_keys():
    """A list of Regulations.gov docket keys."""
    return ['agency', 'agencyAcronym', 'docketId',
            'field2', 'generic', 'keywords', 'numberOfComments',
            'parentAgency', 'parentAgencyAcronym', 'program', 'shortTitle',
            'title', 'type']


@fixture
def document_keys():
    """A list of Regulations.gov document keys."""
    return ['agencyAcronym', 'agencyName', 'allowLateComment',
            'attachmentCount', 'comment', 'commentCategory', 'commentDueDate',
            'commentOnDoc', 'commentStartDate', 'docSubType', 'docketId',
            'docketTitle', 'docketType', 'documentId', 'documentType',
            'numItemsRecieved', 'openForComment', 'postedDate', 'receivedDate',
            'status', 'title', 'trackingNumber']


@fixture
def document_search_keys():
    """A list of Regulations.gov document search keys."""
    return ['documents', 'totalNumRecords']


@vcr.use_cassette('tests/vcr_cassettes/docket-get.yml')
def test_docket_get(docket_keys):
    """Test an API call to get a Regulations.gov docket's data."""
    docket = RegulationDocket(DOCKET_ID)
    response = docket.get()

    assert isinstance(response, dict)
    assert response['docketId'] == DOCKET_ID, \
        'The ID should be in the response'
    assert set(docket_keys).issubset(response.keys()), \
        'All keys should be in the response'


@vcr.use_cassette('tests/vcr_cassettes/document-get.yml')
def test_document_get(document_keys):
    """Test an API call to get a Regulations.gov document's data."""
    document = RegulationDocument(DOCKET_ID, DOCUMENT_ID)
    response = document.get()

    assert isinstance(response, dict)
    assert response['documentId']['value'] == DOCUMENT_ID, \
        'The ID should be in the response'
    assert set(document_keys).issubset(response.keys()), \
        'All keys should be in the response'


@vcr.use_cassette('tests/vcr_cassettes/search-number_of_records.yml')
def test_search_number_of_records():
    """Test API call to search for the total number of records by docket ID."""
    response = RegulationDocumentSearch.number_of_records(DOCKET_ID)

    assert isinstance(response, int), 'Response should be an integer'
    assert response == 6585, 'Response should be 6585'


@vcr.use_cassette('tests/vcr_cassettes/search-number_of_records-w_dct.yml')
def test_search_number_of_records_w_dct():
    """
    Test API call to search for the total number of records by docket ID.

    Includes document type parameter (dct).  Valid values for dct are
    [ 'N': Notice, 'PR': Proposed Rule, 'FR': Rule, 'O': Other,
    'SR': Supporting & Related Material, 'PS': Public Submission ].
    """
    parameters = {'docket_id': DOCKET_ID, 'document_type': 'N'}
    response = RegulationDocumentSearch.number_of_records(**parameters)

    assert isinstance(response, int), 'Response should be an integer'
    assert response == 2, 'Response should be 2'


@vcr.use_cassette('tests/vcr_cassettes/search-by_dktid.yml')
def test_search_by_dktid(document_search_keys):
    """Test API call to search for Regulations.gov documents by docket ID."""
    response = RegulationDocumentSearch.by_docket_id(DOCKET_ID)

    assert isinstance(response, dict), 'Response should be a dictionary'
    assert set(document_search_keys).issubset(response.keys()), \
        'All keys should be in the response'
    assert len(response['documents']) == 10, \
        'Query should return 10 documents by default'


@vcr.use_cassette('tests/vcr_cassettes/search-by_dktid_dct.yml')
def test_search_by_dktid_w_dct():
    """
    Test API call to search for Regulations.gov documents by docket ID.

    Includes document type parameter (dct).  Valid values for dct are
    [ 'N': Notice, 'PR': Proposed Rule, 'FR': Rule, 'O': Other,
    'SR': Supporting & Related Material, 'PS': Public Submission ].
    """
    parameters = {'docket_id': DOCKET_ID, 'document_type': 'N'}
    response = RegulationDocumentSearch.by_docket_id(**parameters)

    assert len(response['documents']) == 2, \
        'Query should return 2 documents'
    assert response['documents'][0]['documentType'] == 'Notice', \
        'Response document type should be Notice'


@vcr.use_cassette('tests/vcr_cassettes/search-by_dktid-rpp.yml')
def test_search_by_dktid_w_rpp():
    """
    Test API call to search for Regulations.gov documents by docket ID.

    Includes results per page parameter (rpp).  Valid values for rpp
    are [ 10, 25, 100, 500, 1000 ].
    """
    parameters = {'docket_id': DOCKET_ID, 'results_per_page': 25}
    response = RegulationDocumentSearch.by_docket_id(**parameters)

    assert len(response['documents']) == 25, 'Query should return 25 documents'


@vcr.use_cassette('tests/vcr_cassettes/search-by_dktid-rpp-po.yml')
def test_search_by_dktid_w_rpp_po():
    """
    Test API call to search for Regulations.gov documents by docket ID.

    Includes results per page parameter (rpp) and page offset (po).
    Valid values for rpp are [ 10, 25, 100, 500, 1000 ].  Page offset
    begins at 0 and generally should increment by results per page.
    """
    parameters = {
        'docket_id': DOCKET_ID,
        'results_per_page': 25,
        'offset': 6575
    }
    response = RegulationDocumentSearch.by_docket_id(**parameters)

    assert len(response['documents']) == 10, 'Query should return 10 documents'


@vcr.use_cassette('tests/vcr_cassettes/search-by_dktid-sort_asc.yml')
def test_search_by_dktid_w_sort_asc():
    """
    Test API call to search for Regulations.gov documents by docket ID.

    Includes sort by (sb) posted date and sort order (so) ascending.
    Valid values for sb are [ "docketId", "docId", "title", "postedDate",
    "agency", "documentType", "submitterName", "organization" ].  Valid values
    for so are [ "ASC", "DESC" ].
    """
    parameters = {
        'docket_id': DOCKET_ID,
        'results_per_page': 100,
        'offset': 0,
        'sort_by': 'postedDate',
        'sort_order': 'ASC'
    }
    response = RegulationDocumentSearch.by_docket_id(**parameters)

    first_doc_date = response['documents'][0]['postedDate']
    second_doc_date = response['documents'][99]['postedDate']
    assert first_doc_date <= second_doc_date, \
        'Response documents should be in ascending sort order'


@vcr.use_cassette('tests/vcr_cassettes/search-by_dktid-sort_desc.yml')
def test_search_by_dktid_w_sort_desc():
    """
    Test API call to search for Regulations.gov documents by docket ID.

    Includes sort by (sb) posted date and sort order (so) descending.
    Valid values for sb are [ "docketId", "docId", "title", "postedDate",
    "agency", "documentType", "submitterName", "organization" ].  Valid values
    for so are [ "ASC", "DESC" ].
    """
    parameters = {
        'docket_id': DOCKET_ID,
        'results_per_page': 100,
        'offset': 0,
        'sort_by': 'postedDate',
        'sort_order': 'DESC'
    }
    response = RegulationDocumentSearch.by_docket_id(**parameters)

    first_doc_date = response['documents'][0]['postedDate']
    second_doc_date = response['documents'][99]['postedDate']
    assert first_doc_date >= second_doc_date, \
        'Response documents should be in descending sort order'


def test_search_all_comments():
    """Test API call to retrieve all Regulations.gov comments by docket ID."""
    comments = RegulationDocumentSearch.all_comments_by_docket_id(DOCKET_ID)

    assert isinstance(comments, list), 'Response should be a list'
    assert len(comments) == 6581, \
        'Query should return 6581 documents by default'

    first_doc_date = comments[0]['postedDate']
    last_doc_date = comments[-1]['postedDate']
    assert first_doc_date <= last_doc_date, \
        'Comments should be in ascending sort order by default'
