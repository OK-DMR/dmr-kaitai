def byteswap_bytearray(data: bytearray) -> bytes:
    trim = len(data) - 1
    # add padding, that will get removed, to have odd number of bytes
    if len(data) % 2 != 0:
        data.append(0x00)
    data[0::2], data[1::2] = data[1::2], data[0::2]
    return bytes(data[:trim])


def byteswap_bytes(data: bytes) -> bytes:
    return byteswap_bytearray(bytearray(data))
