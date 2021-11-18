from typing import List

from okdmr.kaitai.hytera.hytera_simple_transport_reliability_protocol import (
    HyteraSimpleTransportReliabilityProtocol,
)
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_hstrp():
    hexmessages: List[str] = [
        # heartbeat
        "324200020000",
        # connect
        "32420024000083040001869f040102",
        # ACK
        "324200010003",
        # RCP
        "32420020003c83040001869f0401020245b81000000004000200010010270000640000008303",
        # group text message
        "32420020000383040001869f0401020900b10018000000010000271000000064480065006c006c006f002100b803",
        # RCP
        "32420020003583040001869f0401010245b810000000040002000100204e0000640000004c03",
        # group text message
        "32420020000383040001869f0401010900b1001c0000000200004e2000000064570065006c0063006f006d0065002100a403",
        # text message
        "3242000000010901a10026300000010a0000640a01869f5200520053002000770061006900740020006f00760065007200f403",
        # text message send private ack
        "32420020000183040001869f0401020900a2000d30000001000000640001869f00c803",
        # text message protocol ack
        "32420020000183040001869f0401010900a2000d30000002000000640001869f00c703",
        # repeater broadcast transmit status
        "32420020000783040001869f0401020245b810000000050002000000640000009f8601009403",
        # check request
        "32420000001502e700020009013f03",
        # check reply
        "32420020001b83040001869f04010102e780070000010938ffffff8503"
    ]
    for hexmsg in hexmessages:
        prettyprint(
            HyteraSimpleTransportReliabilityProtocol.from_bytes(bytes.fromhex(hexmsg))
        )


if __name__ == "__main__":
    test_hstrp()
