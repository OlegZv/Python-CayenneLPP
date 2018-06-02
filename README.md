# Python-CayenneLPP
## Introduction
Open source library for python to decode CayenneLPP format payload.
The Cayenne Low Power Payload (LPP) provides a convenient and easy way to send data over LPWAN networks such as LoRaWAN.
More details on CayenneLPP payload: https://github.com/myDevicesIoT/cayenne-docs

## Usage
To decode payload simply use method decode() from this package

```python
>>>from python_cayennelpp.decoder import decode
>>>print(decode('03670110056700FF'))
[{'channel': 3, 'name': 'Temperature Sensor', 'value': 27.2}, {'channel': 5, 'name': 'Temperature Sensor', 'value': 25.5}]

```
