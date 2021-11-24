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
seq:
  - id: document_id
    enum: docids
    type: u1
    doc: |
      this should be uintvar, but enum matching is not possible against user-types, and maximum current docid is 0x27
      so it should not matter, unless new docid is bigger than 0x7F (dec:127)
  - id: num_document_bytes
    type: uintvar