import sys

from datetime import datetime
from time import strftime
from ArgumentInputs import ArgumentInputs
from SyntaxChecker import SyntaxChecker
from TargetChecker import TargetChecker
from Selector import Selector
from Results import Results

class Logic:

    args = ArgumentInputs.argumentParser()
    port_list = []
    print("[*] Checking if target is online...")
    if TargetChecker.check_host(args.host) == 1:
        print("[!] Target isn't up")
        print("[!] Exiting...")
        sys.exit()
    else:
        if args.port == None and args.full_scan == False:
            print("[!] No port specified, please enter a port to scan")
            sys.exit()
        elif args.port != None and args.full_scan == False:
            if SyntaxChecker.check_port(args.port) == 1:
                print("[!] Syntax error, enter a valid por number or range")
                sys.exit()
            elif SyntaxChecker.check_port(args.port) == 2:
                print("[!] Port must be an integer between 1 and 65535, both included")
                sys.exit()
            else:
                ports = str(args.port)
                port_list = ports.split('-')

    print("[*] Scanning Started at " + strftime("%H:%M:%S") + "\n")
    start_clock = datetime.now()
    selector = Selector.selector(port_list, args.host, args.mode, args.full_scan)
    Results.results(selector)
    stop_clock = datetime.now()
    total_time = stop_clock - start_clock
    print("\n[*] Scanning Finished!")
    print("[*] Total Scan Duration: " + str(total_time))

