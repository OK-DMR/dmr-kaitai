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


class TextMessageProtocol(KaitaiStruct):
    class TmsServiceCapability(Enum):
        limited_capability = 0
        internal_capability = 1
        external_capability = 2
        full_capability = 3

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.message_size = self._io.read_u2be()
        self.message_header = TextMessageProtocol.MessageHeaderBits(
            self._io, self, self._root
        )
        self.len_address = self._io.read_u1()
        if self.len_address > 0:
            self.address = self._io.read_bytes(self.len_address)

        _on = self.custom_pdu_type
        if _on == 48:
            self.pdu_content = TextMessageProtocol.TmsServiceAvailability(
                self._io, self, self._root
            )
        elif _on == 31:
            self.pdu_content = TextMessageProtocol.TmsAcknowledgement(
                self._io, self, self._root
            )
        elif _on == 0:
            self.pdu_content = TextMessageProtocol.TextMessage(
                self._io, self, self._root
            )
        elif _on == 32:
            self.pdu_content = TextMessageProtocol.TextMessage(
                self._io, self, self._root
            )
        self.unparsed_data = self._io.read_bytes_full()

    class TextMessage(KaitaiStruct):
        """This message is used to send basic text messages."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._root.message_header.extension_bit:
                self.text_message_header_sequence_and_encoding = (
                    TextMessageProtocol.TextMessageHeaderSequenceAndEncoding(
                        self._io, self, self._root
                    )
                )

            self.text_message = (self._io.read_bytes_full()).decode(u"utf-16-le")

    class TmsServiceAvailability(KaitaiStruct):
        """This message is used to announce Text Messaging Service availability on the system by the TMS Server."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._root.message_header.extension_bit:
                self.header = TextMessageProtocol.TmsServiceAvailabilityHeader(
                    self._io, self, self._root
                )

    class TextMessageHeaderSequenceAndEncoding(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.has_encoding_header = self._io.read_bits_int_be(1) != 0
            self.reserved_1 = self._io.read_bits_int_be(2)
            self.sequence_number_lsb_bits = self._io.read_bits_int_be(5)
            if self.has_encoding_header:
                self.header_encoding_extension = self._io.read_bits_int_be(1) != 0

            if self.has_encoding_header:
                self.sequence_number_msb_bits = self._io.read_bits_int_be(2)

            self.encoding = self._io.read_bits_int_be(5)

        @property
        def sequence_number(self):
            if hasattr(self, "_m_sequence_number"):
                return (
                    self._m_sequence_number
                    if hasattr(self, "_m_sequence_number")
                    else None
                )

            self._m_sequence_number = (
                self.sequence_number_msb_bits << 4
            ) + self.sequence_number_lsb_bits
            return (
                self._m_sequence_number if hasattr(self, "_m_sequence_number") else None
            )

    class MessageHeaderBits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extension_bit = self._io.read_bits_int_be(1) != 0
            self.acknowledgement_required = self._io.read_bits_int_be(1) != 0
            self.reserved = self._io.read_bits_int_be(1) != 0
            self.control_user_bit = self._io.read_bits_int_be(1) != 0
            self.pdu_type = self._io.read_bits_int_be(4)

    class TmsAcknowledgement(KaitaiStruct):
        """This message is used to positively acknowledge a text message."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._root.message_header.extension_bit:
                self.tms_acknowledgement_header_sequence_number = (
                    TextMessageProtocol.TmsAcknowledgementHeaderSequenceNumber(
                        self._io, self, self._root
                    )
                )

    class TmsAcknowledgementHeaderSequenceNumber(KaitaiStruct):
        """contains optionally both header bytes (lsb and msb if overflow is needed/occurred)."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.has_msb_header = self._io.read_bits_int_be(1) != 0
            self.header_lsb_reserved = self._io.read_bits_int_be(2)
            self.header_lsb_bits = self._io.read_bits_int_be(5)
            if self.has_msb_header:
                self.header_msb_extension = self._io.read_bits_int_be(1) != 0

            if self.has_msb_header:
                self.header_msb_bits = self._io.read_bits_int_be(2)

            if self.has_msb_header:
                self.header_msb_reserved = self._io.read_bits_int_be(5)

        @property
        def sequence_number(self):
            if hasattr(self, "_m_sequence_number"):
                return (
                    self._m_sequence_number
                    if hasattr(self, "_m_sequence_number")
                    else None
                )

            self._m_sequence_number = (self.header_msb_bits << 4) + self.header_lsb_bits
            return (
                self._m_sequence_number if hasattr(self, "_m_sequence_number") else None
            )

    class TmsServiceAvailabilityAcknowledgement(KaitaiStruct):
        """This message is used to positively acknowledge a service availability message (no headers or payload)
        Same as tms_acknowledgement, only in ack to tms_service_availability announcement no "sequence number" is expected
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

    class TmsServiceAvailabilityHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extension_bit = self._io.read_bits_int_be(1) != 0
            self.reserved = self._io.read_bits_int_be(4)
            self.device = KaitaiStream.resolve_enum(
                TextMessageProtocol.TmsServiceCapability, self._io.read_bits_int_be(3)
            )

    @property
    def custom_pdu_type(self):
        """special enumerable pdu type (ack-type + control-or-user + pdu-type-id)."""
        if hasattr(self, "_m_custom_pdu_type"):
            return (
                self._m_custom_pdu_type if hasattr(self, "_m_custom_pdu_type") else None
            )

        self._m_custom_pdu_type = (
            (int(self._root.message_header.acknowledgement_required) << 5)
            + (int(self._root.message_header.control_user_bit) << 4)
        ) + self._root.message_header.pdu_type
        return self._m_custom_pdu_type if hasattr(self, "_m_custom_pdu_type") else None
