from typing import Dict

from okdmr.kaitai.hytera.radio_control_protocol import RadioControlProtocol
from okdmr.kaitai.tools.prettyprint import prettyprint
from okdmr.tests.kaitai.test_utils import assert_expected_attribute_values


def test_rcp():
    # messages must not start with 0x20, the type header is not supported by radio_control_protocol.ksy
    hexmessages: Dict[str, Dict[str, any]] = {
        # rcp identification request opcode 0x0004
        "040005006400000001": {
            "data": {"data": b"d\x00\x00\x00\x01"},
            "message_length": 5,
            "service_type": RadioControlProtocol.ServiceTypes.radio_identification_request,
        },
        # rcp identification response opcode 0x82D4
        "d482ce00000f6906000200440039002e00300030002e00300037002e003200310030002e0069004d000000410039002e00300030002e00300038002e003300300038002e0069004d0000004f004b00300044004d0052000000000000000000000000000000000000000000520044003900380035002d00300030003000300030003000300030002d003000300030003000300030002d00550031002d0030002d004600000000000000000031003200330032003000410030003300310032000000000000000000000000000f690600000000": {
            "data": {
                "footer": b"\x00\x0fi\x06\x00\x00\x00\x00",
                "header": b"\x00\x0fi\x06\x00\x02",
                "text": "D9.00.07.210.iM\x00A9.00.08.308.iM\x00OK0DMR\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00RD985-00000000-000000-U1-0-F\x00\x00\x00\x0012320A0312\x00\x00\x00\x00\x00\x00",
            }
        },
    }
    for hexmsg, expectations in hexmessages.items():
        rcp = RadioControlProtocol.from_bytes(bytes.fromhex(hexmsg))
        prettyprint(rcp)
        assert_expected_attribute_values(rcp, expectations)
