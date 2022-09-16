import ipaddress


# noinspection PyBroadException
class SyntaxChecker:

    @staticmethod
    def check_host_syntax(host_ip):
        try:
            ipaddress.ip_address(host_ip)
            return True
        except:
            return False

    @staticmethod
    def check_port_syntax(port):
        port = str(port)
        try:
            ports_list = port.split('-')
        except:
            return 1

        if len(ports_list) > 2:
            return 1

        if len(ports_list) > 1:
            try:
                int(ports_list[0])
                int(ports_list[1])
            except:
                return 1

            if int(ports_list[0]) < int(ports_list[1]):
                for ports in ports_list:
                    if int(ports) <= 0 or int(ports) > 65535:
                        return 2
            else:
                return 3
