from typing import List

from okdmr.kaitai.hytera.ip_site_connect_protocol import IpSiteConnectProtocol
from okdmr.kaitai.tools.prettyprint import prettyprint


def test_ipsc():
    hexmessages: List[str] = [
        # wakeup
        "5a5a5a5a0000000042000501020000002222dddd555500004000000000000000000000000000020002000000000000000000000000000000b2dd503250380c00000014000000ff01",
        # data transmission ipsc sync
        "5a5a5a5a0000000042000501020000002222eeee555533334000bd0000008000150000000800fd00230038003b0038003b00b41200447eb7ffffef0844400000fd0800003b382300",
        # voice transmission ipsc sync
        "5a5a5a5a0000000042000501020000002222eeee555511114028000000000000000000006f00230038003b00342a2c10942a2c10f42a2c10833f0017e60a01006f0000003b382300",
    ]
    for hexmsg in hexmessages:
        ipsc_msg: IpSiteConnectProtocol = IpSiteConnectProtocol.from_bytes(
            bytes.fromhex(hexmsg)
        )
        prettyprint(ipsc_msg)
        print(ipsc_msg.ipsc_payload.hex())
