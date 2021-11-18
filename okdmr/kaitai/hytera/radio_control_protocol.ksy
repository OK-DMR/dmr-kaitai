meta:
  id: radio_control_protocol
  endian: le
enums:
  service_types:
    0x0004: radio_identification_request
    0x82D4: radio_identification_reply
    0x0841: call_request
    0x8841: call_reply
    0x0842: remove_radio_request
    0x8842: remove_radio_reply
    0x10C9: broadcast_status_configuration_request
    0x80C9: broadcast_status_configuration_reply
    0xB843: broadcast_transmit_status
    0xB944: broadcast_receive_status
    0xB845: repeater_broadcast_transmit_status
    0x0041: button_and_keyboard_operation_request
    0x8041: button_and_keyboard_operation_reply
    0x00C4: zone_and_channel_operation_request
    0x80C4: zone_and_channel_operation_reply
    0x0201: radio_message_query_request
    0x8201: radio_message_query_reply
    0x00E7: channel_status_or_param_check_request
    0x80E7: channel_status_or_param_check_reply
    0x00ED: function_status_check_request
    0x80ED: function_status_check_reply
    0x00EE: function_enable_disable_request
    0x80EE: function_enable_disable_reply
    0x0044: internal_external_mic_gain_check_control_request
    0x8044: internal_external_mic_gain_check_control_reply
    0x0043: internal_external_mic_enable_disable_request
    0x8043: internal_external_mic_enable_disable_reply
    0x0045: internal_external_speaker_enable_disable_request
    0x8045: internal_external_speaker_enable_disable_reply
    0x0046: volume_check_control_request
    0x8046: volume_check_control_reply
    0x0131: channel_alias_request
    0x8131: channel_alias_reply
    0x0450: channel_number_of_zone_request
    0x8450: channel_number_of_zone_reply
    0x00CA: radio_connect_login_request
    0x80CA: radio_connect_login_reply
    0x00CB: radio_connect_logout_request
    0x80CB: radio_connect_logout_reply
    0x10C7: radio_status_configure_request
    0x80C7: radio_status_configure_reply
    0xB0C8: radio_status_report
    0x00C0: radio_configure_over_air_request
    0x80C0: radio_configure_over_air_reply
    0x0846: delete_subject_line_message_request
    0x8846: delete_subject_line_message_reply
    0x0451: update_authentication_key_request
    0x8451: update_authentication_key_reply
    0x0452: radio_id_and_radio_ip_query_request
    0x8452: radio_id_and_radio_ip_query_reply
    0x0849: radio_disable
    0x8849: radio_disable_ack
    0x084A: radio_enable
    0x884A: radio_enable_ack
    0x0833: radio_check
    0x8833: radio_check_ack
    0x0834: remote_monitor
    0x8834: remote_monitor_ack
    0x0835: allert_call
    0x8835: alert_call_ack
  call_types:
    0x00: private_call
    0x01: group_call
    0x02: all_call
    0x03: emergency_group_call
    0x04: remote_monitor_call
    0x05: reserved
    0x06: priority_private_call
    0x07: priority_group_call
    0x08: priority_all_call
  reply_results:
    0x00: success
    0x01: failure
types:
  call_request:
    seq:
      - id: call_type
        enum: call_types
        type: u1
      - id: target_id
        type: u4le
        doc: ignored for all_call
  call_reply:
    seq:
      - id: result
        type: u1
        enum: reply_results
  generic_data:
    seq:
      - id: data
        size: _parent.message_length
  remove_radio_request:
    doc: |
      Remove Radio Request is used by RCP Application to clear the last call target which was set by Call Request.
      If there is no call target, this request will do nothing.
  remove_radio_reply:
    doc: Response from Dispatch Station
    seq:
      - id: result
        type: u1
        enum: reply_results
  broadcast_configuration:
    seq:
      - id: config_operation
        type: u1
        doc: 0x00 => notifications off 0x01 => notifications on
      - id: config_target
        type: u1
        doc: 0x00 => broadcast transmit status, 0x01 => broadcast receive status, 0x02 => repeater broadcast transmit status
  broadcast_status_configuration_request:
    doc: This message is used to enable/disable broadcast transmit/receive status reporting to RCP Application.
    seq:
      - id: num_broadcast_configuration
        type: u1
      - id: broadcast_configuration
        type: broadcast_configuration
        repeat: expr
        repeat-expr: num_broadcast_configuration
  broadcast_status_configuration_reply:
    seq:
      - id: result
        type: u1
        enum: reply_results
  radio_identification_reply:
    seq:
      - id: header
        size: 6
        if: _parent.message_length >= 6
      - id: text
        type: str
        size: 192
        encoding: utf-16-be
        if: _parent.message_length >= 198
      - id: footer
        size: 8
        if: _parent.message_length >= 206
seq:
  - id: service_type
    type: u2le
    enum: service_types
  - id: message_length
    type: u2le
    doc: length of the message from next field to the end of RCP message
  - id: data
    type:
      switch-on: service_type
      cases:
        service_types::call_request: call_request
        service_types::call_reply: call_reply
        service_types::remove_radio_request: remove_radio_request
        service_types::remove_radio_reply: remove_radio_reply
        service_types::broadcast_status_configuration_request: broadcast_status_configuration_request
        service_types::broadcast_status_configuration_reply: broadcast_status_configuration_reply
        service_types::radio_identification_reply: radio_identification_reply
        _: generic_data