#!/usr/bin/env python3
from typing import List

from okdmr.kaitai.etsi.dmr_csbk import DmrCsbk
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_csbk():
    # Feel free to append these hexstrings for simple tests
    hexmessages: List[str] = [
        "444d52440923383b0008fd0006690fe33391012951dd0c4d8bb40ac413a86c5094fdff57d75df5dcadfa1268aaa87b82b9d8291910003c"
    ]

    for hexmsg in hexmessages:
        prettyprint(DmrCsbk.from_bytes(bytes.fromhex(hexmsg)))
