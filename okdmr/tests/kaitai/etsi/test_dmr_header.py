from typing import List

from okdmr.kaitai.etsi.dmr_data_header import DmrDataHeader
from okdmr.tests.tests_utils import prettyprint


def test_defined_data_header():
    hexstrings: List[str] = [
        "4da323383b23383b05608040",
    ]

    for header_hex in hexstrings:
        header = DmrDataHeader.from_bytes(bytes.fromhex(header_hex))
        prettyprint(header)
        prettyprint(header.data)
