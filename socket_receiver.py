import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server_sock.bind((socket.gethostname(), 8000))
# print(socket.gethostbyaddr(socket.gethostname()))
server_sock.listen(1)
client_sock , client_address = server_sock.accept()

print("starting file sharing...")
print("reading file...")

with open("./newfile",'w') as f:
    ans = '1'
    while ans :
        ans = client_sock.recv(2048)
        f.write(ans.decode())

print("closing connnection...")
client_sock.close()