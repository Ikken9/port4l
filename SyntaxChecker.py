import ipaddress

class SyntaxChecker:

    def check_host_syntax(host_ip):
        try:
            ipaddress.ip_address(host_ip)
            return True
        except ValueError:
            return False
    
    def check_port(port):
        port = str(port)
        try: 
            ports_list = port.split('-')
        except:
            return 1
        for ports in ports_list:  
            if int(ports) <= 0 or int(ports) > 65535:
                return 2
            else:
                return 0