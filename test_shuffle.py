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
def deal_card(com):
    card = random.choice(poker)
    com.append(convert(card))
    poker.remove(card)
    return card

def check(c):    #檢查是否有重複元素，避免重複輸入
        return len(c) != len(set(c))

def check2(c):
    standard = True
    for i in range((len(c))):
        if int(c[i]) > 13 or int(c[i]) < 1:
            standard = False
    return standard