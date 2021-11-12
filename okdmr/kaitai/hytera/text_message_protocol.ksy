meta:
  id: text_message_protocol
  imports:
    - radio_ip
enums:
  ack_flags:
    0: ack_required
    1: ack_not_required
  option_flags:
    0: option_len_and_field_disabled
    1: option_len_and_field_enabled
  service_types:
    0xA1: send_private_message
    0xA2: send_private_message_ack
    0xB1: send_group_message
    0xB2: send_group_message_ack
  result_codes:
    0: ok
    1: fail
    3: invalid_params
    4: channel_busy
    5: rx_only
    6: low_battery
    7: pll_unlock
    8: private_call_no_ack
    9: repeater_wakeup_fail
    10: no_contact
    11: tx_deny
    12: tx_interrupted
instances:
  option_sum_len:
    value: 'option_flag.to_i == 1 ? option_field_len + 2 : 0'
seq:
  - id: ack_flag
    type: b1
    enum: ack_flags
  - id: option_flag
    type: b1
    enum: option_flags
    doc: option fields might not be supported yet
  - id: reserved
    type: b6
  - id: service_type
    type: u1
    enum: service_types
  - id: message_length
    type: u2be
    doc: length of the message from next field to the end of TMP message
  - id: option_field_len
    type: u2be
    if: option_flag.to_i == 1
  - id: request_id
    type: u4be
  - id: destination_ip
    type: radio_ip
    doc: single or group target in ipv4 format
  - id: source_ip
    type: radio_ip
    doc: source of the message in ipv4 format
    if: service_type != service_types::send_group_message_ack
  - id: result
    type: u1
    enum: result_codes
    if: service_type == service_types::send_private_message_ack or service_type == service_types::send_group_message_ack
  - id: tmdata
    type: str
    encoding: UTF-16LE
    # message_len - req_id - dest_ip - source_ip - (2+option_field_len or 0)
    size: message_length - 4 - 4 - 4 - option_sum_len
    if: service_type == service_types::send_private_message or service_type == service_types::send_group_message
  - id: option_field
    type: str
    encoding: UTF-16LE
    size: option_field_len
    if: option_flag.to_i == 1
