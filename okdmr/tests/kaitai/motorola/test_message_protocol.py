from typing import Dict

from okdmr.kaitai.motorola.text_message_protocol import TextMessageProtocol
from okdmr.kaitai.tools.prettyprint import prettyprint
from okdmr.tests.kaitai.test_utils import assert_expected_attribute_values


def test_mototrbo_text_messages():
    hexmessages: Dict[str, Dict[str, any]] = {
        "0010e00093040d000a00410048004f004a00": {
            "len_address": 0,
            "message_header": {
                "acknowledgement_required": True,
                "control_user_bit": False,
                "extension_bit": True,
                "pdu_type": 0,
                "reserved": True,
            },
            "message_size": 16,
            "pdu_content": {
                "text_message": "\r\nAHOJ",
                "text_message_header_sequence_and_encoding": {
                    "encoding": 4,
                    "has_encoding_header": True,
                    "header_encoding_extension": False,
                    "reserved_1": 0,
                    "sequence_number_lsb_bits": 19,
                    "sequence_number_msb_bits": 0,
                },
            },
        }
    }

    for hexmsg, expectations in hexmessages.items():
        tmp = TextMessageProtocol.from_bytes(bytes.fromhex(hexmsg))
        prettyprint(tmp)
        assert_expected_attribute_values(tmp, expectations)
