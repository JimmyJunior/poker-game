import socket

HOST = '192.168.178.173'
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
            #print(choice[i],choice[i].isdigit())
            return True
    else:
        return False

recv = {
    '1' : '請輸入牌型:(若要第一張 --> 1 第二張 --> 2 以此類推，中間以空格間隔)',
    '2' : '請重新輸入:',
}
# 接收 "Please enter your name (player1/player2/player3):" 消息
message = client_socket.recv(1024).decode().strip()
print(message)

# 发送玩家名称
#player_name = input()
#client_socket.send(player_name.encode())
c= True
# 接收游戏数据
while True:
    data = client_socket.recv(1024).decode().strip()
    if data in recv:
        data = recv[data]
        print(data)
        choice = input().lower().split() # 接收玩家选择并发送到服务器
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

