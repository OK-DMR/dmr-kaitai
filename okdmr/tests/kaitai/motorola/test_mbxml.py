from okdmr.kaitai.motorola.motorola_binary_xml import MotorolaBinaryXml
from okdmr.kaitai.motorola.motorola_utils import (
    uintvar_to_int,
    sintvar_to_int,
    ufloatvar_to_float,
    sfloatvar_to_float,
)
from okdmr.tests.kaitai.tests_utils import prettyprint


def test_uintvar():
    # tuples (decoded, encoded)
    uintvars = [(0x25, "25"), (0xA0, "8120"), (0x87A5, "828F25")]
    for t in uintvars:
        uint = MotorolaBinaryXml.Uintvar.from_bytes(bytes.fromhex(t[1]))
        prettyprint(uint)
        assert uintvar_to_int(uint.payload) == t[0]


def test_sintvar():
    # tuples (decoded, encoded)
    sintvars = [
        (-0x25, "65"),
        (-0xA0, "C120"),
    ]
    for t in sintvars:
        sint = MotorolaBinaryXml.Sintvar.from_bytes(bytes.fromhex(t[1]))
        prettyprint(sint)
        assert sintvar_to_int(sint.payload) == t[0]


def test_ufloatvar():
    # tuples (decoded, encoded, accuracy)
    ufloatvars = [
        (37 + (64 / 128), "2540", 1),
        (37 + (8192 / (128 ** 2)), "2540", 1),
        (160 + (7 / 128), "812007", 2),
        (160 + (983 / (128 ** 2)), "81208757", 2),
    ]
    for t in ufloatvars:
        ufloat = MotorolaBinaryXml.Ufloatvar.from_bytes(bytes.fromhex(t[1]))
        not_rounded: float = ufloatvar_to_float(
            ufloat.uint_payload.payload, ufloat.fraction_payload.payload
        )
        precision: int = t[2]
        print(
            f"ufloat raw: {not_rounded}, test precision: {precision} decimals, rounded: {round(not_rounded, precision)}"
            f" | reference raw: {t[0]}, rounded: {round(t[0], precision)}"
        )
        assert round(not_rounded, precision) == round(t[0], precision)


def test_sfloatvar():
    # tuples (decoded, encoded, accuracy)
    sfloatvars = [
        (-37 - (64 / 128), "6540", 1),
        (-160 - (983 / (128 ** 2)), "C1208757", 1),
    ]
    for t in sfloatvars:
        sfloat = MotorolaBinaryXml.Sfloatvar.from_bytes(bytes.fromhex(t[1]))
        not_rounded: float = sfloatvar_to_float(
            sfloat.sint_payload.payload, sfloat.fraction_payload.payload
        )
        precision: int = t[2]
        print(
            f"sfloat raw: {not_rounded}, test precision: {precision} decimals, rounded: {round(not_rounded, precision)}"
            f" | reference raw: {t[0]}, rounded: {round(t[0], precision)}"
        )
        assert round(not_rounded, precision) == round(t[0], precision)


def test_decode():
    lrrp_xml: str = """
    <Immediate-Location-Request>
    <request-id>2468ACE0</request-id>
    <query-info>
    <ret-info ret-info-time="YES" ret-info-accuracy="YES"/>
    <request-speed-hor/>
    </query-info>
    </Immediate-Location-Request>
    """

    lrrp_mbxml: bytes = bytes.fromhex("050822042468ace05162")
    prettyprint(MotorolaBinaryXml.from_bytes(lrrp_mbxml))
