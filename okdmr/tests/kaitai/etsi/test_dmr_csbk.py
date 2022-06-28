#!/usr/bin/env python3
from typing import List

from okdmr.kaitai.etsi.dmr_csbk import DmrCsbk
from okdmr.kaitai.tools.prettyprint import prettyprint


def test_csbk():
    # Feel free to append these hexstrings for simple tests
    hexmessages: List[str] = ["bd0080180008fd23383bb2ed"]

    for hexmsg in hexmessages:
        prettyprint(DmrCsbk.from_bytes(bytes.fromhex(hexmsg)))
