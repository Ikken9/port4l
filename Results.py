class Results():

    def report(selector):
        print("\nPort4l scan report:\n")
        result, mode = selector
        open, closed, filtered = result
        if mode == "single":
            if len(open) == 1 and len(closed) == 0 and len(filtered) == 0:
                print(f"Port {open[0]} is open")
            elif len(open) == 0 and len(closed) == 1 and len(filtered) == 0:
                print(f"Port {closed[0]} is closed")
            elif len(open) == 0 and len(closed) == 0 and len(filtered) == 1:
                print(f"Port {filtered[0]} is filtered")
        elif mode == "ranged":    
            print(f"{len(closed)} closed ports\n{len(filtered)} filtered ports\n")
            if len(open) == 0:
                print("No ports open")    
            elif len(open) > 0: 
                for port in open:
                    print(f"Port {port} is open")
        elif mode == "ping":
            if result == True:
                print("Target is up")
            elif result == False:
                print("Target isn't up")