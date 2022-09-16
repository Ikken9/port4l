from logging import getLogger, ERROR
from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP
from tqdm import tqdm

getLogger("scapy.runtime").setLevel(ERROR)


class SYNStealth:

    @staticmethod
    def single_scan(host, port):
        SYNACK = 0x12
        ACKRST = 0x14
        opened = []
        closed = []
        filtered = []
        RST_packet = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags="R")
        SYN_packet = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags="S")
        try:
            ans = sr1(SYN_packet, timeout=0.01)
            if ans is None:
                filtered.append(port)
            elif ans.haslayer(TCP):
                if ans.getlayer(TCP).flags == SYNACK:
                    opened.append(port)
                elif ans.getlayer(TCP).flags == ACKRST:
                    closed.append(port)
                elif int(ans.getlayer(ICMP).type) == 3 and int(ans.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                    filtered.append(port)
            send(RST_packet)
        except KeyboardInterrupt:
            send(RST_packet)
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            sys.exit()
        return opened, closed, filtered

    @staticmethod
    def range_scan(host, port_min, port_max):
        SYNACK = 0x12
        ACKRST = 0x14
        open = []
        closed = []
        filtered = []
        try:
            for port in tqdm(range(port_min, port_max + 1)):
                RST_packet = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags="R")
                SYN_packet = IP(dst=host) / TCP(sport=RandShort(), dport=port, flags="S")
                ans = sr1(SYN_packet, timeout=0.01)
                if ans is None:
                    filtered.append(port)
                    send(RST_packet)
                elif ans.haslayer(TCP):
                    if ans.getlayer(TCP).flags == SYNACK:
                        open.append(port)
                        send(RST_packet)
                    elif ans.getlayer(TCP).flags == ACKRST:
                        closed.append(port)
                        send(RST_packet)
                    elif int(ans.getlayer(ICMP).type) == 3 and int(ans.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                        filtered.append(port)
                        send(RST_packet)
        except KeyboardInterrupt:
            send(RST_packet)
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            return open, closed, filtered
        return open, closed, filtered
