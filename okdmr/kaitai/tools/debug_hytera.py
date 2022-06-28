from okdmr.kaitai.hytera.data_delivery_states import DataDeliveryStates
from okdmr.kaitai.hytera.data_transmit_protocol import DataTransmitProtocol
from okdmr.kaitai.hytera.hytera_dmr_application_protocol import (
    HyteraDmrApplicationProtocol,
)
from okdmr.kaitai.hytera.hytera_radio_network_protocol import HyteraRadioNetworkProtocol
from okdmr.kaitai.hytera.hytera_simple_transport_reliability_protocol import (
    HyteraSimpleTransportReliabilityProtocol,
)
from okdmr.kaitai.hytera.ip_site_connect_protocol import IpSiteConnectProtocol
from okdmr.kaitai.hytera.location_protocol import LocationProtocol
from okdmr.kaitai.hytera.radio_control_protocol import RadioControlProtocol
from okdmr.kaitai.hytera.radio_registration_service import RadioRegistrationService
from okdmr.kaitai.hytera.telemetry_protocol import TelemetryProtocol
from okdmr.kaitai.hytera.text_message_protocol import TextMessageProtocol
from okdmr.kaitai.tools.debug import ProtocolDebug


class DebugHytera(ProtocolDebug):
    @staticmethod
    def rrs() -> None:
        DebugHytera._impl(
            protocol="Hytera RRS - Radio Registration Service",
            kaitai=RadioRegistrationService,
        )

    @staticmethod
    def tmp() -> None:
        DebugHytera._impl(
            protocol="Hytera TMP - Text Message Protocol", kaitai=TextMessageProtocol
        )

    @staticmethod
    def ipsc() -> None:
        DebugHytera._impl(
            protocol="Hytera IPSC - IP (Multi-)Site Connect Protocol",
            kaitai=IpSiteConnectProtocol,
        )

    @staticmethod
    def rcp() -> None:
        DebugHytera._impl(
            protocol="Hytera RCP - Radio Control Protocol", kaitai=RadioControlProtocol
        )

    @staticmethod
    def dds() -> None:
        DebugHytera._impl(
            protocol="Hytera DDS - Data Delivery States", kaitai=DataDeliveryStates
        )

    @staticmethod
    def hdap() -> None:
        DebugHytera._impl(
            protocol="Hytera HDAP - DMR Application Protocol",
            kaitai=HyteraDmrApplicationProtocol,
        )

    @staticmethod
    def hrnp() -> None:
        DebugHytera._impl(
            protocol="Hytera HRNP - Radio Network Protocol",
            kaitai=HyteraRadioNetworkProtocol,
        )

    @staticmethod
    def hstrp() -> None:
        DebugHytera._impl(
            protocol="Hytera HSTRP - Simple Transport Reliability Protocol",
            kaitai=HyteraSimpleTransportReliabilityProtocol,
        )

    @staticmethod
    def lp() -> None:
        DebugHytera._impl(
            protocol="Hytera LP - Location Protocol", kaitai=LocationProtocol
        )

    @staticmethod
    def dtp() -> None:
        DebugHytera._impl(
            protocol="Hytera DTP - Data Transmit Protocol", kaitai=DataTransmitProtocol
        )

    @staticmethod
    def tp() -> None:
        DebugHytera._impl(
            protocol="Hytera TP - Telemetry Protocol", kaitai=TelemetryProtocol
        )
