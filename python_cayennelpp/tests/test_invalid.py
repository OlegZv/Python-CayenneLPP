from python_cayennelpp.decoder import decode
import pytest


def test_invalid_length():
    with pytest.raises(ValueError) as e:
        assert decode("026711")
    assert str(e.value) == "The length on the payload 026711 is 6 doesn't correspond to expected 8"


def test_invalid_type():
    with pytest.raises(TypeError) as e:
        assert decode(13)
    assert str(e.value) == "Payload must be hex encoded string. Provided type: <class 'int'>"


def test_invalid_type2():
    with pytest.raises(TypeError) as e:
        assert decode(b"02670113")
    assert str(e.value) == "Payload must be hex encoded string. Provided type: <class 'bytes'>"


def test_invalid_key(capsys):
    a = decode("0167023302991233")
    captured = capsys.readouterr()
    assert captured.out == "[ERROR]: Decoding failed or incomplete. Unrecognized sensor type: 99\n"
    assert a == [{'channel': 1, 'name': 'Temperature Sensor', 'value': 56.3}]
