from okdmr.kaitai.hytera.radio_ip import RadioIp


def test_radio_ip():
    hex_ips = [
        ("0a000001", 10, 1, "10.0.0.1"),
        ("0a000050", 10, 80, "10.0.0.80"),
        ("5001172D", 80, 71469, "80.1.23.45"),
        ("500C2238", 80, 795192, "80.12.34.56"),
        ("0a0a0001", 10, 655361, "10.10.0.1"),
        ("0a2110dd", 10, 2167005, "10.33.16.221"),
    ]
    for hexip, _subnet, _id, _ip in hex_ips:
        radioip = RadioIp.from_bytes(bytes.fromhex(hexip))
        assert radioip.radio_id == _id
        assert radioip.subnet == _subnet
        assert radioip.radio_ip == _ip
