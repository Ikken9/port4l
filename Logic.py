import sys

from datetime import datetime
from time import strftime
from ArgumentParser import ArgumentParser
from scan_functions.Ping import Ping
from SyntaxChecker import SyntaxChecker
from Selector import Selector
from Results import Results

class Logic:

    args = ArgumentParser.argumentParser()
    port_list = []
    
    if args.mode not in ["sS", "sT", "sP"]:
        print("[!] Invalid operating mode")
        sys.exit()

    if SyntaxChecker.check_host_syntax(args.host) == False:
        print("[!] Syntax error, enter a valid host IP")
        sys.exit()

    if args.port == None and args.full_scan == False and args.mode != "sP":
        print("[!] No port specified, please enter a port to scan")
        sys.exit()
    elif args.port != None and args.full_scan == False:
        if SyntaxChecker.check_port_syntax(args.port) == 1:
            print("[!] Syntax error, enter a valid port number or range")
            sys.exit()
        elif SyntaxChecker.check_port_syntax(args.port) == 2:
            print("[!] Port must be an integer between 1 and 65535, both included")
            sys.exit()
        elif SyntaxChecker.check_port_syntax(args.port) == 3:
            print("[!] Syntax error, smaller port first: <smaller_port>-<largest_port>")
            sys.exit()
        else:
            ports = str(args.port)
            port_list = ports.split('-')

    print("\n")
    if args.mode == "sP":
        selector = Selector.selector(port_list, args.host, args.mode, args.full_scan)
        Results.report(selector)
        sys.exit()
    
    print("[*] Checking if target is online...")
    if Ping.ping_scan(args.host) == False:
        print("[!] Target isn't up")
        print("[!] Exiting...")
        sys.exit()

    print("[*] Scanning Started at " + strftime("%H:%M:%S") + "\n")
    start_clock = datetime.now()
    selector = Selector.selector(port_list, args.host, args.mode, args.full_scan)
    Results.report(selector)
    stop_clock = datetime.now()
    total_time = stop_clock - start_clock
    print("\n[*] Scanning Finished!")
    print("[*] Total Scan Duration: " + str(total_time))

