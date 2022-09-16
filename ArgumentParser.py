import argparse


class ArgumentParser:

    @staticmethod
    def argument_parser():
        parser = argparse.ArgumentParser(
            prog="port4l",
            description="port4l - Port Scanner")
        parser.add_argument("-H", "--host", help="Target IP", required=True)
        parser.add_argument("-P", "--port", help="Target Port", required=False)
        parser.add_argument("-fs", "--full-scan", action='store_true', help="Scan through all ports", required=False)
        parser.add_argument("-m", "--mode",
                            help="Scan Mode, it can be:\n"
                                 "1. sS (TCP SYN Stealth Scan)\n"
                                 "2. sT (TCP Connect Scan)\n"
                                 "3. sP (Ping Target)",
                            type=str)
        args = parser.parse_args()
        return args
