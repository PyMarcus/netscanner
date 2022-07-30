import nmap


class PortScan:
    """
    Nmap ("Network Mapper") is a free and open source utility for
    network discovery and security auditing. Many systems and network
    administrators also find it useful for tasks such as network inventory,
    managing service upgrade schedules, and monitoring host or service uptime.
    Nmap uses raw IP packets in novel ways to determine what hosts are available on the network,
    what services (application name and version) those hosts are offering,
    what operating systems (and OS versions) they are running,
    what type of packet filters/firewalls are in use, and dozens of other characteristics.
    It was designed to rapidly scan large networks, but works fine against single hosts.
    Nmap runs on all major computer operating systems, and official binary packages are available
    for Linux, Windows, and Mac OS X. In addition to the classic command-line Nmap executable
    the Nmap suite includes an advanced GUI and results viewer (Zenmap), a flexible data transfer,
    redirection, and debugging tool (Ncat), a utility
    for comparing scan results (Ndiff), and a packet generation and response analysis tool (Nping).
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

    def nmapScan(self) -> None:
        """
        uses nmap to scan the target
        :return:
        """
        nm = nmap.PortScanner()
        nm.scan(self.ip_target, self.port)
        state = nm.scan[self.ip_target]['tcp'][int(self.port)]['state']  # state and connection type
        print(f"[*] {self.ip_target} tcp/{self.port} {state}")
