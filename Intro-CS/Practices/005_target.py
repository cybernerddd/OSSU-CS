class Target(object):
    def __init__(self, ip, ports=None):
        """
        ports is a List
        """
        self.ip = ip
        self.ports = ports if ports is not None else []
    
    def add_port(self, port):
        """
        input: int, 
        appends aport to the ports
        list
        """
        self.ports.append(port)

    
    # remove a port
    def remove_port(self, port):
        """
        input: int, 
        removes port from the ports
        """
        if port in self.ports:
            self.ports.remove(port)
        else:
            raise ValueError("Port number not available")
    
    # counts numbrer of ports
    def port_count(self):
        return len(self.ports)
    
    # check if theres a port visible
    def has_port(self, port):
        """
        returns a Bool,
        if port in list of ports
        """
        return port in self.ports
    
    
# example
t = Target("192.168.1.5")
t.add_port(80)
t.add_port(443)
print(t.has_port(80))
print(t.port_count())
t.remove_port(80)
print(t.has_port(80))
