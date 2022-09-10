import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server_sock.bind(('', 8000))

server_sock.listen(1)
client_sock , client_address = server_sock.accept()

print("server started...")
msg = "no"
while msg:
    msg = client_sock.recv(100)
    if not msg:
        break
    print(str(msg))
    ans = input("enter message: ")
    client_sock.send(bytes(ans,'utf-8'))

client_sock.close()
server_sock.close()
print("closing server socket...")