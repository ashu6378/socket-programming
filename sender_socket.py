import socket

sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender.connect(('localhost', 8000))

print("enter file name: ")
file = input()
with open(file, 'r') as f:
	chunk = f.read(1048)
	while chunk:
		sender.send(chunk.encode(encoding='utf-8'))
		chunk = f.read(1048)
	

print("closing connection...")
sender.close()
