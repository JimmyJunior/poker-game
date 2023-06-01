import socket
import time
HOST = '127.0.0.1'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def slipper(choice):
    if len(choice) == 1 and choice[0] == 'p':
        return False
    if len(choice) == 0:
        return True
    for i in range(len(choice)):
        if not choice[i].isdigit():
            return True
    else:
        return False

recv = {
    '1' : '請輸入牌型:(若要第一張 --> 1 第二張 --> 2 以此類推，中間以空格間隔)',
    '2' : '請重新輸入:',
    '3' : '遊戲結束'
}
# 接收 "Please enter your name (player1/player2/player3):" 消息
message = client_socket.recv(1024).decode().strip()
print(message)

c= True
while True:
    data = client_socket.recv(1024).decode().strip()
    if data in recv:
        data = recv[data]
        print(data)
        if data == '遊戲結束':
            time.sleep(2)
            client_socket.close()
            break
        choice = input().lower().split()
        c = slipper(choice) 
        while c:
            choice = input('請重新輸入:').lower().split()
            c = slipper(choice)
        if isinstance(choice, list):
            chat = ' '.join(choice)
            client_socket.send(chat.encode())
        else:
            client_socket.send(choice.encode()) 
    else:
        print(data)

