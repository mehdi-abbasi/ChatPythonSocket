import socket
import threading

def msg_recieve():
    while True:
        msg = s.recvfrom(1024)
        print (msg[0].decode())

User_Name = input("Please Enter Your Username: ")
s=socket.socket()

port = 8080
s.connect(('127.0.0.1',port))

s.send(User_Name.encode())


msg_handler = threading.Thread(target=msg_recieve)
msg_handler.start()

while True:
    
    msg = input("")
    s.send(msg.encode())
