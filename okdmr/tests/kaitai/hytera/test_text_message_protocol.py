from typing import List

from okdmr.kaitai.hytera.text_message_protocol import TextMessageProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_hytera_text_messages():
    hexmessages: List[str] = [
        # hytera short data defined, text message
        # probably 2bytes encoding (0x0001 => UTF-16-LE) and rest is text data
        "00014100480019804a002000540041004400590020004d004100520045004b00000000000000000000000000",
        # Is this really a txt message
        "0980a10022000000010a01b2070a03640e4f004c004900560045005200200054004500530054007a03",
    ]
    for hexmsg in hexmessages:
        prettyprint(TextMessageProtocol.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_hytera_text_messages()
