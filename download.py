"""Script to download all docket public submissions."""

import json
from pydocket import RegulationDocumentSearch

DOCKET_ID = 'FDA-2017-N-4515'
TARGET_FILENAME = 'docket_comments.json'

print('DOCKET: {}'.format(DOCKET_ID))
documents = RegulationDocumentSearch.all_comments_by_docket_id(DOCKET_ID)

print('Writing output to {}'.format(TARGET_FILENAME))
with open(TARGET_FILENAME, 'w') as outfile:
    json.dump(documents, outfile, sort_keys=True, separators=(',\n', ': '))
