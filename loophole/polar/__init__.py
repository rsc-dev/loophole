#!/usr/bin/env python

__author__      = 'Radoslaw Matusiak'
__copyright__   = 'Copyright (c) 2016 Radoslaw Matusiak'
__license__     = 'MIT'
__version__     = '0.4'

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
        return Protocol.pb_pftp_operation(path, action=0x00)
    # end-of-method read

    @staticmethod
    def delete(path):
        """
        Create delete path message.

        :param path: Path to delete.
        :return: Delete path message bytes array.
        """
        return Protocol.pb_pftp_operation(path, action=0x03)
    # end-of-method delete

    @staticmethod
    def put(path, data):
        """
        Not working yet.

        :param path:
        :param data:
        :return:
        """
        raise RuntimeError()

        cmds = []

        length = 64

        p = []
        p.append(0x01)

        total = len(path) + len(data)
        if total > 62:
            p.append(0xf9)
        else:
            p.append(total + 8 << 2)

        p.append(0x00)
        p.append(len(path)+4)
        p.append(0x00)
        p.append(0x08)
        p.append(0x01)
        p.append(0x12)
        p.append(len(path))
        for i in path:
                p.append(ord(i))

        for i in data[0:(length-9-len(path))]:
            p.append(ord(i))

        p = p + [0x00] * (64-len(p))

        cmds.append(p)

        j = 1
        for i in xrange(length-9-len(path), len(data), 61):
            cmd = [0x01]
            subdata = data[i:i+61]

            if len(subdata) == 61:
                cmd.append(0xf9)
            else:
                cmd.append((len(subdata) + 2) << 2)

            cmd.append(j)

            for b in subdata:
                cmd.append(ord(b))

            cmd = cmd + [0x00] * (64-len(cmd))
            cmds.append(cmd)
            j += 1


        return cmds
    # end-of-method put

    @staticmethod
    def pb_pftp_operation(path, action):
        """
        Create PFTP operation message.

        :param path: Message path.
        :param action: Action enum value. (GET=0x00, DELETE=0x03)
        :return: Message bytes array.
        """
        a = []
        a.append(0x01)
        a.append((len(path)+8) << 2)
        a.append(0x00)
        a.append(len(path)+4)
        a.append(0x00)
        a.append(0x08)
        a.append(action)
        a.append(0x12)
        a.append(len(path))
        for i in path:
                a.append(ord(i))

        a = a + [0x00] * (64-len(a))
        return a
    # end-of-method pb_pftp_operation

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

    UsbDevice = namedtuple('UsbDevice', ['vendor_id', 'product_id', 'serial_number', 'product_name'])

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
            """
            Initialize USB communication.

            :return: Nothing.
            """
            if self.device is None:
                raise RuntimeError('USB device not connected!')

            self.device.open()
            self.device.set_raw_data_handler(self.data_handler)

            # If this line is a magic for you - please read https://en.wikipedia.org/wiki/Human_interface_device
            self.out_report = self.device.find_output_reports()[0]

            self.response = None
        # end-of-method init

        def list(self, vendor_id):
            """
            List all USB devices for given vendor id.

            :param vendor_id: Vendor id.
            :return: List of available devices.
            """
            all_hid_devs = self.hid.find_all_hid_devices()
            devices = filter(lambda x: x.vendor_id == vendor_id, all_hid_devs)
            return devices
        # end-of-method list

        def get_info(self, usb_device):
            """
            Get infor for given USB device.

            :param usb_device: USB device.
            :return: Array with USB info.
            """
            info = dict()
            info['manufacturer'] = usb_device.vendor_name
            info['product_name'] = usb_device.product_name
            info['serial_number'] = usb_device.serial_number
            info['vendor_id'] = '0x%04X' % usb_device.vendor_id
            info['product_id'] = '0x%04X' % usb_device.product_id
            return info
        # end-of-method get_info

        def open(self, usb_device):
            """
            Open USB device.

            :param usb_device: USB device to open.
            :return: Nothing.
            """
            f = self.hid.HidDeviceFilter(vendor_id=usb_device.vendor_id, product_id=usb_device.product_id)

            devs = f.get_devices()
            for d in devs:
                if d.serial_number == usb_device.serial_number:
                    self.device = d
                    self.init()
        # end-of-method open

        def close(self):
            """
            Close connected device.

            :return: Nothing.
            """
            self.device.close()
        # end-of-method close

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

            return resp
        # end-of-method data

        pass
    # end-of-class Usb.WinUsb

    class LinuxUsb():

        def __send_wait(self, request, timeout):
            """
            This is internal method used for HOST->DEVICE communication.
            This method only sends raw request and returns raw response.

            :param request: Raw request to send. Array of byte values expected.
            :param timeout: Timeout in milliseconds.
            :return: Device raw response (array of byte values).
            """
            response = None
            self.ep_out_0.write(request, timeout)
            response = self.ep_in_0.read(64, timeout)

            return response
        # end-of-method send_wait

        def __init__(self):
            """
            Constructor.

            :return: Instance object.
            """
            import usb as usb
            import usb.core as usb_core

            self.usb = usb
            self.usb_core = usb_core
            self.ep_out_0 = None
            self.ep_in_0 = None
            self.usb_device = None
        # end-of-method __init__

        def list(self, vendor_id):
            """
            List all USB devices for given vendor id.

            :param vendor_id: Vendor id.
            :return: List of available devices.
            """
            devices = self.usb_core.find(find_all=True)
            return filter(lambda x: x.idVendor == vendor_id, devices)
        # end-of-method list

        def get_info(self, usb_device):
            """
            Get infor for given USB device.

            :param usb_device: USB device.
            :return: Array with USB info.
            """
            info = dict()
            info['manufacturer'] = self.usb.util.get_string(usb_device, usb_device.iManufacturer)
            info['product_name'] = self.usb.util.get_string(usb_device, usb_device.iProduct)
            info['serial_number'] = self.usb.util.get_string(usb_device, usb_device.iSerialNumber)
            info['vendor_id'] = "0x%04X" % usb_device.idVendor
            info['product_id'] = "0x%04X" % usb_device.idProduct
            return info
        # end-of-method get_info

        def open(self, usb_device):
            """
            Open USB device.

            :param usb_device: USB device to open.
            :return: Nothing.
            """
            if usb_device.is_kernel_driver_active(0):
                usb_device.detach_kernel_driver(0)
            usb_device.set_configuration()
            cfg = usb_device.get_active_configuration()
            intf = cfg[(0,0)]
            self.ep_out_0 = self.usb.util.find_descriptor(
                intf, 
                custom_match = \
                    lambda e: \
                        self.usb.util.endpoint_direction(e.bEndpointAddress) == \
                        self.usb.util.ENDPOINT_OUT)
            assert self.ep_out_0 is not None
            self.ep_in_0 = self.usb.util.find_descriptor(
                intf,
                custom_match = \
                    lambda e: \
                        self.usb.util.endpoint_direction(e.bEndpointAddress) == \
                        self.usb.util.ENDPOINT_IN)
            assert self.ep_in_0 is not None

            self.usb_device = usb_device
        # end-of-method open

        def close(self):
            """
            Close connected device.

            :return: Nothing.
            """
            self.usb.util.dispose_resources(self.usb_device)
        # end-of-method close

        def send(self, request, timeout):
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
                ack = Protocol.ack_packet(pckt_no)
                data = self.__send_wait(ack, timeout)

            return resp
        # end-of-method send

        pass
    # end-of-class Usb.LinuxUsb

    def __init__(self):
        """
        Constructor.

        :return: Instance object.
        """
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
    # end-of-method list_devices

    def get_info(self, usb_device):
        """
        Returns info of the given USB device

        :return: Dictionary with USB info
        """
        return self.usb.get_info(usb_device)

    def open(self, usb_device):
        """
        Connect USB device.

        :param usb_device: UsbDevice instance for device to connect.
        :return: Nothing.
        """
        self.usb.open(usb_device)
    # end-of-method open

    def close(self):
        """
        Close USB device.
        """
        self.usb.close()
    # end-of-method close

    def send(self, request, timeout=5000):
        """
        Send

        :param request: UsbDevice instance for device to connect.
        :param timeout: Timeout value.
        :return: Nothing.
        """
        resp = self.usb.send(request, timeout)
        return resp[2:]
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

    def __init__(self, usb_device):
        """
        Constructor.

        :param usb: USB instance connected to Polar device.
        :return: Instance object.
        """
        self.usb_device = usb_device
        self.usb = Usb()
    # end-of-method __init__

    @staticmethod
    def list():
        """
        List all Polar devices connected to the computer.

        :return List of all connected Polar devices.
        """
        usb = Usb()
        return usb.list_devices()
    # end-of-method list

    @staticmethod    
    def get_info(usb_device):
        """
        Reads USB device info from the given usb device.

        :return: Device info dictionary.
        """
        usb = Usb()
        return usb.get_info(usb_device)
    # end-of-method get_info

    def open(self):
        """
        Connects to the device
        """
        self.usb.open(self.usb_device)

    def close(self):
        """
        Closes the device
        """
        self.usb.close()

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

    def delete(self, path):
        """
        Delete path from device.

        :param path: File's path.
        :return: Device response.
        """
        resp = self.usb.send(request=Protocol.delete(path))
        return resp
    # end-of-method delete

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

