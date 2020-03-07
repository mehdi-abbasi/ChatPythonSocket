import socket

s=socket.socket()

port = 12345

s.connect(('127.0.0.1', port))
msg = 'heloooo'
s.send(msg.encode())
rmsg, bbb = s.recvfrom(1024)
print (rmsg.decode())

s.close()