"""Script to download all docket public submissions."""

import json
from pydocket import RegulationDocumentSearch

DOCKET_ID = 'FDA-2017-N-4515'
SOURCE_FILENAME = 'docket_comments.json'

print('DOCKET: {}'.format(DOCKET_ID))
documents = RegulationDocumentSearch.all_comments_by_docket_id(DOCKET_ID)

print("\nWriting output to {}".format(SOURCE_FILENAME))
with open(SOURCE_FILENAME, 'w') as outfile:
    json.dump(documents, outfile, sort_keys=True, separators=(',\n', ': '))
