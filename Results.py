class Results():

    def results(selector):
        result_list, mode = selector
        if mode == "single":
            if len(result_list) == 0:
                print("[*] Port is closed")
            else:
                print(f"[*] Port {result_list[0]} is open")
        elif mode == "ranged":    
            if len(result_list) == 0:
                print("[*] No ports are open")    
            elif len(result_list) > 0:    
                for port in result_list:
                    print(f"[*] Port {port} is open")