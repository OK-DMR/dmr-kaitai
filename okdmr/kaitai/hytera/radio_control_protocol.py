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


class RadioControlProtocol(KaitaiStruct):
    class ServiceTypes(Enum):
        radio_identification_request = 4
        button_and_keyboard_operation_request = 65
        internal_external_mic_enable_disable_request = 67
        internal_external_mic_gain_check_control_request = 68
        internal_external_speaker_enable_disable_request = 69
        volume_check_control_request = 70
        radio_configure_over_air_request = 192
        zone_and_channel_operation_request = 196
        radio_connect_login_request = 202
        radio_connect_logout_request = 203
        channel_status_or_param_check_request = 231
        function_status_check_request = 237
        function_enable_disable_request = 238
        channel_alias_request = 305
        radio_message_query_request = 513
        channel_number_of_zone_request = 1104
        update_authentication_key_request = 1105
        radio_id_and_radio_ip_query_request = 1106
        radio_check = 2099
        remote_monitor = 2100
        allert_call = 2101
        call_request = 2113
        remove_radio_request = 2114
        delete_subject_line_message_request = 2118
        radio_disable = 2121
        radio_enable = 2122
        radio_status_configure_request = 4295
        broadcast_status_configuration_request = 4297
        button_and_keyboard_operation_reply = 32833
        internal_external_mic_enable_disable_reply = 32835
        internal_external_mic_gain_check_control_reply = 32836
        internal_external_speaker_enable_disable_reply = 32837
        volume_check_control_reply = 32838
        radio_configure_over_air_reply = 32960
        zone_and_channel_operation_reply = 32964
        radio_status_configure_reply = 32967
        broadcast_status_configuration_reply = 32969
        radio_connect_login_reply = 32970
        radio_connect_logout_reply = 32971
        channel_status_or_param_check_reply = 32999
        function_status_check_reply = 33005
        function_enable_disable_reply = 33006
        channel_alias_reply = 33073
        radio_message_query_reply = 33281
        radio_identification_reply = 33492
        channel_number_of_zone_reply = 33872
        update_authentication_key_reply = 33873
        radio_id_and_radio_ip_query_reply = 33874
        radio_check_ack = 34867
        remote_monitor_ack = 34868
        alert_call_ack = 34869
        call_reply = 34881
        remove_radio_reply = 34882
        delete_subject_line_message_reply = 34886
        radio_disable_ack = 34889
        radio_enable_ack = 34890
        radio_status_report = 45256
        broadcast_transmit_status = 47171
        repeater_broadcast_transmit_status = 47173
        broadcast_receive_status = 47428

    class CallTypes(Enum):
        private_call = 0
        group_call = 1
        all_call = 2
        emergency_group_call = 3
        remote_monitor_call = 4
        reserved = 5
        priority_private_call = 6
        priority_group_call = 7
        priority_all_call = 8

    class ReplyResults(Enum):
        success = 0
        failure = 1

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.service_type = KaitaiStream.resolve_enum(
            RadioControlProtocol.ServiceTypes, self._io.read_u2le()
        )
        self.message_length = self._io.read_u2le()
        _on = self.service_type
        if _on == RadioControlProtocol.ServiceTypes.call_reply:
            self.data = RadioControlProtocol.CallReply(self._io, self, self._root)
        elif _on == RadioControlProtocol.ServiceTypes.radio_identification_reply:
            self.data = RadioControlProtocol.RadioIdentificationReply(
                self._io, self, self._root
            )
        elif (
            _on
            == RadioControlProtocol.ServiceTypes.broadcast_status_configuration_request
        ):
            self.data = RadioControlProtocol.BroadcastStatusConfigurationRequest(
                self._io, self, self._root
            )
        elif _on == RadioControlProtocol.ServiceTypes.call_request:
            self.data = RadioControlProtocol.CallRequest(self._io, self, self._root)
        elif _on == RadioControlProtocol.ServiceTypes.remove_radio_request:
            self.data = RadioControlProtocol.RemoveRadioRequest(
                self._io, self, self._root
            )
        elif (
            _on
            == RadioControlProtocol.ServiceTypes.broadcast_status_configuration_reply
        ):
            self.data = RadioControlProtocol.BroadcastStatusConfigurationReply(
                self._io, self, self._root
            )
        elif _on == RadioControlProtocol.ServiceTypes.remove_radio_reply:
            self.data = RadioControlProtocol.RemoveRadioReply(
                self._io, self, self._root
            )
        else:
            self.data = RadioControlProtocol.GenericData(self._io, self, self._root)

    class BroadcastStatusConfigurationReply(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.result = KaitaiStream.resolve_enum(
                RadioControlProtocol.ReplyResults, self._io.read_u1()
            )

    class BroadcastConfiguration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.config_operation = self._io.read_u1()
            self.config_target = self._io.read_u1()

    class BroadcastStatusConfigurationRequest(KaitaiStruct):
        """This message is used to enable/disable broadcast transmit/receive status reporting to RCP Application."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_broadcast_configuration = self._io.read_u1()
            self.broadcast_configuration = [None] * (self.num_broadcast_configuration)
            for i in range(self.num_broadcast_configuration):
                self.broadcast_configuration[
                    i
                ] = RadioControlProtocol.BroadcastConfiguration(
                    self._io, self, self._root
                )

    class RadioIdentificationReply(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._parent.message_length >= 6:
                self.header = self._io.read_bytes(6)

            if self._parent.message_length >= 198:
                self.text = (self._io.read_bytes(192)).decode(u"utf-16-be")

            if self._parent.message_length >= 206:
                self.footer = self._io.read_bytes(8)

    class GenericData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.data = self._io.read_bytes(self._parent.message_length)

    class CallRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.call_type = KaitaiStream.resolve_enum(
                RadioControlProtocol.CallTypes, self._io.read_u1()
            )
            self.target_id = self._io.read_u4le()

    class RemoveRadioReply(KaitaiStruct):
        """Response from Dispatch Station."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.result = KaitaiStream.resolve_enum(
                RadioControlProtocol.ReplyResults, self._io.read_u1()
            )

    class RemoveRadioRequest(KaitaiStruct):
        """Remove Radio Request is used by RCP Application to clear the last call target which was set by Call Request.
        If there is no call target, this request will do nothing.
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            pass

    class CallReply(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.result = KaitaiStream.resolve_enum(
                RadioControlProtocol.ReplyResults, self._io.read_u1()
            )
