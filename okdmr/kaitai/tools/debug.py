import sys
from argparse import ArgumentParser
from typing import Type, Optional, List

from kaitaistruct import KaitaiStruct
from okdmr.kaitai.hytera.ip_site_connect_protocol import IpSiteConnectProtocol
from okdmr.kaitai.tools.byteswap import byteswap_bytes
from okdmr.kaitai.tools.prettyprint import prettyprint


class ProtocolDebug:
    @staticmethod
    def _args(protocol: str) -> ArgumentParser:
        parser = ArgumentParser(description="Debug packet")
        parser.add_argument(
            "hex", type=str, nargs="+", help=f"Hex encoded messages of {protocol}"
        )
        return parser

    @staticmethod
    def _impl(
        protocol: str, kaitai: Type[KaitaiStruct], arguments: Optional[List[str]] = None
    ) -> None:
        args = ProtocolDebug._args(protocol=protocol).parse_args(
            sys.argv[1:] if (not arguments or not len(arguments)) else arguments
        )
        for hex_msg in args.hex:
            ars = kaitai.from_bytes(bytes.fromhex(hex_msg))
            if isinstance(ars, IpSiteConnectProtocol):
                getattr(ars, "source_radio_id")
                getattr(ars, "destination_radio_id")
                getattr(ars, "color_code")
                getattr(ars, "is_wakeup")
            prettyprint(ars)
            if (
                isinstance(ars, IpSiteConnectProtocol)
                and ars.slot_type is not IpSiteConnectProtocol.SlotTypes.slot_type_sync
            ):
                print(f"DMR DATA: {byteswap_bytes(ars.ipsc_payload).hex()}")
