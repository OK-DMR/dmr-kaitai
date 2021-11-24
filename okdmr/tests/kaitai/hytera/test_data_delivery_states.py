from typing import List

from okdmr.kaitai.hytera.data_delivery_states import DataDeliveryStates
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_dds():
    hexmessages: List[str] = [
        # Failed state?
        "14000800070003640ea001000d03",
    ]
    for hexmsg in hexmessages:
        prettyprint(DataDeliveryStates.from_bytes(bytes.fromhex(hexmsg)))


if __name__ == "__main__":
    test_dds()
