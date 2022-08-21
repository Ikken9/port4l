import sys

from scapy.all import *
from scapy.layers.inet import IP, TCP

class SYNStealthScan:
    
    def single_scan(host, port):
        SYNACK = 0x12
        ACKRST = 0x14
        results = []
        try:
            conf.verb = 0
            RSTpkt = IP(dst = host)/TCP(sport = RandShort(), dport = port, flags = "R")
            tcp_packet = sr1(IP(dst = host)/TCP(sport = RandShort(), dport = port, flags = "S"))
            tpc_packet_flags = tcp_packet.getlayer(TCP).flags
            
            if tpc_packet_flags == SYNACK:
                results.append(port)            
            send(RSTpkt)
        except KeyboardInterrupt:
            RSTpkt = IP(dst = host)/TCP(sport = RandShort(), dport = port, flags = "R")
            send(RSTpkt)
            
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            sys.exit()
        return results

    def range_scan(host, port_min, port_max):
        SYNACK = 0x12
        ACKRST = 0x14
        results  = []
        try:
            conf.verb = 0
            for port in range (port_min, port_max): 
                RSTpkt = IP(dst = host)/TCP(sport = RandShort(), dport = port, flags = "R")
                tcp_packet = sr(IP(dst = host)/TCP(sport = RandShort(), dport = port, flags = "S"))
                tcp_packet_flags = tcp_packet.getlayer(TCP).flags
                
                if tcp_packet_flags == SYNACK:
                    results.append(port)
                send(RSTpkt)
        except KeyboardInterrupt:
            send(RSTpkt)
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            sys.exit()
        return results