class ScanReport(object):
    def __init__(self, target_ip, open_ports=None, scan_time="1.42s"):
        self.target_ip = target_ip
        self.open_ports = open_ports if open_ports is not None else []
        self.scan_time = scan_time
    
    # add open ports
    def add_open_port(self, port):
        self.open_ports.append(port)
    
    # find total ports
    def total_ports(self):
        return len(self.open_ports)

    # find if a port is opened
    def is_port_open(self, port):
        """
        returns Bool if port 
        is opened or not
        """
        return port in self.open_ports
    
    def summary(self):
        return f"""
        Target: {self.target_ip}
        Open Ports: {self.total_ports()}
        Ports: {self.open_ports}
        Scan Time: {self.scan_time}
        """

# example
# Create a new scan report
report = ScanReport("192.168.1.10")

# Add some open ports

report.add_open_port(22)
report.add_open_port(80)
report.add_open_port(443)

# Show summary
print(report.summary())
