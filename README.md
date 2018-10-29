# loophole - Polar devices API

[![PyPI](https://img.shields.io/pypi/v/loophole.svg)](https://pypi.python.org/pypi/loophole)
[![Join the chat at https://gitter.im/rsc-dev/loophole](https://badges.gitter.im/rsc-dev/loophole.svg)](https://gitter.im/rsc-dev/loophole?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## About
Python API for Polar devices. Command line interface included.

Tested with:
* A360
* Loop
* M400

## Installation
```sh
pip install loophole
```
or
```sh
python setup.py install
```

## Usage
### CLI
Invoke CLI:
```bash
python __main__.py
```

Type '?' or 'help' to see available commands.
```python
 _|                                _|                  _|
 _|    _|_|      _|_|    _|_|_|    _|_|_|      _|_|    _|    _|_|
 _|  _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|_|_|_|
 _|  _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|
 _|    _|_|      _|_|    _|_|_|    _|    _|    _|_|    _|    _|_|_|
                         _|
                         _|
                                                           ver. 0.3

loophole(no device)>?

Documented commands (type help <topic>):
========================================
connect  disconnect  exit  help  info  list  walk
```


| Command | Description |
| --- | --- |
| connect \<dev_no\> | Connect Polar device. Run 'list' to see available devices. |
| disconnect | Disconnect Polar device. |
| dump \<dest\> | Dump device memory. |
| get \<src\> \<dest\>| Read file from device. |
| exit | Quit. |
| help | List available commands with "help" or detailed help with "help cmd". |
| info | Print connected device info. |
| list | List available Polar devices. |
| walk [path] | Walk file system. Default path is root path (\\). |

### permissions

Note: You need the right permission to access the USB device. Otherwise you will get the error: `The device has no langid`

e.g.: run as root via sudo:

```bash
sudo python __main__.py
```

Or create udev role.

```bash
cat - > /etc/udev/rules.d/40-Polar_A360.rules << EOF
#Polar A360 permissions granted to users group
SUBSYSTEM=="usb", ATTRS{idProduct}=="0008", ATTRS{idVendor}=="0da4", MODE="0660", GROUP="plugdev"
SUBSYSTEMS=="usb-serial", MODE="0660", GROUP="plugdev"
EOF

udevadm control --reload-rules && udevadm trigger
```

### Dependencies
* [protobuf](https://pypi.python.org/pypi/protobuf/3.0.0b2) 
* [pywinusb](https://pypi.python.org/pypi/pywinusb/) (Windows)
* [pyusb] (https://github.com/walac/pyusb) (Linux, > 1.0.0rc1)

#### for debian/ubuntu:
```bash
sudo apt install python-protobuf python-usb
```

## Changelog
[Here](https://github.com/rsc-dev/loophole/blob/master/CHANGELOG.md).

## License
Code is released under [MIT license](https://github.com/rsc-dev/loophole/blob/master/LICENSE.md) © [Radoslaw '[rsc]' Matusiak](https://rm2084.blogspot.com/).
