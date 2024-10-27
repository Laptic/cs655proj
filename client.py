import socket

MESSAGE = b"Hello, World!"

class ClientWlp:
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def sendMsg(self, msg):
        sock = socket.socket(socket.AF_INET, # Internet
                           socket.SOCK_DGRAM) # UDP
        sock.sendto(msg, (self.host, self.port))

if __name__ == "__main__":
    client = ClientWlp("192.168.2.1", 5005)
    client.sendMsg(MESSAGE)