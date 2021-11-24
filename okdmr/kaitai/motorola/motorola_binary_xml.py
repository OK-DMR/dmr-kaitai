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

    class LrrpElements(Enum):
        request_id_22_opaque = 34
        request_id_23_opaque_1byte = 35
        request_id_24_cdt_reference = 36

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.documents = []
        i = 0
        while True:
            _ = MotorolaBinaryXml.MbxmlDocument(self._io, self, self._root)
            self.documents.append(_)
            if not (self._io.is_eof()):
                break
            i += 1

    class LrrpImmediateRequestNcdt(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.elements = MotorolaBinaryXml.LrrpElement(self._io, self, self._root)

    class Opaque3byteValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_bytes(3)

    class LrrpElement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.lrrp_element_type = KaitaiStream.resolve_enum(
                MotorolaBinaryXml.LrrpElements, self._io.read_u1()
            )
            _on = self.lrrp_element_type
            if _on == MotorolaBinaryXml.LrrpElements.request_id_22_opaque:
                self.lrrp_element_data = MotorolaBinaryXml.OpaqueElementValue(
                    self._io, self, self._root
                )
            elif _on == MotorolaBinaryXml.LrrpElements.request_id_23_opaque_1byte:
                self.lrrp_element_data = MotorolaBinaryXml.Opaque1byteValue(
                    self._io, self, self._root
                )
            elif _on == MotorolaBinaryXml.LrrpElements.request_id_24_cdt_reference:
                self.lrrp_element_data = MotorolaBinaryXml.ConstantDataTableReference(
                    self._io, self, self._root
                )

    class Sfloatvar(KaitaiStruct):
        """Variable length signed float, first sintvar (signed integer part) then uintvar (unsigned fraction part)"""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sint_payload = MotorolaBinaryXml.Sintvar(self._io, self, self._root)
            self.fraction_payload = MotorolaBinaryXml.Uintvar(
                self._io, self, self._root
            )

    class Opaque5byteValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_bytes(5)

    class Opaque1byteValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_bytes(1)

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

    class ConstantDataTableReference(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.byte_offset_from_cdt_start = MotorolaBinaryXml.Uintvar(
                self._io, self, self._root
            )

    class MbxmlDocument(KaitaiStruct):
        """MBXML payload can contain multiple documents concatenated"""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.document_id = KaitaiStream.resolve_enum(
                MotorolaBinaryXml.Docids, self._io.read_u1()
            )
            self.num_document_bytes = MotorolaBinaryXml.Uintvar(
                self._io, self, self._root
            )
            _on = self.document_id
            if _on == MotorolaBinaryXml.Docids.lrrp_immediate_request_ncdt:
                self.document_data = MotorolaBinaryXml.LrrpImmediateRequestNcdt(
                    self._io, self, self._root
                )

    class OpaqueElementValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_value = self._io.read_u1()
            self.value = self._io.read_bytes(self.len_value)

    class Opaque2byteValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_bytes(2)

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

    class Opaque4byteValue(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_bytes(4)
