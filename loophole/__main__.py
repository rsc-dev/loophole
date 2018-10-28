#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.5'


import cmd
import functools
import os
import sys

from polar import Device
from polar.pb import device_pb2 as pb_device

__INTRO = """

 _|                                _|                  _|
 _|    _|_|      _|_|    _|_|_|    _|_|_|      _|_|    _|    _|_|
 _|  _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|_|_|_|
 _|  _|    _|  _|    _|  _|    _|  _|    _|  _|    _|  _|  _|
 _|    _|_|      _|_|    _|_|_|    _|    _|    _|_|    _|    _|_|_|
                         _|
                         _|
                                                           ver. {}
"""


def check_if_device_is_connected(f):
    """
    Decorator. Checks if device is connected before invoking function.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if args[0].device is not None:
            return f(*args, **kwargs)
        else:
            print '[!] Device disconnected.'
            print
    return wrapper


class LoopholeCli(cmd.Cmd):
    """ Loophole command line interface class. """

    __PROMPT = 'loophole({})>'

    def __init__(self):
        """Constructor.
        """
        cmd.Cmd.__init__(self)
        self.prompt = LoopholeCli.__PROMPT.format('no device')
        self.device = None
    # end-of-method __init__

    def do_exit(self, _):
        """Quit.
Usage: exit
        """
        if self.device is not None:
            self.device.close()
        sys.exit(0)
    # end-of-method do_exit

    def do_EOF(self, _):
        """Quit. handles EOF"""
        self.do_exit(_)
    # end-of-method do_EOF

    def do_list(self, _):
        """List available Polar devices.
Usage: list
        """
        devs = Device.list()

        if len(devs) > 0:
            for i, dev in enumerate(devs):
                try:
                    info = Device.get_info(dev)
                except ValueError as err:
                    print "Device no: %i" % i
                    print "Device info:"
                    print dev
                    print "-"*79
                    if 'langid' in err.message:
                        raise ValueError(
                            (
                                "Can't get device info. Origin Error: %s\n"
                                "Maybe this is a permission issue.\n"
                                "Please read section 'permission' in README ;)"
                            ) % err
                        )
                    raise # raise origin error

                print '{} - {} ({})'.format(i, info['product_name'], info['serial_number'])
        else:
            print '[!] No Polar devices found!'

        print
    # end-of-method do_list

    def do_connect(self, dev_no):
        """Connect Polar device. Run 'list' to see available devices.
Usage: connect <device_no>
        """
        try:
            dev_no = int(dev_no)
        except ValueError:
            print '[!] You need to specify the device number. Run \'list\' to see available devices.'
            print
            return

        try:
            devs = Device.list()
            dev = devs[dev_no]
            serial = Device.get_info(dev)['serial_number']

            self.prompt = LoopholeCli.__PROMPT.format(serial)
            self.device = Device(dev)
            self.device.open()

            print '[+] Device connected.'
            print
        except IndexError:
            print '[!] Device not found or failed to open it. Run \'list\' to see available devices.'
            print
    # end-of-method do_connect

    @check_if_device_is_connected
    def do_disconnect(self, _):
        """Disconnect Polar device.
        """
        self.device.close()
        self.device = None
        self.prompt = LoopholeCli.__PROMPT.format('no device')
        print '[+] Device disconnected.'
        print
    # end-of-method do_disconnect

    @check_if_device_is_connected
    def do_get(self, line):
        """Read file from device and store in under local_path.
Usage: get <device_path> <local_path>
        """
        try:
            src, dest = line.strip().split()

            data = self.device.read_file(src)
            with open(dest, 'wb') as outfile:
                outfile.write(bytearray(data))

            print '[+] File \'{}\' saved to \'{}\''.format(src, dest)
            print
        except ValueError:
            print '[!] Invalid command usage.'
            print '[!] Usage: get <source> <destination>'
            print
    # end-of-method do_get

    @check_if_device_is_connected
    def do_delete(self, line):
        """Delete file from device.
Usage: delete <device_path>
        """
        path = line.strip()
        _ = self.device.delete(path)
    # end-of-method do_delete

    @check_if_device_is_connected
    def do_dump(self, path):
        """Dump device memory. Path is local folder to store dump.
Usage: dump <local_path>
        """
        print '[+] Reading files tree...'
        dev_map = self.device.walk(self.device.SEP)

        for directory in dev_map.keys():
            fixed_directory = directory.replace(self.device.SEP, os.sep)
            full_path = os.path.abspath(os.path.join(path, fixed_directory[1:]))

            if not os.path.exists(full_path):
                os.makedirs(full_path)

            d = dev_map[directory]
            files = [e for e in d.entries if not e.name.endswith('/')]
            for file in files:
                with open(os.path.join(full_path, file.name), 'wb') as fh:
                    print '[+] Dumping {}{}'.format(directory, file.name)
                    data = self.device.read_file('{}{}'.format(directory, file.name))
                    fh.write(bytearray(data))

        print '[+] Device memory dumped.'
        print
    # end-of-method do_dump

    @check_if_device_is_connected
    def do_info(self, _):
        """Print connected device info.
Usage: info
        """
        info = Device.get_info(self.device.usb_device)
        print '{:>20s} - {}'.format('Manufacturer', info['manufacturer'])
        print '{:>20s} - {}'.format('Product name', info['product_name'])
        print '{:>20s} - {}'.format('Vendor ID', info['vendor_id'])
        print '{:>20s} - {}'.format('Product ID', info['product_id'])
        print '{:>20s} - {}'.format('Serial number', info['serial_number'])

        try:
            data = self.device.read_file('/DEVICE.BPB')
            resp = ''.join(chr(c) for c in data)
            d = pb_device.PbDeviceInfo()
            d.ParseFromString(resp)
            bootloader_version = '{}.{}.{}'.format(d.bootloader_version.major, d.bootloader_version.minor, d.bootloader_version.patch)
            print '{:>20s} - {}'.format('Bootloader version', bootloader_version)
            platform_version = '{}.{}.{}'.format(d.platform_version.major, d.platform_version.minor, d.platform_version.patch)
            print '{:>20s} - {}'.format('Platform version', platform_version)
            device_version = '{}.{}.{}'.format(d.device_version.major, d.device_version.minor, d.device_version.patch)
            print '{:>20s} - {}'.format('Device version', device_version)
            print '{:>20s} - {}'.format('SVN revision', d.svn_rev)
            print '{:>20s} - {}'.format('Hardware code', d.hardware_code)
            print '{:>20s} - {}'.format('Color', d.product_color)
            print '{:>20s} - {}'.format('Product design', d.product_design)

        except:
            print '[!] Failed to get extended info.'

        print ' '
    # end-of-method do_info

    @check_if_device_is_connected
    def do_fuzz(self, _):
        import polar
        num = _.strip()

        if len(num) > 0:
            num = int(num)
            resp = self.device.send_raw([0x01, num] + [0x00] * 62)
            print 'req: {} '.format(num),
            if resp:
                print 'err code: {}'.format(polar.PFTP_ERROR[resp[0]])

            return

        for i in xrange(256):
            #raw_input('Sending [{}]...<press enter>'.format(i))
            if (i & 0x03) == 2:
                continue

            if i in [3, 251, 252]:
                continue

            resp = self.device.send_raw([0x01, i] + [0x00] * 62)


            print 'resp: {} '.format(i),
            if resp:
                print 'err code: {}'.format(polar.PFTP_ERROR[resp[0]])
            else:
                print
    # end-of-method do_fuzz

    @check_if_device_is_connected
    def do_put_file(self, line):
        path, filename = line.split()
        self.device.put_file(path.strip(), filename.strip())
    # end-of-method do_put_file

    @check_if_device_is_connected
    def do_walk(self, path):
        """Walk file system. Default device_path is device root folder.
Usage: walk [device_path]
        """
        if not path.endswith('/'):
            path += '/'

        fs = self.device.walk(path)
        keyz = fs.keys()
        keyz.sort()

        for k in keyz:
            print k
            d = fs[k]
            files = [e for e in d.entries if not e.name.endswith('/')]
            files.sort()
            for f in files:
                print '{}{} ({} bytes)'.format(k, f.name, f.size)

        print
    # end-of-method do_walk

    pass
# end-of-class Loophole


def main():
    cli = LoopholeCli()
    cli.cmdloop(__INTRO.format(__version__))
# end-of-function main


##
#  Entry point
if __name__ == '__main__':
    main()

