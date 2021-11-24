meta:
  id: motorola_binary_xml
  endian: be
doc: |
  Motorola Binary XML parsing, contains and references LRRP (Location Request Response Protocol)
  and ARRP (Accessories Request Response Protocol), xml documents encoded in binary form
enums:
  docids:
    0x04: lrrp_immediate_request
    0x05: lrrp_immediate_request_ncdt
    0x06: lrrp_immediate_response
    0x07: lrrp_immediate_response_ncdt
  lrrp_elements:
    0x22: request_id_22_opaque
    0x23: request_id_23_opaque_1byte
    0x24: request_id_24_cdt_reference
types:
  uintvar:
    doc: |
      Variable length unsigned integer, first bit is "continue flag", 7 bits are payload
      maximum size is 2^32 - 1, ie. max size of uintvar is 32 bits
    seq:
      - id: payload
        type: u1
        repeat: until
        repeat-until: (_ & 0x80) == 0 or _io.eof
  sintvar:
    doc: |
      Variable length signed integer, first bit is "continue flag", 7 bits are payload
      (first bit of first payload is sign bit)
      maximum size is 2^32 - 1, ie. max size of sintvar is 32 bits
    seq:
      - id: payload
        type: u1
        repeat: until
        repeat-until: (_ & 0x80) == 0 or _io.eof
  ufloatvar:
    doc: |
      Variable length unsigned float, two consecutive uintvars, first represents integer part,
      second fraction part of float
    seq:
      - id: uint_payload
        type: uintvar
      - id: fraction_payload
        type: uintvar
  sfloatvar:
    doc: |
      Variable length signed float, first sintvar (signed integer part) then uintvar (unsigned fraction part)
    seq:
      - id: sint_payload
        type: sintvar
      - id: fraction_payload
        type: uintvar
  opaque_element_value:
    seq:
      - id: len_value
        type: u1
      - id: value
        size: len_value
  opaque_1byte_value:
    seq:
      - id: value
        size: 1
  opaque_2byte_value:
    seq:
      - id: value
        size: 2
  opaque_3byte_value:
    seq:
      - id: value
        size: 3
  opaque_4byte_value:
    seq:
      - id: value
        size: 4
  opaque_5byte_value:
    seq:
      - id: value
        size: 5
  constant_data_table_reference:
    seq:
      - id: byte_offset_from_cdt_start
        type: uintvar
  lrrp_element:
    seq:
      - id: lrrp_element_type
        enum: lrrp_elements
        type: u1
      - id: lrrp_element_data
        type:
          switch-on: lrrp_element_type
          cases:
            'lrrp_elements::request_id_22_opaque': opaque_element_value
            'lrrp_elements::request_id_23_opaque_1byte': opaque_1byte_value
            'lrrp_elements::request_id_24_cdt_reference': constant_data_table_reference
  lrrp_immediate_request_ncdt:
    seq:
      - id: elements
        type: lrrp_element
  mbxml_document:
    doc: |
      MBXML payload can contain multiple documents concatenated
    seq:
      - id: document_id
        enum: docids
        type: u1
        doc: |
          this should be uintvar, but enum matching is not possible against user-types, and maximum current docid is 0x27
          so it should not matter, unless new docid is bigger than 0x7F (dec:127)
      - id: num_document_bytes
        type: uintvar
      - id: document_data
        type:
          switch-on: document_id
          cases:
            'docids::lrrp_immediate_request_ncdt': lrrp_immediate_request_ncdt
seq:
  - id: documents
    type: mbxml_document
    repeat: until
    repeat-until: not _io.eof