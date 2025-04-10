# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, "API_VERSION", (0, 9)) < (0, 9):
    raise Exception(
        "Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s"
        % (kaitaistruct.__version__)
    )

from okdmr.kaitai.hytera import radio_ip
from okdmr.kaitai.hytera import gpsdata
from okdmr.kaitai.hytera import datetimestring
from okdmr.kaitai.hytera import intervalstring


class LocationProtocol(KaitaiStruct):

    class CmdTypes(Enum):
        cancel_request = 0
        start_request = 1

    class LpSpecificTypes(Enum):
        standard_request = 40961
        standard_answer = 40962
        standard_answer_with_rssi = 40963
        standard_answer_gps_bt = 40964
        emergency_report_stop_request = 45057
        emergency_report_stop_answer = 45058
        emergency_report = 45059
        triggered_report_request = 49153
        triggered_report_answer = 49154
        triggered_report = 49155
        triggered_report_stop_request = 49156
        triggered_report_stop_answer = 49157
        condition_report_request = 53249
        condition_report_answer = 53250
        condition_report = 53251
        condition_report_with_rssi = 53252
        condition_quick_gps_request = 53265
        condition_quick_gps_answer = 53266

    class LpGeneralTypes(Enum):
        standard_location_immediate_service = 160
        emergency_location_reporting_service = 176
        triggered_location_reporting_service = 192
        condition_triggered_reporting_service = 208
        rssi_report_configuring_service = 224

    class TriggerTypes(Enum):
        cancel_request = 0
        distance = 1
        time = 2
        distance_and_time = 3
        distance_or_time = 4

    class ResultCodes(Enum):
        ok = 0
        position_method_failure = 6
        request_format_error = 105

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.opcode_header = KaitaiStream.resolve_enum(
            LocationProtocol.LpSpecificTypes, self._io.read_u2be()
        )
        self.message_length = self._io.read_u2be()
        _on = self.opcode_header
        if _on == LocationProtocol.LpSpecificTypes.triggered_report_answer:
            self.data = LocationProtocol.TriggeredReportAnswer(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.emergency_report_stop_request:
            self.data = LocationProtocol.EmergencyReportStopRequest(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.condition_quick_gps_request:
            self.data = LocationProtocol.ConditionQuickGpsRequest(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.condition_report:
            self.data = LocationProtocol.ConditionReport(self._io, self, self._root)
        elif _on == LocationProtocol.LpSpecificTypes.emergency_report_stop_answer:
            self.data = LocationProtocol.EmergencyReportStopAnswer(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.condition_report_answer:
            self.data = LocationProtocol.ConditionReportAnswer(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.standard_answer:
            self.data = LocationProtocol.StandardAnswer(self._io, self, self._root)
        elif _on == LocationProtocol.LpSpecificTypes.standard_request:
            self.data = LocationProtocol.StandardRequest(self._io, self, self._root)
        elif _on == LocationProtocol.LpSpecificTypes.triggered_report:
            self.data = LocationProtocol.TriggeredReport(self._io, self, self._root)
        elif _on == LocationProtocol.LpSpecificTypes.triggered_report_stop_answer:
            self.data = LocationProtocol.TriggeredReportStopAnswer(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.standard_answer_with_rssi:
            self.data = LocationProtocol.StandardAnswerWithRssi(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.condition_report_with_rssi:
            self.data = LocationProtocol.ConditionReportWithRssi(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.triggered_report_stop_request:
            self.data = LocationProtocol.TriggeredReportStopRequest(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.emergency_report:
            self.data = LocationProtocol.EmergencyReport(self._io, self, self._root)
        elif _on == LocationProtocol.LpSpecificTypes.condition_report_request:
            self.data = LocationProtocol.ConditionReportRequest(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.triggered_report_request:
            self.data = LocationProtocol.TriggeredReportRequest(
                self._io, self, self._root
            )
        elif _on == LocationProtocol.LpSpecificTypes.condition_quick_gps_answer:
            self.data = LocationProtocol.ConditionQuickGpsAnswer(
                self._io, self, self._root
            )

    class TriggeredReportStopAnswer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )

    class ConditionReportRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.trigger_type = self._io.read_u1()
            self.distance = self._io.read_u4be()
            self.start_time = datetimestring.Datetimestring(self._io)
            self.stop_time = datetimestring.Datetimestring(self._io)
            self.interval = intervalstring.Intervalstring(self._io)
            self.max_interval = intervalstring.Intervalstring(self._io)

    class ConditionQuickGpsRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.cmd_type = KaitaiStream.resolve_enum(
                LocationProtocol.CmdTypes, self._io.read_u1()
            )
            if self.cmd_type == LocationProtocol.CmdTypes.start_request:
                self.quick_gps_payload = LocationProtocol.QuickGpsPayload(
                    self._io, self, self._root
                )

    class ConditionReport(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.gpsdata = gpsdata.Gpsdata(self._io)

    class EmergencyReport(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.emergency_type = self._io.read_u1()
            self.gpsdata = gpsdata.Gpsdata(self._io)

    class TriggeredReportAnswer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )

    class StandardAnswerWithRssi(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )
            self.gpsdata = gpsdata.Gpsdata(self._io)
            self.rssi_value = self._io.read_s2be()

    class QuickGpsPayload(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.start_time = datetimestring.Datetimestring(self._io)
            self.stop_time = datetimestring.Datetimestring(self._io)
            self.interval = intervalstring.Intervalstring(self._io)
            self.send_step = self._io.read_u2be()
            self.channel_use_percentage = self._io.read_u1()
            self.send_order = self._io.read_u2be()

    class StandardRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)

    class TriggeredReportRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.start_time = datetimestring.Datetimestring(self._io)
            self.stop_time = datetimestring.Datetimestring(self._io)
            self.interval = intervalstring.Intervalstring(self._io)

    class StandardAnswer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )
            self.gpsdata = gpsdata.Gpsdata(self._io)

    class ConditionReportAnswer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.trigger_type = KaitaiStream.resolve_enum(
                LocationProtocol.TriggerTypes, self._io.read_u1()
            )
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )

    class EmergencyReportStopRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)

    class ConditionQuickGpsAnswer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.cmd_type = KaitaiStream.resolve_enum(
                LocationProtocol.CmdTypes, self._io.read_u1()
            )
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )

    class TriggeredReport(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.time_remaining = intervalstring.Intervalstring(self._io)
            self.gpsdata = gpsdata.Gpsdata(self._io)

    class ConditionReportWithRssi(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )
            self.gpsdata = gpsdata.Gpsdata(self._io)
            self.rssi_value = self._io.read_s2be()

    class EmergencyReportStopAnswer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)
            self.result = KaitaiStream.resolve_enum(
                LocationProtocol.ResultCodes, self._io.read_u2be()
            )

    class TriggeredReportStopRequest(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.request_id = self._io.read_u4be()
            self.radio_ip = radio_ip.RadioIp(self._io)

    @property
    def opcode(self):
        if hasattr(self, "_m_opcode"):
            return self._m_opcode

        _pos = self._io.pos()
        self._io.seek(0)
        self._m_opcode = KaitaiStream.resolve_enum(
            LocationProtocol.LpGeneralTypes, self._io.read_u1()
        )
        self._io.seek(_pos)
        return getattr(self, "_m_opcode", None)
