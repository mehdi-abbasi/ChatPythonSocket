import socket

s = socket.socket()
print('socket successfully created')

port = 12345

s.bind(('', port))
print ('socket binded to ',port)

s.listen(5)
print ('socket is listening')
client, address = s.accept()
print ('got connection from', address)
while True:
        
        
        MSG, bbb = client.recvfrom(1024)
        print (MSG.decode())
        m = input('Enter your message:')
        client.send(m.encode())
        if MSG.decode() == 'quit()':
           break
