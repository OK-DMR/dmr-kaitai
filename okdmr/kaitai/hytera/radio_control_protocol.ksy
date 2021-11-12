meta:
  id: radio_control_protocol
  endian: le
enums:
  service_types:
    0x0841: call_request
    0x8841: call_reply
    0x0842: remove_call_request
    0x8842: remove_call_reply
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
  call_reply_results:
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
        enum: call_reply_results
  generic_data:
    seq:
      - id: data
        size: _parent.message_length
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
        _: generic_data