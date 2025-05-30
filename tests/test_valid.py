from python_cayennelpp.decoder import decode


def test_digital_in():
    expected = [{"channel": 9, "name": "Digital Input", "value": 34}]
    result = decode("090022")
    assert result == expected


def test_digital_out():
    expected = [{"channel": 17, "name": "Digital Output", "value": 34}]
    result = decode("110122")
    assert result == expected


def test_analog_in():
    expected = [{"channel": 5, "name": "Analog Input", "value": 48.84}]
    result = decode("05021314")
    assert result == expected


def test_analog_out():
    expected = [{"channel": 17, "name": "Analog Output", "value": 54.61}]
    result = decode("11031555")
    assert result == expected


def test_analog_in_signed():
    expected = [{"channel": 5, "name": "Analog Input", "value": -78.21}]
    result = decode("0502E173")
    assert result == expected


def test_analog_out_signed():
    expected = [{"channel": 17, "name": "Analog Output", "value": -23.0}]
    result = decode("1103F704")
    assert result == expected


def test_illuminance():
    expected = [{"channel": 23, "name": "Illuminance Sensor", "value": 29509}]
    result = decode("17657345")
    assert result == expected


def test_presence():
    expected = [{"channel": 119, "name": "Presence Sensor", "value": 3}]
    result = decode("776603")
    assert result == expected


def test_temp():
    expected = [{"channel": 3, "name": "Temperature Sensor", "value": 27.2}]
    result = decode("03670110")
    assert result == expected


def test_temp_signed():
    expected = [{"channel": 3, "name": "Temperature Sensor", "value": -12.5}]
    result = decode("0367FF83")
    assert result == expected


def test_humidity():
    expected = [{"channel": 7, "name": "Humidity Sensor", "value": 17.0}]
    result = decode("076822")
    assert result == expected


def test_accelerometer():
    expected = [
        {
            "channel": 83,
            "name": "Accelerometer",
            "value": {"x": 4.66, "y": 22.136, "z": -28.381},
        }
    ]
    result = decode("5371123456789123")
    assert result == expected


def test_barometer():
    expected = [{"channel": 38, "name": "Barometer", "value": 856.8}]
    result = decode("26732178")
    assert result == expected


def test_gyrometer():
    expected = [
        {
            "channel": 153,
            "name": "Gyrometer",
            "value": {"x": 51.57, "y": 141.84, "z": -272.6},
        }
    ]
    result = decode("9986142537689584")
    assert result == expected


def test_gps():
    expected = [
        {
            "channel": 17,
            "name": "GPS Location",
            "value": {"lat": -33.8678, "long": -63.987, "alt": 10.0},
        }
    ]
    result = decode("1188FAD50AF63C820003E8")
    assert result == expected


def test_combination():
    expected = [
        {"channel": 3, "name": "Temperature Sensor", "value": -12.5},
        {"channel": 7, "name": "Humidity Sensor", "value": 17.0},
    ]
    result = decode("0367FF83076822")
    assert result == expected


def test_combinatio2n():
    expected = [
        {
            "channel": 17,
            "name": "GPS Location",
            "value": {"lat": -33.8678, "long": -63.987, "alt": 10.0},
        },
        {"channel": 17, "name": "Analog Output", "value": -23.0},
    ]
    result = decode("1188FAD50AF63C820003E81103F704")
    assert result == expected
