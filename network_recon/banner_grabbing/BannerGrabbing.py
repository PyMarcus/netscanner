import socket
import threading


def connectionScan(target: str, port: list) -> None:
    """
    try to connect
    :param target (ip)
    :param port
    :return: none
    """
    low_level_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp (most connections are)
    for p in port:
        try:
            low_level_socket.connect((target, p))
            low_level_socket.send("give me a banner".encode())
            resp, addr = low_level_socket.recvfrom(1024)
            print(f"[+] The target says: {bytes(resp).rstrip().decode('cp1252')}: {addr[0]}-{bytes(addr[1]).decode('ISO-8859-1')} at {p}")  # response
        except EOFError:
            ...
        except ConnectionRefusedError:
            ...
        except OSError:
            ...
        low_level_socket.close()


def portScanner(ip_target, port):
    """
    list ports
    :return:
    """
    target = socket.gethostbyname(ip_target)
    try:
        threading.Thread(target=connectionScan, args=(target, port)).start()
    except EOFError:
        print(f"[^] Can´t resolve {ip_target}.Unknown Host")
        return None
