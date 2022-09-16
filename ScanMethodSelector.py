from scan_functions.Ping import Ping
from scan_functions.TCPSYNStealth import *
from scan_functions.TCPConnect import *


class ScanMethodSelector:

    @staticmethod
    def scan_methods(ports_list, host, scan_mode, full_scan):
        result = []
        mode = ""
        if scan_mode == "sT" and len(ports_list) == 1 and full_scan is False:
            intport = int(ports_list[0])
            result = TCPConnect.single_scan(host, intport)
            mode = "single"
        elif scan_mode == "sT" and len(ports_list) == 2 and full_scan is False:
            intport_min = int(ports_list[0])
            intport_max = int(ports_list[1])
            result = TCPConnect.range_scan(host, intport_min, intport_max)
            mode = "ranged"
        elif scan_mode == "sT" and full_scan is True:
            result = TCPConnect.range_scan(host, 1, 65535)
            mode = "ranged"
        elif scan_mode == "sS" and len(ports_list) == 1 and full_scan is False:
            intport = int(ports_list[0])
            result = SYNStealth.single_scan(host, intport)
            mode = "single"
        elif scan_mode == "sS" and len(ports_list) == 2 and full_scan is False:
            intport_min = int(ports_list[0])
            intport_max = int(ports_list[1])
            result = SYNStealth.range_scan(host, intport_min, intport_max)
            mode = "ranged"
        elif scan_mode == "sS" and full_scan is True:
            result = SYNStealth.range_scan(host, 1, 65535)
            mode = "ranged"
        elif scan_mode == "sP":
            mode = "ping"
            result = Ping.ping_scan(host)
        return result, mode
