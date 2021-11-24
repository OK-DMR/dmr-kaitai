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


class MotorolaBinaryXml(KaitaiStruct):
    """Motorola Binary XML parsing, contains and references LRRP (Location Request Response Protocol)
    and ARRP (Accessories Request Response Protocol), xml documents encoded in binary form
    """

    class Docids(Enum):
        lrrp_immediate_request = 4
        lrrp_immediate_request_ncdt = 5
        lrrp_immediate_response = 6
        lrrp_immediate_response_ncdt = 7

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.document_id = KaitaiStream.resolve_enum(
            MotorolaBinaryXml.Docids, self._io.read_u1()
        )
        self.num_document_bytes = MotorolaBinaryXml.Uintvar(self._io, self, self._root)

    class Uintvar(KaitaiStruct):
        """Variable length unsigned integer, first bit is "continue flag", 7 bits are payload
        maximum size is 2^32 - 1, ie. max size of uintvar is 32 bits
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.payload = []
            i = 0
            while True:
                _ = self._io.read_u1()
                self.payload.append(_)
                if ((_ & 128) == 0) or (self._io.is_eof()):
                    break
                i += 1

    class Sintvar(KaitaiStruct):
        """Variable length signed integer, first bit is "continue flag", 7 bits are payload
        (first bit of first payload is sign bit)
        maximum size is 2^32 - 1, ie. max size of sintvar is 32 bits
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.payload = []
            i = 0
            while True:
                _ = self._io.read_u1()
                self.payload.append(_)
                if ((_ & 128) == 0) or (self._io.is_eof()):
                    break
                i += 1

    class Ufloatvar(KaitaiStruct):
        """Variable length unsigned float, two consecutive uintvars, first represents integer part,
        second fraction part of float
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uint_payload = MotorolaBinaryXml.Uintvar(self._io, self, self._root)
            self.fraction_payload = MotorolaBinaryXml.Uintvar(
                self._io, self, self._root
            )
