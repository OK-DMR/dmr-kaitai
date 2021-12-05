from okdmr.kaitai.etsi.full_link_control import FullLinkControl
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_group_full_link_control():
    voice_lc_header_hex: str = "000000000009280722504778"
    lc: FullLinkControl = FullLinkControl.from_bytes(bytes.fromhex(voice_lc_header_hex))
    assert isinstance(lc.specific_data, FullLinkControl.GroupVoiceChannelUser)
    assert lc.specific_data.group_address == 9
    assert lc.specific_data.source_address == 2623266
    assert lc.crc_checksum == b"PGx"
