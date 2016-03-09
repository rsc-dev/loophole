# loophole - Polar devices API

## About
Python API for Polar devices. Command line interface included.

Tested with:
* A360
* Loop
* M400

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


### Dependencies
* [protobuf](https://pypi.python.org/pypi/protobuf/3.0.0b2) 
* [pywinusb](https://pypi.python.org/pypi/pywinusb/) (Windows)
* [pyusb] (https://github.com/walac/pyusb) (Linux, > 1.0.0rc1)

## Changelog
[Here](https://github.com/rsc-dev/loophole/blob/master/CHANGELOG.md).

## License
Code is released under [MIT license](https://github.com/rsc-dev/loophole/blob/master/LICENSE.md) © [Radoslaw '[rsc]' Matusiak](https://rm2084.blogspot.com/).
