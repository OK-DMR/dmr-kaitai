from typing import List

from okdmr.kaitai.hytera.hytera_radio_network_protocol import HyteraRadioNetworkProtocol
from okdmr.kaitai.tools.prettyprint import prettyprint


def test_hrnp():
    hexmessages: List[str] = [
        # hrnp connect
        "7e0400fe20100000000c60e1",
        "7e0300fe20100000000c60e2",
        # data (hdap inside)
        "7e0400002010000100189b6002040005006400000001c403",
        # accept
        "7e0400fd10200000000c70d2",
        # RCP data inside
        "7e030000201000000018fefe02c910050002000101014f03"
        "7e040000102000010019d6240204800600000f690600012903",
        "7e0400001020000300e1c65702d482ce00000f6906000200440039002e00300030002e00300037002e003200310030002e0069004d000000410039002e00300030002e00300038002e003300300038002e0069004d0000004f004b00300044004d0052000000000000000000000000000000000000000000520044003900380035002d00300030003000300030003000300030002d003000300030003000300030002d00550031002d0030002d004600000000000000000031003200330032003000410030003300310032000000000000000000000000000f6906000000001b03",
        "7E04000020100000001873890241080500006F0000007503",
    ]
    for hexmsg in hexmessages:
        prettyprint(HyteraRadioNetworkProtocol.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_hrnp()
