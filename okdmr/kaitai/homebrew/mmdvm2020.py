# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version("0.9"):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )


class Mmdvm2020(KaitaiStruct):
    """MMDVM protocol structure (MMDVMHost/HBlink3/DMRGateway) based on reversing effort"""

    class Timeslots(Enum):
        timeslot_1 = 0
        timeslot_2 = 1

    class CallTypes(Enum):
        group_call = 0
        private_call = 1

    class TalkerAliasTypes(Enum):
        talker_alias_header = 0
        talker_alias_block_1 = 1
        talker_alias_block_2 = 2
        talker_alias_block_3 = 3

    class PositionErrors(Enum):
        less_than_2m = 0
        less_than_20m = 1
        less_than_200m = 2
        less_than_2km = 3
        less_than_20km = 4
        less_than_or_equal_200km = 5
        more_than_200km = 6
        position_error_unknown_or_invalid = 7

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.command_prefix = (self._io.read_bytes(4)).decode("ASCII")
        _on = self.command_prefix
        if _on == "RPTL":
            self.command_data = Mmdvm2020.TypeRepeaterLoginRequest(
                self._io, self, self._root
            )
        elif _on == "DMRG":
            self.command_data = Mmdvm2020.TypeRadioPosition(self._io, self, self._root)
        elif _on == "RPTA":
            self.command_data = Mmdvm2020.TypeMasterRepeaterAck(
                self._io, self, self._root
            )
        elif _on == "RPTK":
            self.command_data = Mmdvm2020.TypeRepeaterLoginResponse(
                self._io, self, self._root
            )
        elif _on == "RPTC":
            self.command_data = Mmdvm2020.TypeRepeaterConfigurationOrClosing(
                self._io, self, self._root
            )
        elif _on == "DMRD":
            self.command_data = Mmdvm2020.TypeDmrData(self._io, self, self._root)
        elif _on == "MSTC":
            self.command_data = Mmdvm2020.TypeMasterClosing(self._io, self, self._root)
        elif _on == "RPTP":
            self.command_data = Mmdvm2020.TypeRepeaterPing(self._io, self, self._root)
        elif _on == "RPTO":
            self.command_data = Mmdvm2020.TypeRepeaterOptions(
                self._io, self, self._root
            )
        elif _on == "MSTP":
            self.command_data = Mmdvm2020.TypeMasterPong(self._io, self, self._root)
        elif _on == "RPTS":
            self.command_data = Mmdvm2020.TypeRepeaterBeacon(self._io, self, self._root)
        elif _on == "MSTN":
            self.command_data = Mmdvm2020.TypeMasterNotAccept(
                self._io, self, self._root
            )
        elif _on == "DMRA":
            self.command_data = Mmdvm2020.TypeTalkerAlias(self._io, self, self._root)

    class TypeMasterPong(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x4F\x4E\x47":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x4F\x4E\x47",
                    self.magic,
                    self._io,
                    "/types/type_master_pong/seq/0",
                )
            self.repeater_id = self._io.read_u4be()

    class TypeRadioPosition(KaitaiStruct):
        """etsi dmr, link control, type flcos::gps_info, specifically gps_info_lc_pdu."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.radio_id = self._io.read_bits_int_be(24)
            self.reserved = self._io.read_bits_int_be(4)
            self.position_error = KaitaiStream.resolve_enum(
                Mmdvm2020.PositionErrors, self._io.read_bits_int_be(3)
            )
            self.longitude = self._io.read_bits_int_be(25)
            self.latitude = self._io.read_bits_int_be(24)

    class TypeTalkerAlias(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.radio_id = self._io.read_bits_int_be(24)
            self._io.align_to_byte()
            self.talker_alias_type = KaitaiStream.resolve_enum(
                Mmdvm2020.TalkerAliasTypes, self._io.read_u1()
            )
            self.talker_alias = (self._io.read_bytes(8)).decode("ASCII")

    class TypeRepeaterConfigurationOrClosing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            _on = self._root.fifth_letter
            if _on == "L":
                self.data = Mmdvm2020.TypeRepeaterClosing(self._io, self, self._root)
            else:
                self.data = Mmdvm2020.TypeRepeaterConfiguration(
                    self._io, self, self._root
                )

    class TypeRepeaterLoginResponse(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.repeater_id = self._io.read_u4be()
            self.sha256 = self._io.read_bytes(32)

    class TypeRepeaterLoginRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.repeater_id = self._io.read_u4be()

    class TypeMasterNotAccept(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\x41\x4B":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x41\x4B",
                    self.magic,
                    self._io,
                    "/types/type_master_not_accept/seq/0",
                )
            self.repeater_id = self._io.read_u4be()

    class TypeUnknown(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown_data = self._io.read_bytes_full()

    class TypeMasterRepeaterAck(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(2)
            if not self.magic == b"\x43\x4B":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x43\x4B",
                    self.magic,
                    self._io,
                    "/types/type_master_repeater_ack/seq/0",
                )
            self.repeater_id_or_challenge = self._io.read_u4be()

    class TypeMasterClosing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(1)
            if not self.magic == b"\x4C":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x4C", self.magic, self._io, "/types/type_master_closing/seq/0"
                )
            self.repeater_id = self._io.read_u4be()

    class TypeDmrData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sequence_no = self._io.read_u1()
            self.source_id = self._io.read_bits_int_be(24)
            self.target_id = self._io.read_bits_int_be(24)
            self._io.align_to_byte()
            self.repeater_id = self._io.read_u4be()
            self.slot_no = KaitaiStream.resolve_enum(
                Mmdvm2020.Timeslots, self._io.read_bits_int_be(1)
            )
            self.call_type = KaitaiStream.resolve_enum(
                Mmdvm2020.CallTypes, self._io.read_bits_int_be(1)
            )
            self.frame_type = self._io.read_bits_int_be(2)
            self.data_type = self._io.read_bits_int_be(4)
            self._io.align_to_byte()
            self.stream_id = self._io.read_u4be()
            self.dmr_data = self._io.read_bytes(33)
            if not (self._io.is_eof()):
                self.bit_error_rate = self._io.read_u1()

            if not (self._io.is_eof()):
                self.rssi = self._io.read_u1()

    class TypeRepeaterBeacon(KaitaiStruct):
        """undefined currently."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

    class TypeRepeaterOptions(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.repeater_id = self._io.read_u4be()
            self.options = (self._io.read_bytes_full()).decode("ASCII")

    class TypeRepeaterClosing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(1)
            if not self.magic == b"\x4C":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x4C", self.magic, self._io, "/types/type_repeater_closing/seq/0"
                )
            self.repeater_id = self._io.read_u4be()

    class TypeRepeaterConfiguration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.repeater_id = self._io.read_u4be()
            self.call_sign = (self._io.read_bytes(8)).decode("ASCII")
            self.rx_freq = (self._io.read_bytes(9)).decode("ASCII")
            self.tx_freq = (self._io.read_bytes(9)).decode("ASCII")
            self.tx_power = (self._io.read_bytes(2)).decode("ASCII")
            self.color_code = (self._io.read_bytes(2)).decode("ASCII")
            self.latitude = (self._io.read_bytes(8)).decode("ASCII")
            self.longitude = (self._io.read_bytes(9)).decode("ASCII")
            self.antenna_height_above_ground = (self._io.read_bytes(3)).decode("ASCII")
            self.location = (self._io.read_bytes(20)).decode("ASCII")
            self.description = (self._io.read_bytes(19)).decode("ASCII")
            self.slots = (self._io.read_bytes(1)).decode("ASCII")
            self.url = (self._io.read_bytes(124)).decode("ASCII")
            self.software_id = (self._io.read_bytes(40)).decode("ASCII")
            self.package_id = (self._io.read_bytes(40)).decode("ASCII")
            self.unparsed_data = (self._io.read_bytes_full()).decode("ASCII")

    class TypeRepeaterPing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x49\x4E\x47":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x49\x4E\x47",
                    self.magic,
                    self._io,
                    "/types/type_repeater_ping/seq/0",
                )
            self.repeater_id = self._io.read_u4be()

    @property
    def fifth_letter(self):
        if hasattr(self, "_m_fifth_letter"):
            return self._m_fifth_letter if hasattr(self, "_m_fifth_letter") else None

        _pos = self._io.pos()
        self._io.seek(4)
        self._m_fifth_letter = (self._io.read_bytes(1)).decode("ASCII")
        self._io.seek(_pos)
        return self._m_fifth_letter if hasattr(self, "_m_fifth_letter") else None
