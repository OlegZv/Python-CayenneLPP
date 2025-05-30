"""Main decoder for CayenneLPP payload format."""

import logging
from typing import Any, Dict, List
from python_cayennelpp.methods import hex_library

logger = logging.getLogger(__name__)


def decode(payload: str):
    """Decoder for CayenneLPP payload format. The Cayenne Low Power Payload (LPP)
    provides a convenient and easy way to send data over LPWAN networks such as LoRaWAN.
    More information on the payload format
    https://github.com/myDevicesIoT/cayenne-docs/blob/master/docs/LORA.md

    Example: decode("067104D2FB2E0000")

    :param payload: represents device payload in hex string, e.g. 03670110056700FF
    :return: list of sensors. Each item(sensor) in this list represented by
    a dictionary of channel,name,value.
    """
    # check provided type
    if not isinstance(payload, str):
        raise TypeError(
            f"Payload must be hex encoded string. Provided type: {type(payload)}"
        )
    # parsing payload using hex_library.
    # variable pointer represents caret in line to cut. result is returned result
    result: List[Dict[str, Any]] = []
    pointer = 0
    try:
        while pointer < len(payload):
            sensor = {"channel": int(payload[pointer : pointer + 2], 16), "name": ""}
            pointer += 2
            try:
                sensor["name"], payload_size, action = (
                    hex_library[payload[pointer : pointer + 2]]["name"],
                    hex_library[payload[pointer : pointer + 2]]["size"],
                    hex_library[payload[pointer : pointer + 2]]["action"],
                )
            except KeyError:
                logging.warning(
                    "Decoding failed or incomplete. Unrecognized sensor type: %s",
                    payload[pointer : pointer + 2],
                )
                return result
            pointer += 2
            if len(payload) < pointer + payload_size:
                raise ValueError(
                    f"The length on the payload {payload} is {len(payload)} "
                    f"doesn't correspond to expected {pointer + payload_size}"
                )
            sensor["value"] = action(payload[pointer : pointer + payload_size])
            pointer += payload_size
            result.append(sensor)
        return result
    except Exception:
        logging.warning(
            "Decoding failed for unknown reason. Intermediate result is of decoding %s: %s",
            payload,
            result,
        )
        raise
