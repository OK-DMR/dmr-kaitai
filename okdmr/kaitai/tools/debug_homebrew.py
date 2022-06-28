from okdmr.kaitai.homebrew.homebrew2015 import Homebrew2015
from okdmr.kaitai.homebrew.mmdvm2020 import Mmdvm2020
from okdmr.kaitai.tools.debug import ProtocolDebug


class DebugHomebrew(ProtocolDebug):
    @staticmethod
    def homebrew() -> None:
        DebugHomebrew._impl(
            protocol="Homebrew 2015 - Original IPSC protocol for homebrew repeaters by DL5DI, G4KLX, DG1HT",
            kaitai=Homebrew2015,
        )

    @staticmethod
    def mmdvm() -> None:
        DebugHomebrew._impl(
            protocol="MMDVM 2020 - Evolution of Homebrew protocol used currently",
            kaitai=Mmdvm2020,
        )
