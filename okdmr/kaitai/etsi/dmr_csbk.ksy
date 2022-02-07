meta:
  id: dmr_csbk
  endian: le
doc: |
  TS 102 361-2 V2.4.1 - section 7.1.2 Control Signalling BlocK (CSBK) PDUs
enums:
  csbko_types:
    0b111000: bs_outbound_activation_csbk_pdu
    0b000100: unit_to_unit_voice_service_request
    0b000101: unit_to_unit_voice_service_answer_response
    0b100110: negative_acknowledge_response
    0b111101: preamble
    0b000111: channel_timing
  csbk_data_or_csbk:
    0: csbk_content_follows_preambles
    1: data_content_follows_preambles
  csbk_group_or_individual:
    0: target_address_is_an_individual
    1: target_address_is_a_group
  answer_response:
    0b00100000: proceed
    0b00100001: deny
types:
  service_options:
    seq:
      - id: is_emergency_service
        type: b1
      - id: privacy
        type: b1
      - id: reserved
        type: b2
      - id: is_broadcast_service
        type: b1
      - id: is_open_voice_call_mode
        type: b1
      - id: priority_level
        type: b2
        doc: 00 => no priority, 11 => priority 3
  preamble_data:
    seq:
      - id: preamble_data_or_csbk
        type: b1
        enum: csbk_data_or_csbk
      - id: group_or_individual
        type: b1
        enum: csbk_group_or_individual
      - id: preamble_reserved
        type: b6
        doc: should read 0b000000
      - id: preamble_csbk_blocks_to_follow
        type: b8
      - id: target_address
        type: b24
      - id: source_address
        type: b24
  bs_outbound_activation_data:
    seq:
      - id: reserved
        type: b16
      - id: bs_address
        type: b24
      - id: source_address
        type: b24
  unit_to_unit_voice_request_data:
    seq:
      - id: service_options
        type: service_options
      - id: reserved
        type: b8
      - id: target_address
        type: b24
      - id: source_address
        type: b24
  unit_to_unit_voice_answer_data:
    seq:
      - id: service_options
        type: service_options
      - id: answer_response
        type: b8
        enum: answer_response
      - id: target_address
        type: b24
      - id: source_address
        type: b24
  negative_ack_response_data:
    seq:
      - id: additional_information_field
        type: b1
        doc: should read 0b1
      - id: source_type
        type: b1
      - id: service_type
        type: b6
      - id: reason_code
        type: b8
      - id: source_address
        type: b24
      - id: target_address
        type: b24
  channel_timing_data:
    seq:
      - id: sync_age
        type: b11
      - id: generation
        type: b5
      - id: leader_identifier
        type: b20
      - id: new_leader
        type: b1
      - id: leader_dynamic_identifier
        type: b2
      - id: channel_timing_op1
        type: b1
      - id: source_identifier
        type: b20
      - id: reserved
        type: b1
      - id: source_dynamic_identifier
        type: b2
      - id: channel_timing_op0
        type: b1
seq:
  - id: last_block
    type: b1
    doc: LB
  - id: protect_flag
    type: b1
    doc: PF
  - id: csbk_opcode
    type: b6
    doc: CSBKO
    enum: csbko_types
  - id: feature_set_id
    type: b8
    doc: FID
  - id: csbk_data
    type:
      switch-on: csbk_opcode
      cases:
        csbko_types::bs_outbound_activation_csbk_pdu: bs_outbound_activation_data
        csbko_types::unit_to_unit_voice_service_request: unit_to_unit_voice_request_data
        csbko_types::unit_to_unit_voice_service_answer_response: unit_to_unit_voice_answer_data
        csbko_types::negative_acknowledge_response: negative_ack_response_data
        csbko_types::preamble: preamble_data
        csbko_types::channel_timing: channel_timing_data