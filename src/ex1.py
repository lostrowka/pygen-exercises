import socket
import struct


class ARP:
    def __init__(self, iface):
        """Class for maintaining ARP requests

        Args:
            iface: interface on which we want to send ARP request

        """
        self.iface = iface
        self.sock = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 3)
        # TODO: Bind new socket
        # Find EtherType @ https://en.wikipedia.org/wiki/EtherType
        # self.sock.bind(("<iface>", "<EtherType>"))

    def send_data(self, dest_ip: str):
        # TODO: Write source interface MAC address in appropriate form
        # Use byte-strings e.g. b"\xc0\x25\xe9\x13\xef\xfc"
        # Bonus points: get addr dynamically
        source_mac = b"<insert mac address here>"
        dest_mac = b"\x00\x00\x00\x00\x00\x00"

        # TODO: Insert src ip address as string and convert it to bytes (hint: check family of socket.inet_ methods)
        # Bonus points: get addr dynamically
        src_ip = "<insert src ip address here and convert it to bytes>"
        # TODO: Convert dest_ip to bytes as well
        dst_ip = dest_ip

        # --- short struct reference ---
        # struct.pack(format, args...)
        # ! - network format (big-endian)
        # H - 2 bytes
        # B - 1 byte
        # Xs - char arr (1 byte) with X length


        # TODO: Fill EtherType for Ethernet header
        eth_hdr = struct.pack("!6s6sH", dest_mac, source_mac, "<ARP EtherType>")
        # TODO: Fill arp header, see hints below
        # htype - ethernet (1)
        # ptype - TCP  (see EtherType)
        # hlen - length of hardware address (how many bytes in MAC addr...)
        # plen - length of protocol address (how many bytes in IP addr...)
        # operation - 1 for request, 2 for reply (we are sending...)
        arp_hdr = struct.pack("!HHBBH6s4s6s4s", "<htype>", "<ptype>", "<hlen>", "<plen>", "<operation>", source_mac, src_ip, dest_mac, dst_ip)

        packet = eth_hdr + arp_hdr

        self.sock.send(packet)


def __main__():
    # TODO: Pass interface on which to send ARP request
    arp = ARP("<iface>")
    # TODO: Pass destination IP
    arp.send_data("<dest ip>")


if __name__ == "__main__":
    __main__()
