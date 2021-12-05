import unittest

from typing import List

from okdmr.kaitai.hytera.location_protocol import LocationProtocol
from okdmr.tests.kaitai.tests_utils import prettyprint


class TestLocationProtocl(unittest.TestCase):
    def test_lp(self):
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
        ]
        for hexmsg in hexmessages:
            print(hexmsg)
            message = LocationProtocol.from_bytes(bytes.fromhex(hexmsg))
            prettyprint(message)

    def test_parse_standard_answer(self):
        hex_location_germany = "a0020032200000010a03640e0000413136323232333331313031384e343733362e363937374530303733392e32363830302e303030358903"
        message = LocationProtocol.from_bytes(bytes.fromhex(hex_location_germany))

        # Assert properties from LocationProtocol
        self.assertEqual(
            message.opcode_header, LocationProtocol.LpSpecificTypes.standard_answer
        )
        self.assertEqual(
            message.opcode,
            LocationProtocol.LpGeneralTypes.standard_location_immediate_service,
        )

        # Assert properties in Standard Answer
        self.assertEqual(message.data.result, LocationProtocol.ResultCodes.ok)
        ## TODO: Test radio id/ip, I think there we can decode directly to the correct id (should be 222222)
        self.assertEqual(message.data.radio_ip.subnet, 10)

        # Assert properties in gps payload
        gps_msg = message.data.gpsdata
        self.assertEqual(gps_msg.gps_status.decode("ascii"), "A")
        self.assertEqual(gps_msg.gps_date.decode("ascii"), "311018")
        self.assertEqual(gps_msg.gps_time.decode("ascii"), "162223")
        self.assertEqual(gps_msg.east_west.decode("ascii"), "E")
        self.assertEqual(gps_msg.longitude.decode("ascii"), "00739.2680")
        self.assertEqual(gps_msg.north_south.decode("ascii"), "N")
        self.assertEqual(gps_msg.latitude.decode("ascii"), "4736.6977")
        self.assertEqual(gps_msg.direction.decode("ascii"), "005")
        self.assertEqual(gps_msg.speed.decode("ascii"), "0.0")

        # Payload instances
        self.assertTrue(gps_msg.gps_available)


if __name__ == "__main__":
    unittest.main()
