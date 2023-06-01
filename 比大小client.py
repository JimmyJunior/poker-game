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


while True:
    onerev()
    c.sendto('謝'.encode(FORMAT), ADDR)
    break
