import random
import socket
from shuffle import *
from concurrent.futures import ThreadPoolExecutor

# 创建线程池，设置大小为 10
executor = ThreadPoolExecutor(max_workers=10)
player_names = ["dealer", "player1", "player2", "player3"]
connected_players = {}  # 记录已连接的玩家
def player_st(player_socket):
    player_cards = [] #有花色手排
    card_value=[] #convert過
    for i in range(2):
        player_cards.append(getpoker(draw_card(card_value)))

    ans = dealer_card(dealer_cards)
    message = "Your turn!\n\nYour cards: " + str(player_cards) + "\nDealer's card: " + str(ans)
    player_socket.send(message.encode())

    # 玩家回合
    while True:
        message = "Please choose 'hit' or 'stand':"
        player_socket.send(message.encode())
        choice = player_socket.recv(1024).decode().strip().lower()
        if choice == "hit":
            player_cards.append(getpoker(draw_card(card_value)))
            ans = dealer_card(dealer_cards)
            message = "Your turn!\n\nYour cards:" + str(player_cards) + "\nDealer's card: " + str(ans)
            player_socket.send(message.encode())
            if points(card_value) > 21:
                message = "You bust!\nWaiting Other Player"
                player_socket.send(message.encode())
                return points(card_value), player_cards 
        elif choice == "stand":
            message = "Waiting Other Player"
            player_socket.send(message.encode())
            return points(card_value), player_cards 
        else:
            ans = dealer_card(dealer_cards)
            message = "Invalid choice. Please choose 'hit' or 'stand'.\n\nYour cards: " + str(player_cards) + "\nDealer's card: " + str(ans)
            player_socket.send(message.encode())
def handle_client(player_name, client_socket):
    player_names.remove(player_name)
    # 如果是庄家，发牌给自己
    if player_name == "dealer":
        client_socket.send('You are a DEALER.'.encode())
    else:
        client_socket.send(f'You are {player_name}.'.encode())

    # 记录已连接的玩家
    connected_players[player_name] = client_socket
    
    # 等待所有玩家连接完毕
    if len(connected_players) == 3:
        start_game(dealer_cards)
    else:
        client_socket.send('Waiting for other pLayers'.encode())
        
            
    

def start_game(dealer_cards):    
    # 发牌给庄家
    dealer_card_value=[] #0~51
    for i in range(2):
        dealer_cards.append(getpoker(draw_card(dealer_card_value)))

    # 发牌给每个玩家
    for player_name, player_socket in connected_players.items():
        if player_name == "player1":
            player1_card, hand1 = player_st(player_socket)
        elif player_name == 'player2':
            player2_card, hand2 = player_st(player_socket)
        else:
            continue
    # 庄家回合
    hit_or_stand("dealer", dealer_cards,dealer_card_value,hand1, hand2)
    # 计算游戏结果
    dealer_sum = points(dealer_card_value)
    message = ''
    for player_name, player_socket in connected_players.items():
        #print(player_name)
        if player_name == "player1":
            result = allresult(hand1,player1_card,player_socket,dealer_sum, dealer_cards)
            message += f"\n\n{player_name}'s cards: {hand1}\nYour card: {dealer_cards}\nResult: {result}"
        elif player_name == 'player2':
            result = allresult(hand2, player2_card,player_socket,dealer_sum, dealer_cards)
            message += f"\n\n{player_name}'s cards: {hand2}\nYour card: {dealer_cards}\nResult: {result}"
    
    connected_players["dealer"].send(message.encode())

    # 关闭所有客户端连接
    for player_socket in connected_players.values():
        player_socket.close()
    server_socket.close()

#def draw_card():
    # 随机抽一张牌
    
    #return random.randint(1, 10)

def get_result(player_sum, dealer_sum):   
    #player_sum = points(all_value(player_cards))
    #dealer_sum = points(all_value(dealer_cards))
    print(dealer_sum,player_sum)
    if player_sum > 21:
        return " You bust! You lose",  " Player bust! You win"
    elif dealer_sum > 21:
        return "Dealer bust! You win.", 'You bust! You lose'
    elif player_sum > dealer_sum:
        return "You win!", "You lose"
    elif player_sum == dealer_sum:
        return "Tie! You lose.", "Tie! You win."
    elif player_sum < dealer_sum:
        return "You lose.", "You win."
    else:
        return "You lose.", "You win."

def hit_or_stand(player_name, dealer_cards,dealer_card_value, h1, h2):
    all = 'player1:' + str(dealer_card(h1))
    all = all + ', player2:' + str(dealer_card(h2))
    connected_players['dealer'].send(all.encode())
    message = "Your cards: " + str(dealer_cards) + "\nPlease choose 'hit' or 'stand': "
    connected_players['dealer'].send(message.encode())
    response = connected_players[player_name].recv(1024).decode()
    while True:
        if response.lower() == "hit":
            dealer_cards.append(getpoker(draw_card(dealer_card_value)))
            message = "Your turn!\n\nYour cards:" + str(dealer_cards)
            connected_players['dealer'].send(message.encode())
            if points(dealer_card_value) > 21:
                message = "You bust!\nWaiting Other Player"
                connected_players['dealer'].send(message.encode())
                break
        elif response.lower() == "stand":
            break
        else:
            continue
        message = "Please choose 'hit' or 'stand':" 
        connected_players[player_name].send(message.encode())
        response = connected_players[player_name].recv(1024).decode()

    return dealer_cards

def allresult(hand, player_sum, client_socket,sum, dealer_cards):
    result1, result2= get_result(player_sum, sum)
    message = f"\n\nYour cards: {hand}\nDealer's cards: {dealer_cards}\nResult: {result1}"
    client_socket.send(message.encode())
    return result2


def dealer_card(dealer_cards):
   final_cards = []
   for i in range(len(dealer_cards)-1):
       final_cards.append(dealer_cards[i])

   return final_cards


# 启动服务器
HOST = '192.168.179.203'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
dealer_cards = []
print("Server started on " + HOST + ":" + str(PORT))


def main():
    connected_clients = []
    while True:
        client_socket, address = server_socket.accept()
        # 将任务提交给线程池
        print("New connection from " + str(address))
        if len(connected_clients) == 0:
            player_name = "dealer"
        elif len(connected_clients) > 0:
            player_name = f"player{len(connected_clients)}"
        else:
            message = "The game has already started. Please try again later."
            client_socket.send(message.encode())
            client_socket.close()
            continue
          
        connected_clients.append(player_name)
        executor.submit(handle_client, player_name, client_socket)

if __name__ == '__main__':
    main()

# 启动服务器
"""
import random
import socket
from concurrent.futures import ThreadPoolExecutor

# 创建线程池，设置大小为 10
executor = ThreadPoolExecutor(max_workers=10)
#player_names = ["dealer","player1", "player2", "player3"]

def handle_client(player_name, client_socket):
    player_cards = []
    #player_names.remove(player_name)
    # 如果是庄家，发牌给自己
    if player_name == "dealer":
        dealer_cards = []
        client_socket.send('You are a DEALER.'.encode())
        dealer_cards.append(draw_card())
        dealer_cards.append(draw_card())
        message = "Your cards: [" + str(dealer_cards[0]) + "," + str(dealer_cards[1]) + "]" 
        print('5')
        client_socket.send(message.encode())
        print('6')
    # 如果是玩家，发牌给玩家
    else:
        client_socket.send(f'You are {player_name}.'.encode())
        player_cards.append(draw_card())
        player_cards.append(draw_card())
        message = "Welcome to 21 game!\n\nYour cards: " + str(player_cards) + "\nDealer's card: " + str(dealer_cards[0])
        client_socket.send(message.encode())
    
    # 玩家回合
    while True:
        # 接收玩家的选择
        message = "Please choose 'hit' or 'stand':"
        client_socket.send(message.encode())
        choice = client_socket.recv(1024).decode().strip().lower()
        
        if choice == "hit":
            player_cards.append(draw_card())
            message = "Your cards: " + str(player_cards) + "\nDealer's card: " + '[' + str(dealer_cards[0]) + ']\n'
            client_socket.send(message.encode())
            if sum(player_cards) >= 21:
                break
        elif choice == "stand":
            #player_names.append(player_name)
            break
        else:
            message = "Invalid choice. Please choose 'hit' or 'stand'.\n\nYour cards: " + '[' + str(player_cards)  
            + ']' + "\nDealer's card: " + '[' + str(dealer_cards[0]) + ']\n'
            client_socket.send(message.encode())
    
HOST = '127.0.0.1'
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server started on " + HOST + ":" + str(PORT))

players = ["player1", "player2", "player3"]
dealer_cards = []
def main():
    while True:
        client_socket, address = server_socket.accept()
        # 将任务提交给线程池
            
        print("New connection from " + str(address))
        message = "Please enter your name (" + "/".join(player_names) + "):"
        client_socket.send(message.encode())
        player_name = client_socket.recv(1024).decode().strip().lower()
        if player_name in players or player_name == "dealer":
            print('確定')
            executor.submit(handle_client, player_name, client_socket, players, dealer_cards)
        else:
            message = "Invalid player name. Please try again."
            client_socket.send(message.encode())
            #client_socket.close()

if __name__ == '__main__':
    main()

 player_cards.append(draw_card())
        player_cards.append(draw_card())
        message = "Welcome to 21 game!\n\nYour cards:" + "[" + str(player_cards[0]) + "," + str(player_cards[1]) + "]"
        client_socket.send(message.encode())
        message = "\nDealer's card:" + "[" + str(dealer_cards[0]) +"]"
        client_socket.send(message.encode())
"""

