meta:
  id: automatic_registration_service
  endian: le
enums:
  registration_events:
    0x01: initial_event
    0x02: refresh_event
  failure_reasons:
    0x00: device_not_authorized
types:
  message_header_bits:
    seq:
      - id: extension_bit
        type: b1
        doc: optional headers follow if this indicator is set
      - id: acknowledgement_bit
        type: b1
        doc: if this PDU is request, this indicates requirement of "ACK response", if this PDU is response it indicates successfull "ACK response" (0 means failure)
      - id: priority
        type: b1
        doc: 1 is high priority, 0 is normal priority, in general all control PDUs are set as priority
      - id: control_user_bit
        type: b1
        doc: 1 => this is control pdu message, 0 => this is user pdu message
      - id: pdu_type
        type: b4
        doc: depends on control_user_bit to distinguish pdu class
  device_registration_message_header:
    seq:
      - id: extension_bit
        type: b1
        doc: expected 0
      - id: event
        type: b2
        enum: registration_events
      - id: encoding
        type: b5
        doc: expect 0x00 meaning UTF8 encoding of registration message fields
  device_registration_message:
    doc: sent by device to ARS service
    seq:
      - id: device_registration_message_header
        if: _root.message_header.extension_bit
        type: device_registration_message_header
      - id: len_device_identifier
        type: u1
      - id: device_identifier
        size: len_device_identifier
        if: len_device_identifier > 0
      - id: len_user_identifier
        type: u1
      - id: user_identifier
        size: len_user_identifier
        if: len_user_identifier > 0
      - id: len_password
        type: u1
      - id: password
        size: len_password
        if: len_password > 0
  device_registration_acknowledgement_header:
    doc: part of successfull ACK response
    seq:
      - id: extension_bit
        type: b1
        doc: expect 0
      - id: refresh_time
        type: b7
        doc: 0 = no refresh required, 1 = 30 minutes, 2 = 60 minutes, ..., 127 = 3810 minutes (approx. 2.645 days)
  device_registration_acknowledgement_failure_reason:
    doc: part of failure/unsuccessfull ACK response
    seq:
      - id: extension_bit
        type: b1
        doc: expect 0
      - id: failure_reason
        type: b7
        enum: failure_reasons
  acknowledgement_message:
    doc: |
      sent by ARS service to device as a response to device_registration_message
      sent by subscriber as a response to ars_query_message
    seq:
      - id: device_registration_acknowledgement_header
        type: device_registration_acknowledgement_header
        if: _root.message_header.extension_bit and _root.message_header.acknowledgement_bit
      - id: device_registration_acknowledgement_failure_reason
        if: _root.message_header.extension_bit and not _root.message_header.acknowledgement_bit
        type: device_registration_acknowledgement_failure_reason
  device_deregistration_message:
    doc: sent by device in case of deregistration, does not require ACK response
  ars_query_message:
    doc: sent by service to device/subscriber to check if the user is registered with ARS
seq:
  - id: message_size
    type: u2
    doc: number of bytes to follow after this field
  - id: message_header
    type: message_header_bits
  - id: pdu_content
    type:
      switch-on: message_header.pdu_type
      cases:
        # %0000 ars request (device -> service)
        0: device_registration_message
        # %0001 ars deregistration (device -> service)
        1: device_deregistration_message
        # %0100 ars query message (service -> device)
        4: ars_query_message
        # %1111 ars response / query acknowledgement (service -> device)
        15: acknowledgement_message
  - id: unparsed_data
    size-eos: true