from multiprocessing import Process, Queue
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

def serverWlp2s0():
    server = Server("192.168.2.1", 5005)
    server.receive()

def serverWlp4s0():
    server = Server("192.168.2.1", 5005)
    server.receive()

if __name__ == "__main__":
    proc1 = Process(target=serverWlp2s0)
    proc2 = Process(target=serverWlp4s0)
    proc1.start()
    proc2.start()