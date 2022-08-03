# email source

#import needed libraries
import socket


host='localhost'
port=3000
buffer=1024

addr=(host,port)
source=socket.socket()
source.connect(addr)

#create messages to try filter
while True:
    sender_name=input('type your name: ')
    subject=input('enter your message subject: ')

    source.send(sender_name.encode())
    source.send(subject.encode())

    report=source.recv(buffer).decode()
    print(report)

    msg=input('continue type y or stop type n :')
    if msg=='y' :
        source.send('continue'.encode())
    else:
        source.send('stop'.encode())
        break
    
source.close()
