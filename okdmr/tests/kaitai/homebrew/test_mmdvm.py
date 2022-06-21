from typing import List
from unittest import TestCase

from okdmr.kaitai.homebrew.mmdvm2020 import Mmdvm2020


class TestMmdvm(TestCase):
    def test_packets(self):
        with self.assertRaises(UnicodeDecodeError):
            # malformed DMRA packet that should not pass validation
            Mmdvm2020.from_bytes(
                bytes.fromhex("444d524100066b0c2337fa00cc004f004b0034")
            )
