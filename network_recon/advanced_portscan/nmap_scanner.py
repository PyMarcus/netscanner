import sys
from Thread import Thread


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            print("Scanner the network.If success, the port is open")
            print("usage: python nmap_scanner.py [hostname/IP address]")
        if sys.argv[1] != " " and len(sys.argv) == 2:
            th = [
                    Thread(sys.argv[1], [21, 25, 43]),
                    Thread(sys.argv[1], [80, 8080, 8081]),
                    Thread(sys.argv[1], [5432, 5433, 443]),
                    Thread(sys.argv[1], [53, 110, 23]),
                    Thread(sys.argv[1], [3000, 22, 23]),
                    Thread(sys.argv[1], [9000, 28, 143])
            ]
            print(f"[*] Scan results for {sys.argv[1]}")
            for threads in th:
                threads.start()
            for threads in th:
                threads.join()
        else:
            print("Invalid option or usage")
    except IndexError:
        print("usage: python nmap_scanner.py [hostname/IP address]")
        print("for help: python nmap_scanner.py -h")
