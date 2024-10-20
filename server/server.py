import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def receive(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.host,self.port))
        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            print("received message: %s" % data)

if __name__ == "__main__":
    server = Server("127.0.0.1", 5005)
    server.receive()