from socket import *
import threading
from test_shuffle import *
import time
SERVER = '127.0.0.1' # 伺服器IP地址
PORT = 5000  
HEADER = 1024
ADDR = (SERVER, PORT)
#DISCONNECT_MESSAGE = '!DISCONNECT'
FORMAT = 'utf-8' #解碼
user = [] #玩家手牌
IP = [] #玩家位子
mastertotal=[]
playertotal=[]
master=[]  #存莊家手牌
Person=[]  #存玩家手牌
times = 0 #玩家位子

shuffle(52) #洗牌
#hand = sh.pleyerpoker(1)
class player:
    def __init__(self, cards):
        self.cards   = cards
    def getcard(self, cards):
        b = []            #b是暫存數字的list
        for i in range(13):
            b.append(deal_card())
        b.sort()               #把b排好
        for i in range(13):
            cards.append(getpoker(b[i]))  

        return cards
     
    def receive(self,b,c):
        c = input('請輸入牌型:(若要第一張 --> 1 第二張 --> 2 以此類推，中間以空格間隔)').split()
        while ((len(c)!=1 and len(c)!=2 and len(c)!=5) or(check(c) or not check2(c))) :
            c = input('請重新輸入:').split()
        d=len(c)
        for i in range(d):
            c[i] = int(b[int(c[i])-1])
        return c
def send(massage, i):
    s.sendto(f'{massage}', i)

def handle_client(times, addr): #確認玩家
    print(f'[NEW CONNETCION]{addr}connected.')
    user_name, addr = s.recvfrom(1024)
    user.append(user_name)
    print(user_name)
    for i in range(2):
        Person.append(getpoker(deal_card(playertotal)))
        master.append(getpoker(deal_card(mastertotal)))
    send(f"玩家的牌：{Person}", addr)
    send(f"莊家的明牌：{master[1]}", addr)
    send('是否要加牌?(y/n)', addr)
    #print(mastertotal)
    #print(playertotal)
    answer = ""
    while answer != "n":
        answer = s.recvfrom(1024)
        #answer=input('是否要加牌?(y/n)')
        if answer=="y":
            Person.append(getpoker(deal_card(playertotal)))
            playerpoint=points(playertotal)
            #print("你目前的牌:",player)
            if playerpoint>21:
                #print("哈哈你輸了")
                answer="n"
            else: 
                print("加牌後的手牌",Person) 
                #print(f"你的點數:{playerpoint}")
        elif answer == "n":
            playerpoint=points(playertotal)
            print(f"你的點數:{playerpoint}")
        else:
            send("請重新輸入！  是否要加牌?(y/n)", addr)
            #算莊家的
        masterpoint=points(mastertotal)
        while masterpoint<17:
            master.append(getpoker(deal_card(mastertotal)))
            masterpoint=points(mastertotal)
    send(f"玩家的牌：{Person}，共{playerpoint}點")
    send(f"莊家的牌：{master}，共{masterpoint}點")
    if playerpoint>21:
        send("輸了哈哈", addr)
    elif masterpoint>21:
        send("恭喜你", addr)
    elif playerpoint==masterpoint:
        send("平手欸", addr)
    elif playerpoint>masterpoint:
        send("恭喜你", addr)
    else: 
        send("輸了哈哈")
    
def start(times):
    notice = True
    while notice:
        print(f'伺服器等待連接,IP = {SERVER}')
        data, addr = s.recvfrom(1024) #等等待連結並確認IP
        IP.append(addr) #存取玩家IP
        #print(f'[ACTIVE CONNETCIONS]{threading.activeCount()}')

        thread = threading.Thread(target=handle_client, args=(times, addr))
        thread.start()
        #handle_client(times, addr)
    while not s.recvfrom(1024):
        print(s.recvfrom(1024))
    s.close()  
    
s = socket(type=SOCK_DGRAM)
s.bind(ADDR)
start(times)
s.close()


"""
while True:
    while True:
        data = conn.recv(1024) # 接收客戶端發送的消息
        #data.send(getpoker(poker[0]))
        #del poker[0]
        conn.send(b'hello')
        if not data:
            break
    print('收到消息：', data.decode())



            msg_length = conn.recv(1024).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'[{addr}]{msg}')
            conn.send('Msg received'.encode(FORMAT))
            print()
"""
"""
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    server.sendto(send_length)
    server.sendto(message)
"""    

"""
class player:
    def __init__(self,name):
        self.name=name
        #self.poker=poker
    def getcards(self):
        self.poker  = sh.getpoker(sh.deal_card())
        return self.poker
"""