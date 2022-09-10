import socket 

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
client_sock.connect(('169.254.67.40', 8000))
c = 0
ans  = "no" 
while ans:
    c += 1
    msg = input("enter message: ")
    client_sock.send(bytes(msg,'utf-8'))
    ans = client_sock.recv(100)
    print(str(ans))

client_sock.close()
print("closing client socket...")