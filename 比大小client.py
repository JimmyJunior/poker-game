import pickle
from socket import *

SERVER = gethostbyname(gethostname())# 伺服器IP地址
PORT = 5000  
DISCONNECT_MESSAGE = '!DISCONNECT'     
SERVER = '127.0.0.1'
FORMAT = 'utf-8'
HEADER = 1024
ADDR = (SERVER, PORT)

c = socket(type=SOCK_DGRAM)
#client.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
#client.connect(ADDR)
"""
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    #client.send(send_length)
    client.send(message)
    print()
"""
def rev():
    data = []
    while True:
        packet ,addr = c.recvfrom(4096)
        if not packet: 
            break
        data.append(packet)
    data_arr = pickle.loads(b"".join(data))
    print(data_arr)

def onerev():
    data, addr = c.recvfrom(1024)
    print(data.decode(FORMAT, 'ignore'))

c.sendto('hi'.encode(FORMAT), ADDR)
name = input('輸入你的名字: ')
#c.sendto(f'{name} is online.'.encode(FORMAT), ADDR)
c.sendto(name.encode(FORMAT), ADDR)
a = 1
while a:
    data, addr = c.recvfrom(1024)
    data = data.decode(FORMAT, 'ignore')
    if data == 'done':
        print(data)
        onerev()
        a = 0
    else:
        print(data)
        print(0)


print('西勒靠背')
while True:
    onerev()
    c.sendto('謝'.encode(FORMAT), ADDR)
    break
"""
send('收到')
connected = True
while connected:
    name = input('輸入你的名字')
    send(name.decode(FORMAT))
    a = client.recv(1024).decode(FORMAT)
    
    if a == 'None':
        connected = False
    print(a)
"""
"""
send('hello')
input()
send('你好')
input()
send('I am Jimmy')
send('DISCONNECT_MESSAGE')
"""