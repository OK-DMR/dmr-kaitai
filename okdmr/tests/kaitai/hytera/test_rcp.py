from audioop import byteswap
from typing import List

from okdmr.kaitai.hytera.radio_control_protocol import RadioControlProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_rcp():
    # messages must not start with 0x20, the type header is not supported by radio_control_protocol.ksy
    hexmessages: List[str] = [
        # rcp identification request opcode 0x0004
        "040005006400000001",
        # rcp identification response opcode 0x82D4
        "d482ce00000f6906000200440039002e00300030002e00300037002e003200310030002e0069004d000000410039002e00300030002e00300038002e003300300038002e0069004d0000004f004b00300044004d0052000000000000000000000000000000000000000000520044003900380035002d00300030003000300030003000300030002d003000300030003000300030002d00550031002d0030002d004600000000000000000031003200330032003000410030003300310032000000000000000000000000000f690600000000",
    ]
    for hexmsg in hexmessages:
        prettyprint(RadioControlProtocol.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_rcp()
