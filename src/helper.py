import socket
import struct


class ICMP:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    def create_packet(self, id, data):
        # calculate checksum from clear header
        header = struct.pack('bbhhh', 8, 0, 0, id, 1)
        header = struct.pack('bbHHh', 8, 0, socket.htons(self.checksum(header + bytes(data, 'utf-8'))), id, 1)
        return header + bytes(data, 'utf-8')

    def send_data(self, data):
        self.sock.sendto(self.create_packet(1, data), (self.ip, self.port))

    def checksum(self, data):
        """ calculate network checksum out of given data """
        if len(data) % 2 != 0:
            data += b'\x00'

        chksum = 0
        for i in range(0, len(data), 2):
            if i + 1 >= len(data):
                chksum += data[i] & 0xFF
            else:
                w = ((data[i] << 8) & 0xFF00) + (data[i + 1] & 0xFF)
                chksum += w

        while (chksum >> 16) > 0:
            chksum = (chksum & 0xFFFF) + (chksum >> 16)

        return ~chksum & 0xFFFF
