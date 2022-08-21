from scapy.all import *
from scapy.layers.inet import IP, ICMP

class TargetChecker:

    def check_host(host):
        conf.verb = 0
        icmp = sr(IP(dst = host)/ICMP(), timeout = 3)
        if icmp is not None:    
            return 0
        elif icmp is None:
            return 1
    
    