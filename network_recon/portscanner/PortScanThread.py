import threading
from network_recon.portscanner.PortScanController import PortScan


class Thread(threading.Thread):
    def __init__(self, ip: str, ports: list[int]):
        super().__init__()
        self.ip = ip
        self.ports = ports

    def run(self) -> None:
        PortScan(self.ip, self.ports).portScanner()
