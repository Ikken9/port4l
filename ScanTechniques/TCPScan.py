import socket, sys

class TCPScan:

    def single_scan(host, port):
        scansocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scansocket.settimeout(float(0.05))
        results = []
        result = scansocket.connect_ex((host, int(port)))
        if result == 0:
            scansocket.close()
            results.append(port)
        return results

    def range_scan(host, port_min, port_max):
        scansocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scansocket.settimeout(float(0.05))
        results = []
        try:
            for port in range (port_min, port_max):
                result = scansocket.connect_ex((host, int(port)))
                if result == 0:
                    scansocket.close()
                    results.append(port)
        except KeyboardInterrupt:
            print("\n[*] User Requested Shutdown...")
            print("[*] Exiting...")
            sys.exit()
        return results