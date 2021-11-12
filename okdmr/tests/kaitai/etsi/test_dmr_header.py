from typing import List

from okdmr.kaitai.etsi.dmr_data_header import DmrDataHeader
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_dmr_data_headers():
    hexmessages: List[str] = [
        "4da323383b23383b05608040",
    ]

    for hexmsg in hexmessages:
        header = DmrDataHeader.from_bytes(bytes.fromhex(hexmsg))
        prettyprint(header)
        prettyprint(header.data)
