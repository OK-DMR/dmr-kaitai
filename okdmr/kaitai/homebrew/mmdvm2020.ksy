meta:
  id: mmdvm2020
  endian: be
doc: |
  MMDVM protocol structure (MMDVMHost/HBlink3/DMRGateway) based on reversing effort
enums:
  timeslots:
    0: "timeslot_1"
    1: "timeslot_2"
  call_types:
    0: "group_call"
    1: "private_call"
  talker_alias_types:
    0: talker_alias_header
    1: talker_alias_block_1
    2: talker_alias_block_2
    3: talker_alias_block_3
  position_errors:
    0b000: less_than_2m
    0b001: less_than_20m
    0b010: less_than_200m
    0b011: less_than_2km
    0b100: less_than_20km
    0b101: less_than_or_equal_200km
    0b110: more_than_200km
    0b111: position_error_unknown_or_invalid
types:
  type_unknown:
    seq:
      - id: unknown_data
        size-eos: true
  type_talker_alias:
    seq:
      - id: radio_id
        type: b24
      - id: talker_alias_type
        enum: talker_alias_types
        type: u1
      - id: talker_alias
        type: str
        size: 8
        encoding: ASCII
  type_dmr_data:
    seq:
      - id: sequence_no
        type: u1
      - id: source_id
        type: b24
      - id: target_id
        type: b24
      - id: repeater_id
        type: u4
      - id: slot_no
        type: b1
        enum: timeslots
      - id: call_type
        type: b1
        enum: call_types
      - id: frame_type
        type: b2
      - id: data_type
        type: b4
      - id: stream_id
        type: u4
      - id: dmr_data
        size: 33
      - id: bit_error_rate
        type: u1
        if: not _io.eof
      - id: rssi
        type: u1
        if: not _io.eof
  type_repeater_login_request:
    seq:
      - id: repeater_id
        type: u4
  type_repeater_ping:
    seq:
      - id: magic
        contents: ING
      - id: repeater_id
        type: u4
  type_master_pong:
    seq:
      - id: magic
        contents: ONG
      - id: repeater_id
        type: u4
  type_master_closing:
    seq:
      - id: magic
        contents: L
      - id: repeater_id
        type: u4
  type_master_not_accept:
    seq:
      - id: magic
        contents: AK
      - id: repeater_id
        type: u4
  type_master_repeater_ack:
    seq:
      - id: magic
        contents: CK
      - id: repeater_id_or_challenge
        type: u4
  type_repeater_login_response:
    seq:
      - id: repeater_id
        type: u4
      - id: sha256
        size: 32
  type_repeater_configuration_or_closing:
    seq:
      - id: data
        type:
          switch-on: _root.fifth_letter
          cases:
            _: type_repeater_configuration
            '"L"': type_repeater_closing
  type_repeater_closing:
    seq:
      - id: magic
        contents: L
      - id: repeater_id
        type: u4
  type_repeater_configuration:
    seq:
      - id: repeater_id
        type: u4
      - id: call_sign
        type: str
        encoding: ASCII
        size: 8
      - id: rx_freq
        type: str
        encoding: ASCII
        size: 9
      - id: tx_freq
        type: str
        encoding: ASCII
        size: 9
      - id: tx_power
        type: str
        encoding: ASCII
        size: 2
      - id: color_code
        type: str
        encoding: ASCII
        size: 2
      - id: latitude
        type: str
        encoding: ASCII
        size: 8
      - id: longitude
        type: str
        encoding: ASCII
        size: 9
      - id: antenna_height_above_ground
        size: 3
        type: str
        encoding: ASCII
      - id: location
        type: str
        size: 20
        encoding: ASCII
      - id: description
        type: str
        size: 19
        encoding: ASCII
      - id: slots
        type: str
        encoding: ASCII
        size: 1
        doc: 1 = only slot 1, 2 = only slot 2, 3 = both slots
      - id: url
        type: str
        size: 124
        encoding: ASCII
      - id: software_id
        type: str
        size: 40
        encoding: ASCII
      - id: package_id
        type: str
        encoding: ASCII
        size: 40
      - id: unparsed_data
        size-eos: true
        type: str
        encoding: ASCII
  type_repeater_options:
    seq:
      - id: repeater_id
        type: u4
      - id: options
        type: str
        encoding: ASCII
        size-eos: true
        doc: structure probably key=value;key=value;...
  type_radio_position:
    doc: etsi dmr, link control, type flcos::gps_info, specifically gps_info_lc_pdu
    seq:
      - id: radio_id
        type: b24
      - id: reserved
        type: b4
      - id: position_error
        type: b3
        enum: position_errors
      - id: longitude
        type: b25
      - id: latitude
        type: b24
  type_repeater_beacon:
    doc: undefined currently
instances:
  fifth_letter:
    pos: 4
    type: str
    encoding: ASCII
    size: 1
seq:
  - id: command_prefix
    type: str
    encoding: ASCII
    size: 4
  - id: command_data
    type:
      switch-on: command_prefix
      cases:
        '"DMRA"': type_talker_alias
        '"DMRG"': type_radio_position
        '"DMRD"': type_dmr_data
        '"MSTC"': type_master_closing
        '"MSTP"': type_master_pong
        '"MSTN"': type_master_not_accept
        '"RPTP"': type_repeater_ping
        '"RPTO"': type_repeater_options
        '"RPTL"': type_repeater_login_request
        '"RPTA"': type_master_repeater_ack
        '"RPTK"': type_repeater_login_response
        '"RPTC"': type_repeater_configuration_or_closing
        '"RPTS"': type_repeater_beacon
