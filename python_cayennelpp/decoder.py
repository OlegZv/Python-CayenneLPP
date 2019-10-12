from python_cayennelpp.methods import hex_library


def decode(payload):
    """Decoder for CayenneLPP payload format. The Cayenne Low Power Payload (LPP) provides a convenient and easy way to send data over LPWAN networks such as LoRaWAN.
    More information on the payload format https://github.com/myDevicesIoT/cayenne-docs/blob/master/docs/LORA.md

    Example: decode("067104D2FB2E0000")

    :param payload: represents device payload in hex string, e.g. 03670110056700FF
    :return: list of sensors. Each item(sensor) in this list represented by dictionary of channel,name,value.
    """
    # check provided type
    if type(payload) is not str:
        raise TypeError("Payload must be hex encoded string. Provided type: {}".format(type(payload)))
    # parsing payload using hex_library. variable pointer represents caret in line to cut. result is returned result
    result = []
    pointer = 0
    try:
        while pointer < len(payload):
            sensor = {'channel': int(payload[pointer:pointer + 2], 16)}
            pointer += 2
            try:
                sensor['name'], payload_size, action = hex_library[payload[pointer:pointer + 2]]['name'],\
                    hex_library[payload[pointer:pointer + 2]]['size'],\
                    hex_library[payload[pointer:pointer + 2]]['action']
            except KeyError:
                print('[ERROR]: Decoding failed or incomplete. Unrecognized sensor type: {}'.format(payload[pointer:pointer + 2]))
                return result
            pointer += 2
            if len(payload) < pointer + payload_size:
                raise ValueError("The length on the payload {} is {} doesn't correspond to expected {}".format(payload, len(payload), pointer + payload_size))
            sensor['value'] = action(payload[pointer:pointer + payload_size])
            pointer += payload_size
            result.append(sensor)
        return result
    except Exception:
        print('[ERROR]: Decoding failed. Intermediate result is of decoding {}: {}'.format(payload, result))
        raise
