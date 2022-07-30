import socket


class PortScan:
    """
    In a network scanner, to consider:
    1) indentify the network topology
    2) find operating systems
    3) locate open ports and network services
    4) find live address of live host and firewalls
    5) consider a list of potential vulnerabilities
    6) be quiet
    """
    def __init__(self, ip_target: str, port: list[int]) -> None:
        """
        Scanner the network.If success, the port is open
        :param ip_target:
        :param port:
        """
        self.__ip_target = ip_target
        self.__port = port

    @property
    def ip_target(self):
        return self.__ip_target

    @property
    def port(self):
        return self.__port

    @staticmethod
    def __connectionScan(target: str, port: list) -> None:
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
                print(f"[+] tcp port: {p} -> is open")
            except EOFError:
                print(f"[-] tcp port: {p} -> is closed ")
            except ConnectionRefusedError:
                print(f"[-] connection refused to {p}.Probably there is a firewall blocking it")
            except OSError:
                print(f"[-] error to scan {p}")
            low_level_socket.close()

    def portScanner(self):
        """
        list ports
        :return:
        """
        target = socket.gethostbyname(self.ip_target)
        try:
            self.__connectionScan(target, self.port)
        except EOFError:
            print(f"[^] Can´t resolve {self.ip_target}.Unknown Host")
            return None
