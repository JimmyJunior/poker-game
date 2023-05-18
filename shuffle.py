import random
n = 52
poker = [i for i in range(n)]

def shuffle(k):
    for i in range(52):
        p1 = random.randrange(0, k-1)
        p2 = random.randrange(0, k-1)
        poker[p1], poker[p2] = poker[p2], poker[p1]

def color(x):
    color = ['♣', '♦', '♥', '♠']
    c = x%4
    if c < 0 or c > 4:
        return 'Error'
    return color[c]

def value(x):
    value = x //4 + 1
    if value == 1:
        return 'A'
    elif value >= 2 and value <= 10:
        return str(value)
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'

def getpoker(x):
    return color(x) + value(x) + ' '

def pleyerpoker(a):
    b = []
    for x in range(a):
        paper = getpoker(poker[0])
        b.append(paper)
        del poker[0]
    return b
    #print(''.join(a))
    #print(''.join(b))
    #print(''.join(c))
"""
def deal_card():
    card = random.choice(poker)
    poker.remove(card)
    return card
"""
def valuenumber(x):
    value = x // 4 + 1
    return value
def convert(x):
    number=x //4 + 1
    if number>10: 
        return 10
    elif number==1: 
        return 11
    else: 
        return number
def all_value(l):
    for i in range(len(l)):
        l[i] = convert(l[i]) 
    return l
def points(a):
    su=sum(a)
    if len(a)==2: 
        return su
    elif su>21:
        for i in range (0, len(a), 1):
            if a[i]==11:
                a[i]=1
        su=sum(a)
        return su
    else: 
        return su
def draw_card(com):
    card = random.choice(poker)
    com.append(convert(card))
    poker.remove(card)
    return card
"""
#先發兩張牌給玩家
for i in range(2):
    player.append(getpoker(deal_card(playertotal)))
    master.append(getpoker(deal_card(mastertotal)))
print(f"玩家的牌：{player}")
print(f"莊家的明牌：{master[1]}")
#print(mastertotal)
#print(playertotal)
answer=""
while answer != "n":
    answer=input('是否要加牌?(y/n)')
    if answer=="y":
        player.append(getpoker(deal_card(playertotal)))
        playerpoint=points(playertotal)
        #print("你目前的牌:",player)
        if playerpoint>21:
            #print("哈哈你輸了")
            answer="n"
        else: 
            print("加牌後的手牌",player,) 
            #print(f"你的點數:{playerpoint}")
    elif answer == "n":
        playerpoint=points(playertotal)
        print(f"你的點數:{playerpoint}")
    else:
        print("請重新輸入！  是否要加牌?(y/n)")
        #算莊家的
    masterpoint=points(mastertotal)
    while masterpoint<17:
        master.append(getpoker(deal_card(mastertotal)))
        masterpoint=points(mastertotal)
print(f"玩家的牌：{player}，共{playerpoint}點")
print(f"莊家的牌：{master}，共{masterpoint}點")
if playerpoint>21:
    print("輸了哈哈")
elif masterpoint>21:
    print("恭喜你")
elif playerpoint==masterpoint:
    print("平手欸")
elif playerpoint>masterpoint:
    print("恭喜你")
else: 
    print("輸了哈哈")
"""
 #大老二   
def check(c):    #檢查是否有重複元素，避免重複輸入
        return len(c) != len(set(c))

def check2(c):
    standard = True
    for i in range((len(c))):
        if int(c[i]) > 13 or int(c[i]) < 1:
            standard = False
    return standard
'''def game(c,f):
    d=[]
    if(f=='順子'):
   '''     
userinputarray=[]
playertotal=[]
player1total=[]
player2total=[]
master=[]  #存莊家手牌
player_1=[]  #存玩家手牌
player_3=[]
player_5=[]
#先發兩張牌給玩家
'''for i in range(13):
    player_1.append(getpoker(deal_card(playertotal)))
    master.append(getpoker(deal_card(mastertotal)))
    '''
class player:
    def __init__(self,name,poker,a):
        self.name=name
        self.poker=poker
        self.a = a
    def getcard(self, a,b):    #b是暫存數字的list
        for i in range(13):
            b.append(draw_card())
        b.sort()               #把b排好
        for i in range(13):
            a.append(getpoker(b[i]))       #把玩家手牌由小到大排好
        #playertotal.clear()
        return a     
         
    def receive(self,b,c):
        c = input('請輸入牌型:(若要第一張 --> 1 第二張 --> 2 以此類推，中間以空格間隔)').split()
        #print(c)
        #print(len(c))
        while ((len(c)!=1 and len(c)!=2 and len(c)!=5) or(check(c) or not check2(c))) :
            c = input('請重新輸入:').split()
        #print(len(c))
        #print(c)
        #print(check(c))
        d=len(c)
        for i in range(d):
            #b.remove(b[c[i]])
            #c[i] = int(valuenumber(b[int(c[i])-1]))
            c[i] = int(b[int(c[i])-1])
            #c.append(int(valuenumber(b[int(c[i])-1])))
        #print(c)
        return c
    def judge(self,c):       #a是儲存玩家輸入的數字的list    b是玩家牌
    #先傳入陣列(x[])
    #讀取陣列元素，長度 5 -> 鐵支 葫蘆 順子 2 -> 一對   1 -> 單張
    #判斷牌型
    #是否比前一個大
    #return牌型 ex:    33344,3葫蘆
    #輸入
        #print(c)
        c.sort()
        '''if len(c)==1:
            return ('你選了',c[0],'一張')
        if len(c)==2:
            if c[0]==c[1]:
                return ('你選了',c[0],'一對')
            else:
                return -1
        else:
            if(c[0] == c[1] and c[1] == c[2] and c[2] != c[3] and c[3] == c[4]):
                return ('你選了',c[0],'葫蘆')
            elif(c[0] == c[1] and c[1] != c[2] and c[2] == c[3] and c[3] == c[4]):
                return ('你選了',c[2],'葫蘆')
            elif(c[0] == c[1] and c[1] == c[2] and c[2] == c[3] and c[3] != c[4]):
                return ('你選了',c[0],'鐵支')
            elif(c[1]-c[0] == c[2]-c[1] and c[3]-c[2] == c[2]-c[1] and c[4]-c[3] == c[3]-c[2]):
                return ('你選了','順子')
            else :
                return -1             '''
        temp=[]
        for i in len(c):
            temp.append(c[i])
        if len(c)==1:
            return ('你選了',c[0],'一張')
        if len(c)==2:
            if temp[0]==valuenumber(c[1]):
                return ('你選了',c[0],'一對')
            else:
                return -1
        else:
            if(c[0] == c[1] and c[1] == c[2] and c[2] != c[3] and c[3] == c[4]):
                return ('你選了',c[0],'葫蘆')
            elif(c[0] == c[1] and c[1] != c[2] and c[2] == c[3] and c[3] == c[4]):
                return ('你選了',c[2],'葫蘆')
            elif(c[0] == c[1] and c[1] == c[2] and c[2] == c[3] and c[3] != c[4]):
                return ('你選了',c[0],'鐵支')
            elif(c[1]-c[0] == c[2]-c[1] and c[3]-c[2] == c[2]-c[1] and c[4]-c[3] == c[3]-c[2]):
                return ('你選了','順子')
            else :
                return -1

"""
#a = input("請輸入名字:")
#player_2=player(a,poker,player_1)

#print (player_2.name,"的牌:",player_2.getcard(player_1,playertotal))
'''b = input("請輸入名字:")player_4=player(b,poker,player_3)
print (player_4.name,"的牌:",player_4.getcard(player_3,player1total))
c = input("請輸入名字:")
player_6=player(c,poker,player_5)
print (player_6.name,"的牌:",player_6.getcard(player_5,player2total))
answer = -1'''

#print(player_2.receive(playertotal,userinputarray))
#userinputarray = player_2.receive(playertotal,userinputarray)
#print(userinputarray,'測試')
while True:
    if(player_2.judge(userinputarray) != -1):
        print(player_2.judge(userinputarray))
        break
    else:
        while player_2.judge(userinputarray) == -1:
            print('Oh no!沒有這樣的牌型')
            userinputarray = player_2.receive(playertotal,userinputarray)

#print(returnvalue)
#while player_2.judge(player_2.receive(playertotal,userinputarray))
'''while player_2.judge(userinputarray) == -1:
    print(player_2.receive(playertotal,userinputarray))
    #print()'''
"""