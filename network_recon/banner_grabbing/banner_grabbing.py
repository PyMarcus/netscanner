import sys
from BannerGrabbing import portScanner


if __name__ == '__main__':
    try:
        if sys.argv[1] == '-h':
            print("Scanner the network.If success, the port is open")
            print("usage: python banner_grabbing.py [hostname/IP address]")
        elif sys.argv[1] != " " and len(sys.argv) == 2:
            portScanner(sys.argv[1], [23, 80, 443, 5432, 21, 45])
            print(f"[*] Scan results for {sys.argv[1]}")

        else:
            print("Invalid option or usage")
    except IndexError:
        print("usage: python banner_grabbing.py [hostname/IP address]")
        print("for help: python banner_grabbing.py -h")