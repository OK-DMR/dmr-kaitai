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


class AutomaticRegistrationService(KaitaiStruct):
    class RegistrationEvents(Enum):
        initial_event = 1
        refresh_event = 2

    class FailureReasons(Enum):
        device_not_authorized = 0

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.message_size = self._io.read_u2le()
        self.message_header = AutomaticRegistrationService.MessageHeaderBits(
            self._io, self, self._root
        )
        _on = self.message_header.pdu_type
        if _on == 0:
            self.pdu_content = AutomaticRegistrationService.DeviceRegistrationMessage(
                self._io, self, self._root
            )
        elif _on == 1:
            self.pdu_content = AutomaticRegistrationService.DeviceDeregistrationMessage(
                self._io, self, self._root
            )
        elif _on == 4:
            self.pdu_content = AutomaticRegistrationService.ArsQueryMessage(
                self._io, self, self._root
            )
        elif _on == 15:
            self.pdu_content = AutomaticRegistrationService.AcknowledgementMessage(
                self._io, self, self._root
            )
        self.unparsed_data = self._io.read_bytes_full()

    class AcknowledgementMessage(KaitaiStruct):
        """sent by ARS service to device as a response to device_registration_message
        sent by subscriber as a response to ars_query_message
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if (self._root.message_header.extension_bit) and (
                self._root.message_header.acknowledgement_bit
            ):
                self.device_registration_acknowledgement_header = AutomaticRegistrationService.DeviceRegistrationAcknowledgementHeader(
                    self._io, self, self._root
                )

            if (self._root.message_header.extension_bit) and (
                not (self._root.message_header.acknowledgement_bit)
            ):
                self.device_registration_acknowledgement_failure_reason = AutomaticRegistrationService.DeviceRegistrationAcknowledgementFailureReason(
                    self._io, self, self._root
                )

    class DeviceRegistrationMessageHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extension_bit = self._io.read_bits_int_be(1) != 0
            self.event = KaitaiStream.resolve_enum(
                AutomaticRegistrationService.RegistrationEvents,
                self._io.read_bits_int_be(2),
            )
            self.encoding = self._io.read_bits_int_be(5)

    class MessageHeaderBits(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extension_bit = self._io.read_bits_int_be(1) != 0
            self.acknowledgement_bit = self._io.read_bits_int_be(1) != 0
            self.priority = self._io.read_bits_int_be(1) != 0
            self.control_user_bit = self._io.read_bits_int_be(1) != 0
            self.pdu_type = self._io.read_bits_int_be(4)

    class DeviceDeregistrationMessage(KaitaiStruct):
        """sent by device in case of deregistration, does not require ACK response."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

    class DeviceRegistrationAcknowledgementFailureReason(KaitaiStruct):
        """part of failure/unsuccessfull ACK response."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extension_bit = self._io.read_bits_int_be(1) != 0
            self.failure_reason = KaitaiStream.resolve_enum(
                AutomaticRegistrationService.FailureReasons,
                self._io.read_bits_int_be(7),
            )

    class DeviceRegistrationMessage(KaitaiStruct):
        """sent by device to ARS service."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._root.message_header.extension_bit:
                self.device_registration_message_header = (
                    AutomaticRegistrationService.DeviceRegistrationMessageHeader(
                        self._io, self, self._root
                    )
                )

            self.len_device_identifier = self._io.read_u1()
            if self.len_device_identifier > 0:
                self.device_identifier = self._io.read_bytes(self.len_device_identifier)

            self.len_user_identifier = self._io.read_u1()
            if self.len_user_identifier > 0:
                self.user_identifier = self._io.read_bytes(self.len_user_identifier)

            self.len_password = self._io.read_u1()
            if self.len_password > 0:
                self.password = self._io.read_bytes(self.len_password)

    class ArsQueryMessage(KaitaiStruct):
        """sent by service to device/subscriber to check if the user is registered with ARS."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

    class DeviceRegistrationAcknowledgementHeader(KaitaiStruct):
        """part of successfull ACK response."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.extension_bit = self._io.read_bits_int_be(1) != 0
            self.refresh_time = self._io.read_bits_int_be(7)
