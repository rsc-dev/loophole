#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.3'

from collections import namedtuple
import os
import time

import polar.pb.pftp_response_pb2 as pb_resp


class Protocol():
    """ Device protocol util class. """

    @staticmethod
    def directory(resp):
        """
        Parse device response as directory response.

        :param resp: Device response.
        :return: Directory object.
        """
        d = pb_resp.PbPFtpDirectory()
        d.ParseFromString(resp)
        return d
    # end-of-method directory

    @staticmethod
    def read(path):
        """
        Create read path message.

        :param path: Path to read.
        :return: Read path message bytes array.
        """
        a = []
        a.append(0x01)
        a.append((len(path)+8) << 2)
        a.append(0x00)
        a.append(len(path)+4)
        a.append(0x00)
        a.append(0x08)
        a.append(0x00)
        a.append(0x12)
        a.append(len(path))
        for i in path:
                a.append(ord(i))

        a = a + [0x00] * (64-len(a))
        return a
    # end-of-method read

    @staticmethod
    def ack_packet(packet_no):
        """
        Create response message byte array to acknowledge incoming packet.

        :param packet_no: Number of packet to ack.
        :return: Ack packet message bytes array.
        """
        return [01, 05, packet_no] + [0] * 61
    # end-of-method ack_packet

    pass
# end-of-class Protocol


class Usb():
    """
    USB interface to Polar devices.
    Wraps Windows and Linux classes.
    """

    UsbDevice = namedtuple('UsbDevice', ['vendor_id', 'product_id', 'serial_number'])

    class WinUsb():
        """
        PyWinUSB wrapper class.
        Provides Windows USB support.
        """

        def __init__(self):
            """
            Constructor.

            :return: Instance object.
            """
            import pywinusb.hid as hid

            self.hid = hid
            self.device = None
        # end-of-method __init__

        def __send_wait(self, request, timeout=2000):
            """
            This is internal method used for HOST->DEVICE communication.
            This method only sends raw request and returns raw response.

            :param request: Raw request to send. Array of byte values expected.
            :param timeout: Timeout in milliseconds.
            :return: Device raw response (array of byte values).
            """
            self.response = None

            self.out_report.set_raw_data(request)
            self.out_report.send()

            t = 0
            while self.response is None:
                time.sleep(0.05)
                t += 50

                if t >= timeout:
                    break

            return self.response
        # end-of-method send_wait

        def close(self):
            """
            Close connected device.

            :return: Nothing.
            """
            self.device.close()
        # end-of-method close

        def connect(self, usb_device):
            """
            Connect USB device.

            :param usb_device: UsbDevice instance for device to connect.
            :return:
            """
            f = self.hid.HidDeviceFilter(vendor_id=usb_device.vendor_id, product_id=usb_device.product_id)

            devs = f.get_devices()
            for d in devs:
                if d.serial_number == usb_device.serial_number:
                    self.device = d
                    self.init()

            return self.device
        # end-of-method connect

        def data_handler(self, response):
            """
            Simple USB->HOST data handler.

            :param response: Response from USB HID device.
            :return: Nothing.
            """
            self.response = response
            return None
        # end-of-method data_handler

        def init(self):
            if self.device is None:
                raise RuntimeError('USB device not connected!')

            self.device.open()
            self.device.set_raw_data_handler(self.data_handler)

            # If this line is a magic for you - please read https://en.wikipedia.org/wiki/Human_interface_device
            self.out_report = self.device.find_output_reports()[0]

            self.response = None
        # end-of-method init

        def list(self, vendor_id):
            all_hid_devs = self.hid.find_all_hid_devices()
            devices = filter(lambda x: x.vendor_id == vendor_id, all_hid_devs)
            return [Usb.UsbDevice(d.vendor_id, d.product_id, d.serial_number) for d in devices]
        # end-of-method list

        def send(self, request, timeout=2000):
            """
            Send raw data to device and read response.

            :param request: Request to send.
            :param timeout: Max timeout in milliseconds. Default value: 2000 ms.
            :return: Response from device.
            """
            resp = []

            data = self.__send_wait(request, timeout)
            while data is not None:
                if data[1] & 3 == 0:
                    length = data[1] >> 2
                    resp += data[3:length+1]
                    break
                resp += data[3:]
                pckt_no = data[2]
                data = self.__send_wait(Protocol.ack_packet(pckt_no), timeout)

            return resp[2:]
        # end-of-method data

        pass
    # end-of-class Usb.WinUsb

    class LinuxUsb():

        def __init__(self):
            import usb as usb
            import usb.core as usb_core

            self.usb = usb
            self.usb_core = usb_core
        # end-of-method __init__

        def list(self, vendor_id):
            devices = self.usb_core.find(idVendor=vendor_id)
            return [Usb.UsbDevice(d.idVendor, d.idProduct, d.serial_number) for d in devices]
        # end-of-method list

        pass
    # end-of-class Usb.LinuxUsb

    def __init__(self):
        if os.name == 'nt':
            self.usb = Usb.WinUsb()
        elif os.name == 'posix':
            self.usb = Usb.LinuxUsb()
        else:
            raise NotImplementedError('Unknown operating system. Usb not supported.')
    # end-of-method __init__

    def list_devices(self):
        """
        List available Polar device.
        :return: List of UsbDevice instances for all USB plugged Polar devices.
        """
        return self.usb.list(vendor_id=Device.VENDOR_ID)
    # end-of-method list

    def close(self):
        """
        Close USB device.
        """
        self.usb.close()
    # end-of-method close

    def connect(self, usb_device):
        """
        Connect USB device.

        :param usb_device: UsbDevice instance for device to connect.
        :return: Nothing.
        """
        self.usb.connect(usb_device)
    # end-of-method get_device

    def send(self, request, timeout=2000):
        """
        Send

        :param request: UsbDevice instance for device to connect.
        :param timeout: Timeout value.
        :return: Nothing.
        """
        return self.usb.send(request, timeout)
    # end-of-method send

    pass
# end-of-class Usb


class Device():
    """
    Polar devices class. Works on Windows.

    Note: Tested with Polar Loop.
    """

    VENDOR_ID   = 0x0DA4  # Polar Electro Oy
    PRODUCT_ID  = {0x0008: 'Loop'}

    SEP = '/'

    def __init__(self, usb):
        """
        Constructor.

        :param usb: USB instance connected to Polar device.
        :return: Instance object.
        """
        self.usb = usb
    # end-of-method __init__

    def get_info(self):
        """
        Read USB device info.

        :return: Device info dictionary.
        """
        info = dict()
        info['vendor_name']     = self.device.vendor_name
        info['version_number']  = self.device.version_number
        info['vendor_id']       = self.device.vendor_id
        info['serial_number']   = self.device.serial_number
        info['product_name']    = self.device.product_name
        info['product_id']      = self.device.product_id
        info['device_path']     = self.device.device_path

        return info
    # end-of-method get_info

    def walk(self, path):
        """
        Recursively walk given path.

        :param path: Path to walk.
        :return: Dictionary of files and subfolders.
        """
        ret = {}
        dirs = [path]

        while True:
            try:
                current_dir = dirs.pop()
                d = self.list_dir(current_dir)

                if d is not None:
                    ret[current_dir] = d

                    for e in d.entries:
                        if e.name.endswith('/'):
                            dirs.append('{}{}'.format(current_dir, e.name))
            except IndexError:
                break

        return ret
    # end-of-method walk

    def list_dir(self, path):
        """
        List given directory.

        :param path: Path to list.
        :return: Directory object.
        """
        try:
            resp = self.usb.send(request=Protocol.read(path))

            if resp is not None and len(resp) > 0:
                resp = ''.join(chr(c) for c in resp)
                d = Protocol.directory(resp)
                return d
        except:
            print 'Path {} failed!'.format(path)
    # end-of-method list_dir

    def read_file(self, path):
        """
        Read file from device.

        :param path: File's path.
        :return: Bytes list.
        """
        resp = self.usb.send(request=Protocol.read(path))
        return resp
    # end-of-method read_file

    @staticmethod
    def get_product_by_id(id):
        """
        Returns product name by given product ID.

        :param id: Product ID numeric value.
        :return: Product name.
        """

        if id in Device.PRODUCT_ID.keys():
            return Device.PRODUCT_ID[id]
        else:
            return 'unknown'
    # end-of-method get_product_by_id

    pass
# end-of-class Device


if __name__ == '__main__':
    pass