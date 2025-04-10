# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )

from okdmr.kaitai.hytera import data_transmit_protocol
from okdmr.kaitai.hytera import radio_control_protocol
from okdmr.kaitai.hytera import telemetry_protocol
from okdmr.kaitai.hytera import location_protocol
from okdmr.kaitai.hytera import text_message_protocol
from okdmr.kaitai.hytera import data_delivery_states
from okdmr.kaitai.hytera import radio_registration_service


class HyteraDmrApplicationProtocol(KaitaiStruct):

    class MessageHeaderTypes(Enum):
        radio_control_protocol = 2
        location_protocol = 8
        text_message_protocol = 9
        radio_registration = 17
        telemetry_protocol = 18
        data_transmit_protocol = 19
        data_delivery_states = 20

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.is_reliable_message = self._io.read_bits_int_be(1) != 0
        self.message_header = KaitaiStream.resolve_enum(
            HyteraDmrApplicationProtocol.MessageHeaderTypes,
            self._io.read_bits_int_be(7),
        )
        self._io.align_to_byte()
        _on = self.message_header
        if _on == HyteraDmrApplicationProtocol.MessageHeaderTypes.radio_registration:
            self.data = radio_registration_service.RadioRegistrationService(self._io)
        elif _on == HyteraDmrApplicationProtocol.MessageHeaderTypes.telemetry_protocol:
            self.data = telemetry_protocol.TelemetryProtocol(self._io)
        elif (
            _on
            == HyteraDmrApplicationProtocol.MessageHeaderTypes.radio_control_protocol
        ):
            self.data = radio_control_protocol.RadioControlProtocol(self._io)
        elif (
            _on == HyteraDmrApplicationProtocol.MessageHeaderTypes.text_message_protocol
        ):
            self.data = text_message_protocol.TextMessageProtocol(self._io)
        elif (
            _on == HyteraDmrApplicationProtocol.MessageHeaderTypes.data_delivery_states
        ):
            self.data = data_delivery_states.DataDeliveryStates(self._io)
        elif _on == HyteraDmrApplicationProtocol.MessageHeaderTypes.location_protocol:
            self.data = location_protocol.LocationProtocol(self._io)
        elif (
            _on
            == HyteraDmrApplicationProtocol.MessageHeaderTypes.data_transmit_protocol
        ):
            self.data = data_transmit_protocol.DataTransmitProtocol(self._io)
        self.checksum = self._io.read_u1()
        self.message_footer = self._io.read_bytes(1)
        if not self.message_footer == b"\x03":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x03", self.message_footer, self._io, "/seq/4"
            )

    class UndefinedProtocol(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes_full()
