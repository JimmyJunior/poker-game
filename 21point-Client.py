import socket

HOST = '192.168.179.203'
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 接收 "Please enter your name (player1/player2/player3):" 消息
message = client_socket.recv(1024).decode().strip()
print(message)

# 发送玩家名称
#player_name = input()
#client_socket.send(player_name.encode())

# 接收游戏数据
while True:
    data = client_socket.recv(1024).decode().strip()
    if data:
        print(data)
        if "Please choose 'hit' or 'stand':" in data:
            # 接收玩家选择并发送到服务器
            choice = input().lower()
            while choice not in ["hit", "stand"]:
                choice = input("Invalid choice. Please choose 'hit' or 'stand': ")
            client_socket.send(choice.encode())
    else:
        break

client_socket.close()
