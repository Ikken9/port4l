from scapy.all import *
from scapy.layers.inet import IP, ICMP


class Ping:

    @staticmethod
    def ping_scan(host):
        conf.verb = 0
        icmp = sr(IP(dst=host) / ICMP(), timeout=0.05)
        if icmp is not None:
            return True
        elif icmp is None:
            return False
