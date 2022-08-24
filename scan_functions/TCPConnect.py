import socket, sys

class TCPConnect:

    def single_scan(host, port):
        scansocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scansocket.settimeout(float(0.05))
        open = []
        closed = []
        filtered = []
        result = scansocket.connect_ex((host, int(port)))
        if result == 0:
            scansocket.close()
            open.append(port)
        else:
            closed.append(port)
        return open, closed, filtered

    def range_scan(host, port_min, port_max):
        scansocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scansocket.settimeout(float(0.05))
        open = []
        closed = []
        filtered = []
        try:
            for port in range (port_min, port_max+1):
                result = scansocket.connect_ex((host, int(port)))
                if result == 0:
                    scansocket.close()
                    open.append(port)
                else:
                    closed.append(port)
        except KeyboardInterrupt:
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            sys.exit()
        return open, closed, filtered