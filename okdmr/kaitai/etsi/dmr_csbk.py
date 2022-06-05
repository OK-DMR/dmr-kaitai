# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )


class DmrCsbk(KaitaiStruct):
    """TS 102 361-2 V2.4.1 - section 7.1.2 Control Signalling BlocK (CSBK) PDUs"""

    class CsbkoTypes(Enum):
        unit_to_unit_voice_service_request = 4
        unit_to_unit_voice_service_answer_response = 5
        channel_timing = 7
        negative_acknowledge_response = 38
        bs_outbound_activation_csbk_pdu = 56
        preamble = 61

    class CsbkDataOrCsbk(Enum):
        csbk_content_follows_preambles = 0
        data_content_follows_preambles = 1

    class CsbkGroupOrIndividual(Enum):
        target_address_is_an_individual = 0
        target_address_is_a_group = 1

    class AnswerResponse(Enum):
        proceed = 32
        deny = 33

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.last_block = self._io.read_bits_int_be(1) != 0
        self.protect_flag = self._io.read_bits_int_be(1) != 0
        self.csbk_opcode = KaitaiStream.resolve_enum(
            DmrCsbk.CsbkoTypes, self._io.read_bits_int_be(6)
        )
        self.feature_set_id = self._io.read_bits_int_be(8)
        self._io.align_to_byte()
        _on = self.csbk_opcode
        if _on == DmrCsbk.CsbkoTypes.unit_to_unit_voice_service_answer_response:
            self.csbk_data = DmrCsbk.UnitToUnitVoiceAnswerData(
                self._io, self, self._root
            )
        elif _on == DmrCsbk.CsbkoTypes.preamble:
            self.csbk_data = DmrCsbk.PreambleData(self._io, self, self._root)
        elif _on == DmrCsbk.CsbkoTypes.channel_timing:
            self.csbk_data = DmrCsbk.ChannelTimingData(self._io, self, self._root)
        elif _on == DmrCsbk.CsbkoTypes.unit_to_unit_voice_service_request:
            self.csbk_data = DmrCsbk.UnitToUnitVoiceRequestData(
                self._io, self, self._root
            )
        elif _on == DmrCsbk.CsbkoTypes.bs_outbound_activation_csbk_pdu:
            self.csbk_data = DmrCsbk.BsOutboundActivationData(
                self._io, self, self._root
            )
        elif _on == DmrCsbk.CsbkoTypes.negative_acknowledge_response:
            self.csbk_data = DmrCsbk.NegativeAckResponseData(self._io, self, self._root)

    class NegativeAckResponseData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.additional_information_field = self._io.read_bits_int_be(1) != 0
            self.source_type = self._io.read_bits_int_be(1) != 0
            self.service_type = self._io.read_bits_int_be(6)
            self.reason_code = self._io.read_bits_int_be(8)
            self.source_address = self._io.read_bits_int_be(24)
            self.target_address = self._io.read_bits_int_be(24)

    class UnitToUnitVoiceRequestData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.service_options = DmrCsbk.ServiceOptions(self._io, self, self._root)
            self.reserved = self._io.read_bits_int_be(8)
            self.target_address = self._io.read_bits_int_be(24)
            self.source_address = self._io.read_bits_int_be(24)

    class ServiceOptions(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.is_emergency_service = self._io.read_bits_int_be(1) != 0
            self.privacy = self._io.read_bits_int_be(1) != 0
            self.reserved = self._io.read_bits_int_be(2)
            self.is_broadcast_service = self._io.read_bits_int_be(1) != 0
            self.is_open_voice_call_mode = self._io.read_bits_int_be(1) != 0
            self.priority_level = self._io.read_bits_int_be(2)

    class PreambleData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.preamble_data_or_csbk = KaitaiStream.resolve_enum(
                DmrCsbk.CsbkDataOrCsbk, self._io.read_bits_int_be(1)
            )
            self.group_or_individual = KaitaiStream.resolve_enum(
                DmrCsbk.CsbkGroupOrIndividual, self._io.read_bits_int_be(1)
            )
            self.preamble_reserved = self._io.read_bits_int_be(6)
            self.preamble_csbk_blocks_to_follow = self._io.read_bits_int_be(8)
            self.target_address = self._io.read_bits_int_be(24)
            self.source_address = self._io.read_bits_int_be(24)

    class ChannelTimingData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sync_age = self._io.read_bits_int_be(11)
            self.generation = self._io.read_bits_int_be(5)
            self.leader_identifier = self._io.read_bits_int_be(20)
            self.new_leader = self._io.read_bits_int_be(1) != 0
            self.leader_dynamic_identifier = self._io.read_bits_int_be(2)
            self.channel_timing_op1 = self._io.read_bits_int_be(1) != 0
            self.source_identifier = self._io.read_bits_int_be(20)
            self.reserved = self._io.read_bits_int_be(1) != 0
            self.source_dynamic_identifier = self._io.read_bits_int_be(2)
            self.channel_timing_op0 = self._io.read_bits_int_be(1) != 0

    class BsOutboundActivationData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.reserved = self._io.read_bits_int_be(16)
            self.bs_address = self._io.read_bits_int_be(24)
            self.source_address = self._io.read_bits_int_be(24)

    class UnitToUnitVoiceAnswerData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.service_options = DmrCsbk.ServiceOptions(self._io, self, self._root)
            self.answer_response = KaitaiStream.resolve_enum(
                DmrCsbk.AnswerResponse, self._io.read_bits_int_be(8)
            )
            self.target_address = self._io.read_bits_int_be(24)
            self.source_address = self._io.read_bits_int_be(24)
