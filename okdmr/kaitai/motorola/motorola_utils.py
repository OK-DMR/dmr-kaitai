from typing import List


def uintvar_to_int(payload: List[int]) -> int:
    _out: int = 0
    for single in payload:
        _out = (_out << 7) + (single & 0x7F)
    return _out


def clear_msb(dirty: int) -> int:
    return int("0" + bin(dirty)[3:], 2)


def sintvar_to_int(payload: List[int]) -> int:
    # remove first bit, which is sign-bit
    _out = clear_msb(uintvar_to_int(payload))
    # calculate final sign of int
    _is_negative = (payload[0] & 0x40) > 0
    return -_out if _is_negative else _out


def ufloatvar_to_float(int_part: List[int], fraction_part: List[int]) -> float:
    return uintvar_to_int(int_part) + (
        uintvar_to_int(fraction_part) / 128 ** len(fraction_part)
    )


def sfloatvar_to_float(sint_part: List[int], fraction_part: List[int]) -> float:
    _out: float = clear_msb(uintvar_to_int(sint_part)) + (
        uintvar_to_int(fraction_part) / 128 ** len(fraction_part)
    )
    _is_negative = (sint_part[0] & 0x40) > 0
    return -_out if _is_negative else _out
