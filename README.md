# DMR Kaitai protocols

![.github/workflows/sanity.yml](https://img.shields.io/github/actions/workflow/status/OK-DMR/dmr-kaitai/sanity.yml?style=flat-square&branch=master)
![Code Style: Python Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)
![License](https://img.shields.io/pypi/l/dmr-kaitai?style=flat-square)
![Last released version](https://img.shields.io/pypi/v/dmr-kaitai?style=flat-square)
![PyPI downloads](https://img.shields.io/pypi/dm/dmr-kaitai?style=flat-square)
![Python versions](https://img.shields.io/pypi/pyversions/dmr-kaitai?style=flat-square)
![Wheel](https://img.shields.io/pypi/wheel/dmr-kaitai?style=flat-square)

This repository contains [Kaitai-IO](https://kaitai.io/) definitions of various protocols that can be met in DMR
networks, both amateur and professional

## Contributing

Please follow these steps

1. Add or update `.ksy` definition file
2. Run re-compilation script `./rebuild-all.sh` (generates .py from .ksy and formats them using *black* formatter)
3. Provide at least one example dataset to check the implementation with

And specifically avoid these mistakes:

1. Modifying generated python sources / dissectors after generating

## Supported

- ETSI
    - CSBK (all from TS 102 361-2)
    - Data Blocks (Rate 1, 1/2, 3/4 confirmed and unconfirmed)
    - Data Headers (UDT, Response, Unconfirmed, Confirmed, Short Data Defined, Short Status Precoded, Proprietary)
    - UDP IPv4 Compressed header
    - FULL LC (Full Link Control, Group/Individual voice, GPS Info, Talker Alias + continuation blocks)
- HAM
    - Homebrew 2015 (per DL5DI, G4KLX, DG1HT 2015)
    - Mmdvm 2020 (with non-standardized features in mmdvm-host, dmr-gateway, hblink and others)
- Hytera
    - Data Delivery States
    - Data Transmit Protocol
    - GPS Data
    - HDAP (Hytera DMR Application Protocol)
    - HRNP (Hytera Radio Network Protocol)
    - HSTRP (Hytera Simple Transport Reliability Protocol)
    - IPSC (with separate definition for IPSC Heartbeat)
    - LP (Location Protocol)
    - RCP (Radio Control Protocol)
    - RRS (Radio Registration Service)
    - RTTP (Real-time Transport Protocol)
    - TP (Telemetry Protocol)
    - TMP (Text Message Protocol)
- Motorola
    - ARS (Automatic Registration Service)
    - MBXML (Motorola Binary XML) - only partially supported now
    - TMP (Text Message Protocol)

## Testing

run `make test` (or pytest directly like this `env PYTHONPATH=. pytest -vrpP`)

## Development notes

1) Use `make test`, `make build` or `make test-only` (without rebuilding the .py files first), or use the commands from Makefile directly, if you don't have `make` available
2) If you intend to modify/develop this library, use `python3 -m pip install -e --upgrade .`, changes to dmr-kaitai project sources are then automatically propagated to your environment without re-installing

## Tools

If you install through `pip3 install dmr-kaitai` or manually from repo using `python3 -m pip install .`, you should be
provided with command-line tools,
to pass hex payloads of various protocols to and see what is inside. Tools support multiple hex payloads, each hex
string is treated as separate PDU to parse and pretty-print

Usage example

```
> debug-hytera-hrnp 7e0400002010000100189b6002040005006400000001c403
{'block': 0,
 'checksum': 39776,
 'data': {'checksum': 196,
          'data': {'data': {'data': b'd\x00\x00\x00\x01'},
                   'message_length': 5,
                   'service_type': <ServiceTypes.radio_identification_request: 4>},
          'is_reliable_message': False,
          'message_footer': b'\x03',
          'message_header': <MessageHeaderTypes.radio_control_protocol: 2>},
 'destination_id': 16,
 'header_identifier': b'~',
 'hrnp_packet_length': 24,
 'opcode': <Opcodes.data: 0>,
 'packet_number': 1,
 'source_id': 32,
 'version': 4}
```

Full listing of available tools

- debug-homebrew
- debug-mmdvm
- debug-hytera-rcp
- debug-hytera-hdap
- debug-hytera-hrnp
- debug-hytera-hstrp
- debug-hytera-tmp
- debug-hytera-lp
- debug-hytera-ipsc
- debug-hytera-rrs
- debug-hytera-dds
- debug-hytera-dtp
- debug-motorola-ars
- debug-motorola-tmp

## License

AGPLv3.0 see LICENSE file for more info
