from typing import Dict

from okdmr.kaitai.motorola.automatic_registration_service import (
    AutomaticRegistrationService,
)
from okdmr.kaitai.tools.prettyprint import prettyprint
from okdmr.tests.kaitai.test_utils import assert_expected_attribute_values


def test_ars():
    ars_hex_messages: Dict[str, Dict[str, any]] = {
        "000cf0200732333038303934000000": {
            "message_size": 3072,
            "message_header": {
                "acknowledgement_bit": True,
                "control_user_bit": True,
                "extension_bit": True,
                "pdu_type": 0,
                "priority": True,
            },
            "pdu_content": {
                "device_identifier": b"2308094",
                "len_device_identifier": 7,
                "len_password": 0,
                "len_user_identifier": 0,
                "device_registration_message_header": {
                    "encoding": 0,
                    "event": AutomaticRegistrationService.RegistrationEvents.initial_event,
                    "extension_bit": False,
                },
            },
        }
    }
    for ars_hex_message, validations in ars_hex_messages.items():
        ars = AutomaticRegistrationService.from_bytes(bytes.fromhex(ars_hex_message))
        prettyprint(ars)
        assert_expected_attribute_values(ars, validations)
