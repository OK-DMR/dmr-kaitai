from okdmr.kaitai.hytera.radio_ip import RadioIp


def test_radio_ip():
    hex_ips = [
        ("0a000001", 10, 1, "001"),
        ("0a000050", 10, 80, "0080"),
        ("5001172D", 80, 12345, "12345"),
        ("500C2238", 80, 123456, "123456"),
        ("0a0a0001", 10, 100001, "1001"),
    ]
    for (hexip, _subnet, _id, _id_str) in hex_ips:
        radioip = RadioIp.from_bytes(bytes.fromhex(hexip))
        assert radioip.radio_id == _id
        assert radioip.subnet == _subnet
        assert radioip.radio_id_str == _id_str
