from typing import List

from okdmr.kaitai.hytera.data_delivery_states import DataDeliveryStates
from okdmr.kaitai.hytera.text_message_protocol import TextMessageProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_lp():
    hexmessages: List[str] = [
        # Failed state?
        "14000800070003640ea001000d03",
    ]
    for hexmsg in hexmessages:
        prettyprint(DataDeliveryStates.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_lp()
