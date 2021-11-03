meta:
  id: text_message_protocol
  endian: le
enums:
  tms_service_capability:
    0: limited_capability
    1: internal_capability
    2: external_capability
    3: full_capability
types:
  message_header_bits:
    seq:
      - id: extension_bit
        type: b1
        doc: optional headers follow if this indicator is set
      - id: acknowledgement_required
        type: b1
        doc: if this PDU is request, this indicates requirement of "ACK response", if this PDU is response it indicates this is the required "ACK response"
      - id: reserved
        type: b1
        doc: unused/reserved
      - id: control_user_bit
        type: b1
        doc: 1 => this is control pdu message, 0 => this is user pdu message
      - id: pdu_type
        type: b4
        doc: depends on control_user_bit to distinguish pdu class
  tms_service_availability_header:
    seq:
      - id: extension_bit
        type: b1
        doc: should be 0
      - id: reserved
        type: b4
      - id: device
        type: b3
        enum: tms_service_capability
  tms_service_availability:
    doc: This message is used to announce Text Messaging Service availability on the system by the TMS Server
    seq:
      - id: header
        type: tms_service_availability_header
        if: _root.message_header.extension_bit
  tms_service_availability_acknowledgement:
    doc: |
      This message is used to positively acknowledge a service availability message (no headers or payload)
      Same as tms_acknowledgement, only in ack to tms_service_availability announcement no "sequence number" is expected
  tms_acknowledgement_header_sequence_number:
    doc: contains optionally both header bytes (lsb and msb if overflow is needed/occurred)
    instances:
      sequence_number:
        value: (header_msb_bits << 4) + header_lsb_bits
    seq:
      - id: has_msb_header
        type: b1
      - id: header_lsb_reserved
        type: b2
      - id: header_lsb_bits
        type: b5
      - id: header_msb_extension
        if: has_msb_header
        type: b1
      - id: header_msb_bits
        if: has_msb_header
        type: b2
      - id: header_msb_reserved
        if: has_msb_header
        type: b5
  tms_acknowledgement:
    doc: This message is used to positively acknowledge a text message.
    seq:
      - id: tms_acknowledgement_header_sequence_number
        if: _root.message_header.extension_bit
        type: tms_acknowledgement_header_sequence_number
  text_message_header_sequence_and_encoding:
    instances:
      sequence_number:
        value: (sequence_number_msb_bits << 4) + sequence_number_lsb_bits
    seq:
      - id: has_encoding_header
        type: b1
      - id: reserved_1
        type: b2
      - id: sequence_number_lsb_bits
        type: b5
      - id: header_encoding_extension
        type: b1
        if: has_encoding_header
      - id: sequence_number_msb_bits
        type: b2
        if: has_encoding_header
      - id: encoding
        type: b5
        doc: expected 0x04, only supported, UCS2-LE encoding
  text_message:
    doc: This message is used to send basic text messages.
    seq:
      - id: text_message_header_sequence_and_encoding
        type: text_message_header_sequence_and_encoding
        if: _root.message_header.extension_bit
      - id: text_message
        doc: |
          might include CR (0x0D00) and/or LF (0x0A00) if "message subject" is sent, then it's format is <subject><cr><lf><text>
        type: str
        encoding: utf-16-le
        size-eos: true
instances:
  custom_pdu_type:
    doc: special enumerable pdu type (ack-type + control-or-user + pdu-type-id)
    value: (_root.message_header.acknowledgement_required.to_i << 5) + (_root.message_header.control_user_bit.to_i << 4) + _root.message_header.pdu_type
seq:
  - id: message_size
    type: u2be
    doc: number of bytes to follow, always big endian
  - id: message_header
    type: message_header_bits
  - id: len_address
    type: u1
  - id: address
    doc: variable address field (might be string, int, ip, radio id, ...)
    size: len_address
    if: len_address > 0
  - id: pdu_content
    type:
      switch-on: custom_pdu_type
      cases:
        # 0b110000 (ack requested, is control, pdu %0000) - announce / request
        48: tms_service_availability
        # 0b011111 (ack not requested, is control, pdu %1111) - response to tms_service_availability
        31: tms_acknowledgement
        # 0b000000 (ack not requested, is user, pdu %0000) - text message un-confirmed
        0: text_message
        # 0b100000 (ack requested, is user, pdu %0000) - text message confirmed
        32: text_message
  - id: unparsed_data
    size-eos: true
