from okdmr.kaitai.etsi.full_link_control import FullLinkControl
from okdmr.kaitai.tools.prettyprint import prettyprint


def test_group_full_link_control():
    voice_lc_header_hex: str = "000000000009280722504778"
    lc: FullLinkControl = FullLinkControl.from_bytes(bytes.fromhex(voice_lc_header_hex))
    assert isinstance(lc.specific_data, FullLinkControl.GroupVoiceChannelUser)
    assert lc.specific_data.group_address == 9
    assert lc.specific_data.source_address == 2623266
    assert hasattr(lc, "crc_checksum")
    assert not hasattr(lc, "cs5_checksum")
    assert lc.crc_checksum == b"PGx"
    print(prettyprint(lc))


def test_group_embedded_full_link_control():
    embedded_deinterleaved: str = "00000000086520baf888"
    lc: FullLinkControl = FullLinkControl.from_bytes(
        bytes.fromhex(embedded_deinterleaved)
    )
    assert isinstance(lc.specific_data, FullLinkControl.GroupVoiceChannelUser)
    assert lc.full_link_control_opcode == FullLinkControl.Flcos.group_voice
    assert lc.feature_set_id == FullLinkControl.FeatureSetIds.standardized_ts_102_361_2
    assert lc.specific_data.group_address == 2149
    assert lc.specific_data.source_address == 2145016
    assert lc.specific_data.service_options == 0
    assert not hasattr(lc, "crc_checksum")
    assert hasattr(lc, "cs5_checksum")
