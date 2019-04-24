from python_cayennelpp.methods import hex_library


def decode(payload):
    """Decoder for CayenneLPP payload format. The Cayenne Low Power Payload (LPP) provides a convenient and easy way to send data over LPWAN networks such as LoRaWAN.
    More information on the payload format https://github.com/myDevicesIoT/cayenne-docs/blob/master/docs/LORA.md

    Example: decode("067104D2FB2E0000")

    :param payload: represents device payload in hex, e.g. 03670110056700FF
    :return: list of sensors. Each item(sensor) in this list represented by dictionary of channel,name,value.
    """
    # parsing payload using hex_library. variable pointer represents caret in line to cut. result is returned result
    result = []
    pointer = 0
    try:
        while pointer < len(payload):
            sensor = {'channel': int(payload[pointer:pointer + 2], 16)}
            pointer += 2
            sensor['name'], payload_size, action = hex_library[payload[pointer:pointer + 2]]['name'],\
                                                   hex_library[payload[pointer:pointer + 2]]['size'],\
                                                   hex_library[payload[pointer:pointer + 2]]['action']
            pointer += 2
            sensor['value'] = action(payload[pointer:pointer + payload_size])
            pointer += payload_size
            result.append(sensor)
        return result
    except:
        print('[ERROR] Something went wrong during payload decoding.')
        return result


print(decode('03670110056700FF'))
