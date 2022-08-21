import argparse

class ArgumentInputs():
    
    def argumentParser():
        parser = argparse.ArgumentParser(
            prog="port4l",
            description="port4l - Port Scanner")
        parser.add_argument("-H", "--host", help="Target IP", required=True)
        parser.add_argument("-P", "--port", help="Target Port", required=False)
        parser.add_argument("-fs", "--full-scan", action='store_true', help="Scan through all ports", required=False)
        parser.add_argument("-t", "--timeout", help="Set connection timeout in seconds, defaut is 0.05", required=False, default=0.05)
        parser.add_argument("-m", "--mode", help="Scan Mode, it can be:\n1. sS (TCP SYN Stealth Scan)\n2. sT (TCP Connect Scan)", type=str)
        args = parser.parse_args()
        return args