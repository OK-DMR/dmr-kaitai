from typing import List

from okdmr.kaitai.motorola.text_message_protocol import TextMessageProtocol
from okdmr.tests.tests_utils import prettyprint


def test_ahoj():
    hexstrings: List[str] = ["0010e00093040d000a00410048004f004a00"]

    for message_hex in hexstrings:
        prettyprint(TextMessageProtocol.from_bytes(bytes.fromhex(message_hex)))
