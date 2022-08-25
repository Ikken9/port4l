import socket, sys

from tqdm import tqdm

class TCPConnect:

    def single_scan(host, port):
        try:
            open = []
            closed = []
            filtered = []
            scansocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scansocket.settimeout(float(1))
            result = scansocket.connect_ex((host, int(port)))
            if result == 0:
                open.append(port)
            else:
                closed.append(port)
            scansocket.close()
        except KeyboardInterrupt:
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            return open, closed, filtered
        return open, closed, filtered

    def range_scan(host, port_min, port_max):
        open = []
        closed = []
        filtered = []
        try:
            for port in tqdm(range(port_min, port_max+1)):
                scansocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scansocket.settimeout(float(1))
                result = scansocket.connect_ex((host, int(port)))
                if result == 0:
                    open.append(port)
                else:
                    closed.append(port)
                scansocket.close()
        except KeyboardInterrupt:
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            return open, closed, filtered
        return open, closed, filtered