from okdmr.kaitai.motorola.automatic_registration_service import (
    AutomaticRegistrationService,
)
from okdmr.kaitai.motorola.text_message_protocol import TextMessageProtocol
from okdmr.kaitai.tools.debug import ProtocolDebug


class DebugMotorola(ProtocolDebug):
    @staticmethod
    def ars() -> None:
        DebugMotorola._impl(
            protocol="Motorola ARS - Automatic Registration Service",
            kaitai=AutomaticRegistrationService,
        )

    @staticmethod
    def tmp() -> None:
        DebugMotorola._impl(
            protocol="Motorola TMP - Text Message Protocol", kaitai=TextMessageProtocol
        )
