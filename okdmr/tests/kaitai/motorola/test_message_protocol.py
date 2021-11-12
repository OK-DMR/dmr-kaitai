from typing import List

from okdmr.kaitai.motorola.text_message_protocol import TextMessageProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_mototrbo_text_messages():
    hexmessages: List[str] = ["0010e00093040d000a00410048004f004a00"]

    for hexmsg in hexmessages:
        prettyprint(TextMessageProtocol.from_bytes(bytes.fromhex(hexmsg)))
