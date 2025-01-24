# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )


class Homebrew2015(KaitaiStruct):
    """Homebrew DMR protocol, based on PDF (DL5DI, G4KLX, DG1HT 2015) specification"""

    class Timeslots(Enum):
        timeslot_1 = 0
        timeslot_2 = 1

    class CallTypes(Enum):
        group_call = 0
        private_call = 1

    class FrameTypes(Enum):
        voice_data = 0
        voice_sync = 1
        data_or_data_sync = 2
        unused = 3

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.command_prefix = (self._io.read_bytes(4)).decode("UTF-8")
        _on = self.command_prefix
        if _on == "RPTL":
            self.command_data = Homebrew2015.TypeRepeaterLoginRequest(
                self._io, self, self._root
            )
        elif _on == "MSTA":
            self.command_data = Homebrew2015.TypeMasterRepeaterAck(
                self._io, self, self._root
            )
        elif _on == "RPTK":
            self.command_data = Homebrew2015.TypeRepeaterLoginResponse(
                self._io, self, self._root
            )
        elif _on == "RPTC":
            self.command_data = Homebrew2015.TypeRepeaterConfigurationOrClosing(
                self._io, self, self._root
            )
        elif _on == "DMRD":
            self.command_data = Homebrew2015.TypeDmrData(self._io, self, self._root)
        elif _on == "MSTC":
            self.command_data = Homebrew2015.TypeMasterClosing(
                self._io, self, self._root
            )
        elif _on == "RPTP":
            self.command_data = Homebrew2015.TypeRepeaterPong(
                self._io, self, self._root
            )
        elif _on == "MSTP":
            self.command_data = Homebrew2015.TypeMasterPing(self._io, self, self._root)
        elif _on == "MSTN":
            self.command_data = Homebrew2015.TypeMasterNotAccept(
                self._io, self, self._root
            )

    class TypeMasterPing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x49\x4e\x47":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x49\x4e\x47",
                    self.magic,
                    self._io,
                    "/types/type_master_ping/seq/0",
                )
            self.repeater_id = self._io.read_u4be()

    class TypeRepeaterPong(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(3)
            if not self.magic == b"\x4f\x4e\x47":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x4f\x4e\x47",
                    self.magic,
                    self._io,
                    "/types/type_repeater_pong/seq/0",
                )
            self.repeater_id = self._io.read_u4be()

    class TypeRepeaterConfigurationOrClosing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            _on = self._root.fifth_letter
            if _on == "L":
                self.data = Homebrew2015.TypeRepeaterClosing(self._io, self, self._root)
            else:
                self.data = Homebrew2015.TypeRepeaterConfiguration(
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
            if not self.magic == b"\x41\x4b":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x41\x4b",
                    self.magic,
                    self._io,
                    "/types/type_master_not_accept/seq/0",
                )
            self.repeater_id = self._io.read_u4be()

    class TypeMasterRepeaterAck(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magictype_master_repeater_ack = self._io.read_bytes(2)
            if not self.magictype_master_repeater_ack == b"\x43\x4b":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x43\x4b",
                    self.magictype_master_repeater_ack,
                    self._io,
                    "/types/type_master_repeater_ack/seq/0",
                )
            self.repeater_id = self._io.read_u4be()
            if not (self._io.is_eof()):
                self.random_number = self._io.read_u4be()

    class TypeMasterClosing(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.magic = self._io.read_bytes(1)
            if not self.magic == b"\x4c":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x4c", self.magic, self._io, "/types/type_master_closing/seq/0"
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
                Homebrew2015.Timeslots, self._io.read_bits_int_be(1)
            )
            self.call_type = KaitaiStream.resolve_enum(
                Homebrew2015.CallTypes, self._io.read_bits_int_be(1)
            )
            self.frame_type = KaitaiStream.resolve_enum(
                Homebrew2015.FrameTypes, self._io.read_bits_int_be(2)
            )
            self.data_type = self._io.read_bits_int_be(4)
            self._io.align_to_byte()
            self.stream_id = self._io.read_u4be()
            self.dmr_data = self._io.read_bytes(33)
            if not (self._io.is_eof()):
                self.bit_error_rate = self._io.read_u1()

            if not (self._io.is_eof()):
                self.rssi = self._io.read_u1()

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
            if not self.magic == b"\x4c":
                raise kaitaistruct.ValidationNotEqualError(
                    b"\x4c", self.magic, self._io, "/types/type_repeater_closing/seq/0"
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
            self.description = (self._io.read_bytes(20)).decode("ASCII")
            self.url = (self._io.read_bytes(124)).decode("ASCII")
            self.software_id = (self._io.read_bytes(40)).decode("ASCII")
            self.package_id = (self._io.read_bytes(40)).decode("ASCII")
            self.unparsed_data = (self._io.read_bytes_full()).decode("ASCII")

    @property
    def fifth_letter(self):
        if hasattr(self, "_m_fifth_letter"):
            return self._m_fifth_letter

        _pos = self._io.pos()
        self._io.seek(4)
        self._m_fifth_letter = (self._io.read_bytes(1)).decode("ASCII")
        self._io.seek(_pos)
        return getattr(self, "_m_fifth_letter", None)
