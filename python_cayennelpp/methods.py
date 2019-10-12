def hex_to_int(hex_string, signed=True):
    """Returns hex_string converted to int. Method can work with signed 2's complement any length.

    :param hex_string: hex string. Example 'DEADBEEF' or 'deadbeef'.
    :param signed: boolean. True or False, indicating if hex signed. Default True
    :return: int representation of hex_string
    """
    if signed:
        # get total number of bits to be able to extract MSB. If MSB=1 number is signed
        bits = len(bytearray.fromhex(hex_string)) * 8
        val = int('0x' + hex_string, 16)
        # get MSB and if MSB = 1 (means number is signed) - take 2's compliment
        if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)  # compute negative value
        return val
    else:
        return int(hex_string, 16)


def digital_input_output_presence_illuminance(data):
    """Digital Output/Input/Presence/Illuminance | Data Resolution per bit = 1, Unsigned
     All these values are the same in decoding.

    :param data: hex string of sensor value
    :return: int decoded value
    """
    return hex_to_int(data, False)


def analog_input_output(data):
    """Analog Input/Output | Data Resolution per bit = 0.01 Signed

    :param data: hex string of sensor value
    :return: int decoded value
    """
    return hex_to_int(data) / 100.0


def temperature(data):
    """Temperature | Data Resolution per bit = 0.1 degC Signed MSB

    :param data: hex string of sensor value
    :return: int decoded value
    """
    return hex_to_int(data) / 10.0


def humidity(data):
    """Humidity | Data Resolution per bit = 0.5 % Unsigned

    :param data: hex string of sensor value
    :return: int decoded value
    """
    return hex_to_int(data, False) / 2.0


def accelerometer(data):
    """Accelerometer | 	Data Resolution per bit = 0.001 G Signed MSB per axis
    Data Size: 6 bytes. x axis value = 2 bytes, y axis value = 2 bytes, z axis value = 2 bytes.
    Example: 04 D2 FB 2E 00 00 --> 04D2 - x, FB2E - y, 0000 - z.

    :param data: hex string of sensor value
    :return: dictionary of x,y,z axis as keys and their values
    """
    return {'x': hex_to_int(data[:4]) / 1000.0, 'y': hex_to_int(data[4:8]) / 1000.0, 'z': hex_to_int(data[8:]) / 1000.0}


def barometer(data):
    """Barometer | Data Resolution per bit = 0.1 hPa Unsigned MSB

    :param data: hex string of sensor value
    :return: int decoded value
    """
    return hex_to_int(data, False) / 10.0


def gyrometer(data):
    """Gyrometer | 	Data Resolution per bit = 0.01 deg/s Signed MSB per axis
    Data Size: 6 bytes. x axis value = 2 bytes, y axis value = 2 bytes, z axis value = 2 bytes.
    Example: 04 D2 FB 2E 00 00 --> 04D2 - x, FB2E - y, 0000 - z.

    :param data: hex string of sensor value
    :return: dictionary of x,y,z axis as keys and their values
    """
    return {'x': hex_to_int(data[:4]) / 100.0, 'y': hex_to_int(data[4:8]) / 100.0, 'z': hex_to_int(data[8:]) / 100.0}


def gps_location(data):
    """GPS Location | Data Resolution per bit below

    * Latitude : 0.0001 deg Signed MSB
    * Longitude : 0.0001 deg Signed MSB
    * Altitude : 0.01 meter Signed MSB

    :param data: hex string of sensor value
    :return: dictionary of lat,long,alt as key and their values
    """
    return {'lat': hex_to_int(data[:6]) / 10000.0, 'long': hex_to_int(data[6:12]) / 10000.0, 'alt': hex_to_int(data[12:]) / 100.0}


hex_library = {
    "00": {
        "name": "Digital Input",
        "size": 2,
        "action": digital_input_output_presence_illuminance
    },
    "01": {
        "name": "Digital Output",
        "size": 2,
        "action": digital_input_output_presence_illuminance
    },
    "02": {
        "name": "Analog Input",
        "size": 4,
        "action": analog_input_output
    },
    "03": {
        "name": "Analog Output",
        "size": 4,
        "action": analog_input_output
    },
    "65": {
        "name": "Illuminance Sensor",
        "size": 4,
        "action": digital_input_output_presence_illuminance
    },
    "66": {
        "name": "Presence Sensor",
        "size": 2,
        "action": digital_input_output_presence_illuminance
    },
    "67": {
        "name": "Temperature Sensor",
        "size": 4,
        "action": temperature
    },
    "68": {
        "name": "Humidity Sensor",
        "size": 2,
        "action": humidity
    },
    "71": {
        "name": "Accelerometer",
        "size": 12,
        "action": accelerometer
    },
    "73": {
        "name": "Barometer",
        "size": 4,
        "action": barometer
    },
    "86": {
        "name": "Gyrometer",
        "size": 12,
        "action": gyrometer
    },
    "88": {
        "name": "GPS Location",
        "size": 18,
        "action": gps_location
    }
}
