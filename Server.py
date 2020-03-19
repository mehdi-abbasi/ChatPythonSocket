import socket
import threading
import queue

def MSG_Broadcast(rmsg,rclient):
    for client in Clients:
        try:
            if Clients[client] != rclient:
                Clients[client].send(rmsg)
        except:
            print("ERROR BROADCASTING")

def conn_accept(myq):
    while True:
        client = server.accept()
        client[0].settimeout(0.0001)
        msg = client[0].recvfrom(1024)
        msg = msg[0].decode()
        print ('got connection from', msg)
        client_dict = {msg : client[0]}
        myq.put(client_dict)

q = queue.Queue()
Clients = {}

addr = ("127.0.0.1",8080)
server = socket.create_server(addr,family=socket.AF_INET,)

accept_thread = threading.Thread(target=conn_accept,args=(q,))
accept_thread.start()

while True:
    if not q.empty():
        c = q.get()
        Clients.update(c)
    for client in Clients:
        try:
            msg = Clients[client].recvfrom(1024)
            msg = client + ": " + msg[0].decode()
            msg = msg.encode()
            MSG_Broadcast(msg,Clients[client])
        except:
            pass
