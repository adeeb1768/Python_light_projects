# spam filter code

#import needed libraries
import socket

host=''
port=3000
buffer=1024

sfilter=socket.socket()
sfilter.bind((host,port))

print('filter wait incomming messages....')

blocked_sender=[] #sender blocked
#words mean spam
spam_keys=['Password','password','User name','user name',
           'https://','enter your','send us','send your',
           'Dear account holder','Dear subscriber','buy now',
           'subscribe now','sign up now','buy now','special offer']
blocked_messages={} 

#search for words like spam key to block sender
def spam_filter(sender_name,subject):
    if any(x in subject for x in spam_keys):
        blocked_sender.append(sender_name)
        blocked_messages[sender_name]=subject
        conn.send('you are spam source ):'.encode())
    else:
        conn.send('you are not spam source (:'.encode())


#find if the sender blocked
def detect_sender(sender_name,subject):
    if sender_name in blocked_sender:
        conn.send('you are spam source ):'.encode())
    else:
        spam_filter(sender_name,subject)
#print blocked messages
def print_blocked_messages():
    messages=blocked_messages.items()
    print('messages blocked: ')
    for m in messages:
        print(m)

#filter routine

sfilter.listen(5)
conn, addr=sfilter.accept()
while True:
    sender_name=conn.recv(buffer).decode()
    subject=conn.recv(buffer).decode()
    detect_sender(sender_name,subject)
    msg=conn.recv(buffer).decode()
    if msg=='stop':
        break

print_blocked_messages()
conn.close()
    
