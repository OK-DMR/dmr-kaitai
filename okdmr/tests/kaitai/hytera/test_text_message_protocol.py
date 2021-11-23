from typing import List

from okdmr.kaitai.hytera.text_message_protocol import TextMessageProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_lp():
    hexmessages: List[str] = [
        # this is not a text message?
        "a0030034000000000a2338630000413131323534303237303932314e353030332e383734364530313432362e35313932302e32323533ff1cae03",
        # Is this really a txt message
        "0980a10022000000010a01b2070a03640e4f004c004900560045005200200054004500530054007a03"
    ]
    for hexmsg in hexmessages:
        prettyprint(TextMessageProtocol.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_lp()
