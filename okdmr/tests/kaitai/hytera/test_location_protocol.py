from typing import List, Dict

from okdmr.kaitai.hytera.gpsdata import Gpsdata
from okdmr.kaitai.hytera.location_protocol import LocationProtocol
from okdmr.kaitai.tools.prettyprint import prettyprint


def test_lp():
    hexmessages: List[str] = [
        # location protocol
        "a0030034000000000a2338630000413131323534303237303932314e353030332e383734364530313432362e35313932302e32323533ff1cae03",
        "A0010009200000030A03640E01E503",
        "a0020032200000030a03640e0000413136323235313331313031384e343733362e363937354530303733392e32363830302e303030358803",
        "a0010009200000010a03640e01e703",
        "a0020032200000010a03640e0000413136323232333331313031384e343733362e363937374530303733392e32363830302e303030358903",
        "a0010009200000020a03640e01e603",
        # Condition report, no data
        "d0010039200000020a03640e04000003e830303030303030303030303030303030303030303030303030303030303030303031303030303030303832304d03",
        # Received from repeater
        "d0040034000015c80a0000030000413138343033303036313232314e343732342e303135384530303733312e31303733302e30323037ffc66303",
    ]
    for hexmsg in hexmessages:
        print(hexmsg)
        message = LocationProtocol.from_bytes(bytes.fromhex(hexmsg))
        prettyprint(message)


def test_parse_standard_answer():
    hex_location_germany = "a0020032200000010a03640e0000413136323232333331313031384e343733362e363937374530303733392e32363830302e303030358903"
    message = LocationProtocol.from_bytes(bytes.fromhex(hex_location_germany))

    # properties from LocationProtocol
    assert message.opcode_header == LocationProtocol.LpSpecificTypes.standard_answer
    assert (
        message.opcode
        == LocationProtocol.LpGeneralTypes.standard_location_immediate_service
    )

    # properties in Standard Answer
    assert message.data.result == LocationProtocol.ResultCodes.ok
    ## TODO: Test radio id/ip, I think there we can decode directly to the correct id (should be 222222)
    assert message.data.radio_ip.subnet == 10

    # properties in gps payload
    gps_msg = message.data.gpsdata

    values: Dict[str, str] = {
        "gps_status": "A",
        "gps_date": "311018",
        "gps_time": "162223",
        "east_west": "E",
        "longitude": "00739.2680",
        "north_south": "N",
        "latitude": "4736.6977",
        "direction": "005",
        "speed": "0.0",
    }
    assert_gps_data(gps_msg, values)
    # Payload instances
    assert gps_msg.gps_available


def test_parse_condition_report_rssi():
    hex_location_switzerland = "d0040034000015c80a0000030000413138343033303036313232314e343732342e303135384530303733312e31303733302e30323037ffc66303"
    message = LocationProtocol.from_bytes(bytes.fromhex(hex_location_switzerland))

    # properties from LocationProtocol
    assert (
        message.opcode_header
        == LocationProtocol.LpSpecificTypes.condition_report_with_rssi
    )
    assert (
        message.opcode
        == LocationProtocol.LpGeneralTypes.condition_triggered_reporting_service
    )

    # properties in Condition Answer
    assert message.data.result == LocationProtocol.ResultCodes.ok
    assert message.data.radio_ip.subnet == 10

    # properties in gps payload
    gps_msg = message.data.gpsdata

    values: Dict[str, str] = {
        "gps_status": "A",
        "gps_date": "061221",
        "gps_time": "184030",
        "east_west": "E",
        "longitude": "00731.1073",
        "north_south": "N",
        "latitude": "4724.0158",
        "direction": "207",
        "speed": "0.0",
    }
    assert_gps_data(gps_msg, values)

    # Payload instances
    assert gps_msg.gps_available


def assert_gps_data(data: Gpsdata, values: Dict[str, str]):
    for prop, val in values.items():
        assert (
            getattr(data, prop).decode("ascii") == val
        ), "Gps data does not match on property %s: %s should be %s" % (
            prop,
            getattr(data, prop).decode("ascii"),
            val,
        )


if __name__ == "__main__":
    test_lp()
    test_parse_standard_answer()
    test_parse_condition_report_rssi()
