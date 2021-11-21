from typing import List

from okdmr.kaitai.hytera.location_protocol import LocationProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_lp():
    hexmessages: List[str] = [
        # location protocol
        "a0030034000000000a2338630000413131323534303237303932314e353030332e383734364530313432362e35313932302e32323533ff1cae03",
    ]
    for hexmsg in hexmessages:
        prettyprint(LocationProtocol.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_lp()
