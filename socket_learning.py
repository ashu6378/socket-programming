import socket

from grpc import server

class Myset():
    def __init__(self, s = None):
        if s == None : 
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else :
            self.s = s
    
    def connect(self, host, port):
        self.s.connect((host, port))
    
    def my_send(self, msg):
        total_sent = 0
        MSGLEN = len(msg)
        while total_sent<MSGLEN:
            sent =  self.s.send(msg[total_sent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            total_sent += sent

    def my_recieve(self):
        chunks = []
        total_recv = 0
        MSGLEN = 10000
        while total_recv < MSGLEN:
            chunk = self.s.recv(min(MSGLEN-total_recv , 2048))
            if chunk = b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            total_recv += len(chunk)
        return b''.join(chunks)


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
client_sock.connect(('localhost', 5000))