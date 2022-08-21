from ScanTechniques.SYNStealthScan import *
from ScanTechniques.TCPScan import *

class Selector:
  
    def selector(ports_list, host, scan_mode, full_scan):
        result = []
        mode = ""
        print(scan_mode)
        if scan_mode == "sT" and len(ports_list) == 1 and full_scan == False:
            intport = int(ports_list[0])
            result = TCPScan.single_scan(host, intport)
            mode = "single"
        elif scan_mode == "sT" and len(ports_list) == 2 and full_scan == False:
            intport_min = int(ports_list[0])
            intport_max = int(ports_list[1])
            result = TCPScan.range_scan(host, intport_min, intport_max)
            mode = "ranged"
        elif scan_mode == "sT" and full_scan == True:
            result = TCPScan.range_scan(host, 1, 65535)
            mode = "ranged"
        elif scan_mode == "sS" and len(ports_list) == 1 and full_scan == False:
            intport = int(ports_list[0])
            result = SYNStealthScan.single_scan(host, intport)
            mode = "single"
        elif scan_mode == "sS" and len(ports_list) == 2 and full_scan == False:
            intport_min = int(ports_list[0])
            intport_max = int(ports_list[1])
            result = SYNStealthScan.range_scan(host, intport_min, intport_max)
            mode = "ranged"
        elif scan_mode == "sS" and full_scan == True:
            result = SYNStealthScan.range_scan(host, 1, 65535)
            mode = "ranged"
        return result, mode