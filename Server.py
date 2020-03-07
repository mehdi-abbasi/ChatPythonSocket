import socket

s = socket.socket()
print('socket successfully created')

port = 12345

s.bind(('', port))
print ('socket binded to ',port)

s.listen(5)
print ('socket is listening')

while True:
    client, address = s.accept()
    print ('got connection from', address)
    MSG, bbb = client.recvfrom(1024)
    print (MSG.decode())
    m = 'thank you for connecting'
    client.send(m.encode())
    client.close()
