import pygame
import random
from random import randint
import os
pygame.init()
screenWidth = 1000
screenHeight = 800
display = (screenWidth, screenHeight)
win = pygame.display.set_mode(display)
pygame.display.set_caption("Gamebling")
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
purple = (102,0,204)
cardsPics = [pygame.image.load(os.path.join('gameblingPic','1clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','1diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','1heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','1spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','2clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','2diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','2heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','2spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','3clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','3diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','3heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','3spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','4clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','4diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','4heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','4spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','5clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','5diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','5heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','5spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','6clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','6diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','6heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','6spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','7clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','7diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','7heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','7spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','8clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','8diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','8heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','8spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','9clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','9diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','9heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','9spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','10clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','10diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','10heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','10spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','11clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','11diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','11heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','11spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','12clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','12diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','12heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','12spade.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','13clover.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','13diamond.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','13heart.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','13spade.png')).convert_alpha()]
horsesPics =[pygame.image.load(os.path.join('gameblingPic','Rhorse.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','Bhorse.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','Ghorse.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','Yhorse.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','Phorse.png')).convert_alpha()]
coloredButtonsPics =[pygame.image.load(os.path.join('gameblingPic','Rbutton3.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','Bbutton3.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','Gbutton3.png')).convert_alpha(),pygame.image.load(os.path.join('gameblingPic','Ybutton3.png')).convert_alpha(),
             pygame.image.load(os.path.join('gameblingPic','Pbutton3.png')).convert_alpha()]
track = pygame.image.load(os.path.join('gameblingPic','TrackRace.png')).convert_alpha()
pokerTable = pygame.image.load(os.path.join('gameblingPic','PokerTable.png')).convert_alpha()
background = pygame.image.load(os.path.join('gameblingPic','Background.png')).convert_alpha()
button1 = pygame.image.load(os.path.join('gameblingPic','button1.png')).convert_alpha() #100,75
button2 = pygame.image.load(os.path.join('gameblingPic','button2.png')).convert_alpha() #100,60
darkButton2 = pygame.image.load(os.path.join('gameblingPic','darkbutton2.png')).convert_alpha()
button3 = pygame.image.load(os.path.join('gameblingPic','button3.png')).convert_alpha() #135,50
button4 = pygame.image.load(os.path.join('gameblingPic','button4.png')).convert_alpha() #150,75
rouletteBoard = pygame.image.load(os.path.join('gameblingPic','rouletteBoard.png')).convert_alpha()
rouletteBackground = pygame.image.load(os.path.join('gameblingPic','rouletteBackground.png')).convert_alpha()
roulette = pygame.image.load(os.path.join('gameblingPic','roulette.png')).convert_alpha()
spinningRoulette = pygame.transform.rotate(roulette, 0)
coin100 = pygame.image.load(os.path.join('gameblingPic','100coin.png')).convert_alpha()
coin50 = pygame.image.load(os.path.join('gameblingPic','50coin.png')).convert_alpha()
coin10 = pygame.image.load(os.path.join('gameblingPic','10coin.png')).convert_alpha()
coin5 = pygame.image.load(os.path.join('gameblingPic','5coin.png')).convert_alpha()
modeHorse1 = pygame.image.load(os.path.join('gameblingPic','Mode - horse1.png')).convert_alpha()
modeHorse2 = pygame.image.load(os.path.join('gameblingPic','Mode - horse2.png')).convert_alpha()
modeBlackjack1 = pygame.image.load(os.path.join('gameblingPic','Mode - blackjack1.png')).convert_alpha()
modeBlackjack2 = pygame.image.load(os.path.join('gameblingPic','Mode - blackjack2.png')).convert_alpha()
modeRoulette1 = pygame.image.load(os.path.join('gameblingPic','Mode - roulette1.png')).convert_alpha()
modeRoulette2 = pygame.image.load(os.path.join('gameblingPic','Mode - roulette2.png')).convert_alpha()
icon = pygame.image.load(os.path.join('gameblingPic','gamblingIcon.png')).convert_alpha()
pygame.display.set_icon(icon)
colors = [red,blue,green,yellow,purple]
colorsNames = ['Red','Blue','Green','Yellow','Purple']
horses = []
prob = [[14/50,6/50,10/50,11/50,9/50], [5 / 20, 6 / 20, 3 / 20, 4 / 20, 2 / 20],[8 / 20, 1 / 20, 2 / 20, 6 / 20, 3 / 20], [9/20,1/20,5/20,3/20,2/20],[10/50,15/50,5/50,12/50,8/50]]
step = 10
count = 0
font1 = pygame.font.SysFont(pygame.font.get_fonts()[2],27)
font2 = pygame.font.SysFont(pygame.font.get_fonts()[2],24)
class horse():
    def __init__(self,p,color,n):
        self.p = p
        self.ratio = round(0.65/self.p,1)
        self.placement = 0
        self.counter = 0
        self.color = color
        self.n = n
    def draw(self,win):
        win.blit(pygame.transform.scale(horsesPics[self.n-1], (70,30)),((125+self.placement, 300+75*(self.n-1))))
        #pygame.draw.rect(win, self.color, (125+self.placement, 300+75*(self.n-1), 50, 20))
class card():
    def __init__(self,num,type):
        self.num = num
        self.type = type
        if self.num==1:
            self.name: str = "ace "+self.type
        elif self.num==11:
            self.name: str = "prince "+self.type
        elif self.num==12:
            self.name: str = "queen "+self.type
        elif self.num==13:
            self.name: str = "king "+self.type
        else:
            self.name: str = str(self.num) + " " + self.type
        if self.num>10:
            self.value = 10
        if self.num<=10:
            self.value=self.num
        if self.num==1:
            self.value=11
    def draw(self,win,person,n):
        l,h = 120,180
        k = 0
        if self.type=='clover':
            k = 0
        if self.type=='diamond':
            k = 1
        if self.type=='heart':
            k = 2
        if self.type=='spade':
            k = 3
        if person=="player":
            win.blit(cardsPics[(self.num-1)*4+k],(300+l*n*2/3,500))
        if person=="diller":
            win.blit(cardsPics[(self.num - 1)*4+k],(660-l*n*2/3,225))
class option:
    def __init__(self,num,color):
        self.num = num
        self.color = color
        if num!=0:
            if num % 3 == 0:
                self.row = 3
            elif (num - 2) % 3 == 0:
                self.row = 2
            else:
                self.row = 1
        else:
            self.row = 0
        if num%2==0:
            self.even = True
        else:
            self.even= False
        if num<=12 and num>0:
            self.twelve = 1
        elif num<=24 and num>0:
            self.twelve = 2
        elif num<=36 and num>0:
            self.twelve = 3
        else:
            self.twelve = 0
        if 1<=num and num<=18:
            self.half = 1
        elif 19<=num and num<=36:
            self.half = 2
        else:
            self.half = 0
    def info(self):
        print("num:",self.num,"color:",self.color,"row:",self.row,"even:",self.even,"twelve:",self.twelve)
class rouletteBet():
    def __init__(self,type,value,money,x,y):
        self.type = type
        self.value = value
        self.money = money
        self.x = x
        self.y = y
    def info(self):
        print("type:",self.type,"value:",self.value,"bet",self.money)
    def draw(self,win):
        a = 30
        if self.money == 100:
            win.blit(coin100,(self.x-a*0.5,self.y-a*0.5))
            #pygame.draw.rect(win,black,(self.x-a*0.5,self.y-a*0.5,a,a))
        if self.money == 50:
            win.blit(coin50, (self.x - a * 0.5, self.y - a * 0.5))
            #pygame.draw.rect(win,blue,(self.x-a*0.5,self.y-a*0.5,a,a))
        if self.money == 10:
            win.blit(coin10, (self.x - a * 0.5, self.y - a * 0.5))
            #pygame.draw.rect(win,green,(self.x-a*0.5,self.y-a*0.5,a,a))
        if self.money == 5:
            win.blit(coin5, (self.x - a * 0.5, self.y - a * 0.5))
            #pygame.draw.rect(win,red,(self.x-a*0.5,self.y-a*0.5,a,a))
mode = "Home page"
money = 1000.0
currentMoney = money
totalBet = 0
betRatio = 1
selectedColor = ""
list = []
types = ["spade","clover","heart","diamond"]
cards = []
player = []
diller = []
turn = 1
gameOn = False
bj = 'null'
currentBet = 0
hitCon = False
standCon = False
betCon = False
run = True
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)
def setupHorse():
    global horses,prob,list,selectedColor
    horses = []
    prob = [[14/50,5/50,10/50,12/50,9/50], [5 / 20, 6 / 20, 3 / 20, 4 / 20, 2 / 20],[8 / 20, 1 / 20, 2 / 20, 6 / 20, 3 / 20], [9/20,1/20,5/20,3/20,2/20],[10/50,15/50,5/50,12/50,8/50]]
    josh = randint(0, 4)
    for i in range(0, 5):
        drake = random.choice(prob[josh])
        horses.append(horse(drake,colors[i],i+1))
        prob[josh].remove(drake)
    pp = int(1 / (horses[0].p * horses[1].p * horses[2].p * horses[3].p * horses[4].p))
    list = []
    for k in range(0, len(horses)):
        for i in range(0, int(pp * horses[k].p)):
            list.append(k)
    selectedColor = ""
def noWinner():
    for i in range(0,len(horses)):
        if horses[i].placement >=685:
            return False
    return True
def resetCards():
    global cards,player,diller, turn, hitCon, standCon, bj
    cards = []
    player = []
    diller = []
    for i in range(0, 4, 1):
        for k in range(0, 13, 1):
            cards.append(card(k + 1, types[i]))
    turn = 1
    hitCon = False
    standCon = False
    bj = 'null'
def sumi(list):
    sum = 0
    for i in range(0, len(list)):
        sum = sum+list[i].value
    return sum
def ace(list):
    for i in range(0,len(list)):
        if list[i].value==11:
            return True
    return False
def hit():
    global player,cards,bj,hitCon, gameOn
    roei = random.choice(cards)
    cards.remove(roei)
    player.append(roei)
    if sumi(player) > 21:
        if ace(player)==True:
            for i in range(0, len(player)):
                if player[i].value == 11 and sumi(player) > 21:
                    player[i].value = 1
        else:
            bj = 'lost'
    elif sumi(player) == 21:
        bj = 'win'
    hitCon=False
    gameOn = False
def stand():
    global bj, cards, diller, standCon, gameOn
    if sumi(diller) < 17:
        ron = random.choice(cards)
        cards.remove(ron)
        diller.append(ron)
        if sumi(diller) > 21 and ace(diller) == True:
            for i in range(0, len(diller)):
                if diller[i].value == 11:
                    diller[i].value = 1
    else:
        if sumi(diller) > sumi(player) and sumi(diller) <= 21:
            bj = 'lost'
        if sumi(diller) < sumi(player) or sumi(diller) > 21:
            bj = 'win'
        if sumi(diller) == sumi(player):
            bj = 'draw'
        standCon = False
        gameOn = False
def setupRoulette():
    global options,list2, rouletteBets
    options = []
    for i in range(1,10,2):
        options.append(option(i,"red"))
    for i in range(19,28,2):
        options.append(option(i,"red"))
    for i in range(12,19,2):
        options.append(option(i,"red"))
    for i in range(30,37,2):
        options.append(option(i,"red"))
    for i in range(2,11,2):
        options.append(option(i,"black"))
    for i in range(20, 29, 2):
        options.append(option(i, "black"))
    for i in range(11,18,2):
        options.append(option(i,"black"))
    for i in range(29,36,2):
        options.append(option(i,"black"))
    options.append(option(0,"green"))
    list2 = {0:0,1:32,2:15,3:19,4:4,5:21,6:2,7:25,8:17,9:34,10:6,11:27,12:13,13:36,14:11,15:30,16:8,17:23,18:10,
            19:5,20:24,21:16,22:33,23:1,24:20,25:14,26:31,27:9,28:22,29:18,30:29,31:7,32:28,33:12,34:35,35:3,36:26}
    rouletteBets = []
def checkRoulette():
    global rouletteBets, winnerNum,options
    moneyWon = 0
    for i in range(len(options)):
        if options[i].num==winnerNum:
            num = options[i].num
            color = options[i].color
            row = options[i].row
            even = options[i].even
            twelve = options[i].twelve
            half = options[i].half
            break
    for i in range(len(rouletteBets)):
        if rouletteBets[i].type == "number":
            if num==rouletteBets[i].value:
                moneyWon+=rouletteBets[i].money*35
        if rouletteBets[i].type == "color":
            if color==rouletteBets[i].value:
                moneyWon+=rouletteBets[i].money*2
        if rouletteBets[i].type == "even":
            if even==rouletteBets[i].value:
                moneyWon+=rouletteBets[i].money*2
        if rouletteBets[i].type == "half":
            if half==rouletteBets[i].value:
                moneyWon+=rouletteBets[i].money*2
        if rouletteBets[i].type == "row":
            if row==rouletteBets[i].value:
                moneyWon+=rouletteBets[i].money*3
        if rouletteBets[i].type == "twelve":
            if twelve==rouletteBets[i].value:
                moneyWon+=rouletteBets[i].money*3
    return moneyWon
def spinRoulette():
    global t, w,roulette,spinningRoulette
    #print(-t**3+50*t)
    if (-t**3+20*t)<=0:
        pygame.draw.rect(win,white,(360,210,280,280),2)
        blitRotateCenter(win, roulette, (360, 210), w)
        pygame.draw.circle(win, white, (500, 420), 10)
        return True
    else:
        w +=-t**3+20*t
        t+=0.03
    pygame.draw.rect(win,white,(360,210,280,280),2)
    blitRotateCenter(win,roulette,(360,210),w)
    pygame.draw.circle(win,white,(500,420),10)
def betExists(type,value,bet):
    global rouletteBets,money
    tom = 0
    for c in range(len(rouletteBets)):
        if rouletteBets[c].type==type and rouletteBets[c].value==value:
            tom+=1
            if rouletteBets[c].money!=bet and money>=bet-rouletteBets[c].money:
                money += rouletteBets[c].money
                rouletteBets[c].money = bet
                money -= bet
            elif rouletteBets[c].money==bet:
                money+=rouletteBets[c].money
                rouletteBets.remove(rouletteBets[c])
            break
    if tom>0:
        return True
    elif tom==0 and money>=bet:
        return False
def makeText(str,col,x,y,font):
    if font == 1:
      txt = font1.render(str, 1, col)
    if font == 2:
      txt = font2.render(str, 1, col)
    win.blit(txt,(x,y))
while run:
    if mode == "Home page":
        win.blit(background,(0,0))
        pygame.time.delay(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (700 + 200 > mouse[0] > 700) and (300 + 200 > mouse[1] > 300):
                    mode = "Horse Race"
                    setupHorse()
                    betCon = False
                if (400 + 200 > mouse[0] > 400) and (300 + 200 > mouse[1] > 300):
                    mode = "Blackjack"
                    resetCards()
                    betCon = False
                if (100 + 200 > mouse[0] > 100) and (300 + 200 > mouse[1] > 300):
                    mode = "Roulette"
                    setupRoulette()
                    betCon = False
        pygame.draw.rect(win,white,(100,300,200,200),2)
        if 100+200>mouse[0]>100 and 300+200>mouse[1]>300:
            win.blit(modeRoulette2,(100,300))
        else:
            win.blit(modeRoulette1,(100,300))
        pygame.draw.rect(win, white, (100, 300, 200, 200), 2)
        makeText("Roulette", white, 150, 260, 1)
        if 400+200>mouse[0]>400 and 300+200>mouse[1]>300:
            win.blit(modeBlackjack2,(400,300))
        else:
            win.blit(modeBlackjack1,(400,300))
        pygame.draw.rect(win, white, (400, 300, 200, 200), 2)
        makeText("Blackjack", white, 440, 260, 1)
        if 700+200>mouse[0]>700 and 300+200>mouse[1]>300:
            win.blit(modeHorse2,(700,300))
        else:
            win.blit(modeHorse1,(700,300))
        pygame.draw.rect(win, white, (700, 300, 200, 200), 2)
        makeText("Horse Race", white, 730, 260, 1)
        makeText(str(currentMoney) + '$', white, screenWidth / 2 - 9*len(str(currentMoney)), 10, 1)
    if mode == "Roulette":
        win.blit(background,(0, 0))
        pygame.time.delay(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                #print("x:",mouse[0],"y:",mouse[1])
                if 1000>mouse[0]>0 and 50>mouse[1]>0 and (betCon==False or (betCon==True and spinRoulette()==True)):
                    mode = "Home page"
                    currentBet = 0
                    if betCon==False:
                        money = currentMoney
                    else:
                        money += checkRoulette()
                        currentMoney = money
                        currentBet = 0
                if 220+100>mouse[0]>220 and 500+60>mouse[1]>500:
                    currentBet = 5
                if 220+1*150+100>mouse[0]>220+1*150 and 500+60>mouse[1]>500:
                    currentBet = 10
                if 220+2*150+100>mouse[0]>220+2*150 and 500+60>mouse[1]>500:
                    currentBet = 50
                if 220+3*150+100>mouse[0]>220+3*150 and 500+60>mouse[1]>500:
                    currentBet = 100
                if currentBet!=0:
                    for i in range(12):
                        for q in range(3):
                            if 825-55*i>mouse[0]>825-55*i-50 and 390-56*q>mouse[1]>390-56*q-50:
                                if betExists("number",q+1+3*i,currentBet)==False:
                                    rouletteBets.append(rouletteBet("number",q+1+3*i,currentBet, 800 - 55 * i, 365 - 56 * q))
                                    money -= currentBet
                    if 880>mouse[0]>830 and 390>mouse[1]>225:
                        if betExists("number", 0, currentBet) == False:
                            rouletteBets.append(rouletteBet("number", 0, currentBet, 855, 307))
                            money -= currentBet
                    for i in range(3):
                        if 169>mouse[0]>125 and 390-56*i>mouse[1]>390-56*i-50:
                            if betExists("row", i+1, currentBet) == False:
                                rouletteBets.append(rouletteBet("row", i+1, currentBet,147,365-56*i))
                                money -= currentBet
                        if 825-55*4*i>mouse[0]>825-55*4*i-53*4 and 435>mouse[1]>405:
                            if betExists("twelve", i+1, currentBet) == False:
                                rouletteBets.append(rouletteBet("twelve", i + 1, currentBet,825-55*4*i-53*2,420))
                                money -= currentBet
                    if 820>mouse[0]>720 and 475>mouse[1]>445:
                        if betExists("half", 1, currentBet) == False:
                            rouletteBets.append(rouletteBet("half", 1, currentBet,770,460))
                            money -= currentBet
                    if 715>mouse[0]>605 and 475>mouse[1]>445:
                        if betExists("even", True, currentBet) == False:
                            rouletteBets.append(rouletteBet("even",True, currentBet,660,460))
                            money -= currentBet
                    if 604>mouse[0]>500 and 475>mouse[1]>445:
                        if betExists("color","red", currentBet) == False:
                            rouletteBets.append(rouletteBet("color", "red", currentBet,552,460))
                            money -= currentBet
                    if 495>mouse[0]>395 and 475>mouse[1]>445:
                        if betExists("color", "black", currentBet) == False:
                            rouletteBets.append(rouletteBet("color", "black", currentBet,445,460))
                            money -= currentBet
                    if 390>mouse[0]>285 and 475>mouse[1]>445:
                        if betExists("even", False, currentBet) == False:
                            rouletteBets.append(rouletteBet("even", False, currentBet,337,460))
                            money -= currentBet
                    if 280>mouse[0]>175 and 475>mouse[1]>445:
                        if betExists("half", 2, currentBet) == False:
                            rouletteBets.append(rouletteBet("half", 2, currentBet,227,460))
                            money -= currentBet
                if 450+100>mouse[0]>450 and 590+75>mouse[1]>590 and len(rouletteBets)>0 and betCon==False:
                    betCon = True
                    w = randint(0,359)
                    t = 0.03
                    currentMoney = money
                if 425+150>mouse[0]>425 and 575+75>mouse[1]>575 and betCon==True and spinRoulette()==True:
                    betCon=False
                    money+=checkRoulette()
                    currentMoney = money
                    currentBet = 0
                    rouletteBets = []
        makeText(str(currentMoney) + '$', white, screenWidth / 2 - 9* len(str(currentMoney)), 10, 1)
        pygame.draw.rect(win, white, (100, 200, 800, 500), 5)
        win.blit(rouletteBackground,(100,200))
        #pygame.draw.rect(win, white, (100+20, 200+20, 760, 260), 2)
        if betCon==False:
            win.blit(rouletteBoard, (120, 220))
            if currentBet == 5:
                win.blit(darkButton2, (220 + 0 * 150, 500))
                mark = round((-25 * 0 ** 3) / 6 + 30 * 0 ** 2 - (125 * 0) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 240 + 0 * 150, 510, 1)
            else:
                win.blit(button2, (220 + 0 * 150, 500))
                mark = round((-25 * 0 ** 3) / 6 + 30 * 0 ** 2 - (125 * 0) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 240 + 0 * 150, 510, 1)
            if currentBet == 10:
                win.blit(darkButton2, (220 + 1 * 150, 500))
                mark = round((-25 * 1 ** 3) / 6 + 30 * 1 ** 2 - (125 * 1) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 240 + 1 * 150, 510, 1)
            else:
                win.blit(button2, (220 + 1 * 150, 500))
                mark = round((-25 * 1 ** 3) / 6 + 30 * 1 ** 2 - (125 * 1) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 240 + 1 * 150, 510, 1)
            if currentBet == 50:
                win.blit(darkButton2, (220 + 2 * 150, 500))
                mark = round((-25 * 2 ** 3) / 6 + 30 * 2 ** 2 - (125 * 2) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 235 + 2 * 150, 510, 1)
            else:
                win.blit(button2, (220 + 2 * 150, 500))
                mark = round((-25 * 2 ** 3) / 6 + 30 * 2 ** 2 - (125 * 2) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 235 + 2 * 150, 510, 1)
            if currentBet == 100:
                win.blit(darkButton2, (220 + 3 * 150, 500))
                mark = round((-25 * 3 ** 3) / 6 + 30 * 3 ** 2 - (125 * 3) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 235 + 3 * 150, 510, 1)
            else:
                win.blit(button2, (220 + 3 * 150, 500))
                mark = round((-25 * 3 ** 3) / 6 + 30 * 3 ** 2 - (125 * 3) / 6 + 5, 1)
                makeText(str(mark) + "$", black, 235 + 3 * 150, 510, 1)
            win.blit(button1, (450, 590))
            makeText("spin!", black, 470, 605, 1)
            for i in range(len(rouletteBets)):
                rouletteBets[i].draw(win)
        else:
            if spinRoulette()==True:
                winnerNum = list2[int((w%360) / (360 / 37))]
                makeText("The winning number:"+str(winnerNum),white,355,500,1)
                #print("The winning number:",winnerNum)
                makeText("you won:"+str(checkRoulette())+"$", white, 425, 540, 1)
                #print("you won:",checkRoulette(),"$")
                win.blit(button4,(425,600))
                makeText("Play again", black, 445, 615, 2)
    if mode == "Blackjack":
        win.blit(background,(0, 0))
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (1000 > mouse[0] > 0) and (50 > mouse[1] > 0):
                    if betCon==False:
                        money+=totalBet
                        mode = "Home page"
                        totalBet = 0
                        currentMoney = money
                    elif betCon==True and bj!='null':
                        mode = "Home page"
                        totalBet = 0
                        currentMoney = money
                if (525+100 > mouse[0] > 525) and (400+75 > mouse[1] > 400) and totalBet>0:
                    betCon = True
                    gameOn = True
                    currentMoney=money
                for i in range(0, 4, 1):
                    if (125+100>mouse[0]>125) and (225+85*i+60>mouse[1]>225+85*i) and betCon==False:
                        if i==0 and money>=5:
                            totalBet+=5
                            money-=5
                        if i==1 and money>=10:
                            totalBet+=10
                            money -= 10
                        if i==2 and money>=50:
                            totalBet+=50
                            money -= 50
                        if i==3 and money>=100:
                            totalBet+=100
                            money -= 100
                if (125 + 100 > mouse[0] > 125) and (330 + 75 > mouse[1] > 330) and gameOn==False and bj=='null' and betCon==True:
                    turn += 1
                    gameOn = True
                    hitCon = True
                    standCon = False
                if (125 + 100 > mouse[0] > 125) and (465 + 75 > mouse[1] > 465) and gameOn==False and bj=='null' and betCon==True:
                    turn += 1
                    gameOn = True
                    hitCon = False
                    standCon = True
                if (125 + 100 > mouse[0] > 125) and (600 + 75 > mouse[1] > 600) and gameOn == False and bj!='null' and betCon==True:
                    resetCards()
                    betCon = False
                    currentMoney = money
                    totalBet = 0
                if (100+150 > mouse[0] > 100) and (600+75 > mouse[1] > 600) and betCon == False and bj == 'null':
                    money+=totalBet
                    totalBet=0
        pygame.draw.rect(win, white, (100, 200, 800, 500), 5)
        win.blit(pokerTable,(100,200))
        pygame.draw.line(win, white, (0, 50), (1000, 50), 2)
        makeText(str(currentMoney) + '$', white, screenWidth / 2 - 9*len(str(currentMoney)), 10, 1)
        #pygame.draw.line(win, white, (250, 200), (250, 700), 2)
        if betCon==True:
            if bj == 'null':
                # pygame.draw.rect(win,white,(125,330,100,75))
                win.blit(button1, (125, 330))
                makeText("hit!", black, 155, 350, 1)
                # pygame.draw.rect(win, white, (125, 465, 100, 75))
                win.blit(button1, (125, 465))
                makeText("stand", black, 140, 480, 1)
            if turn==1 and bj=='null':
                if gameOn==True:
                    roei = random.choice(cards)
                    cards.remove(roei)
                    player.append(roei)
                    roei = random.choice(cards)
                    cards.remove(roei)
                    player.append(roei)
                    ron = random.choice(cards)
                    cards.remove(ron)
                    diller.append(ron)
                    if sumi(player) == 21:
                        bj = 'win'
                    gameOn = False
            if turn==2 and bj=='null':
                if gameOn==True and hitCon==True:
                    hit()
                if gameOn==True and standCon==True:
                    stand()
            if turn==3 and bj=='null':
                if gameOn==True and hitCon==True:
                    hit()
                if gameOn==True and standCon==True:
                    stand()
            if turn==4 and bj=='null':
                if gameOn==True and hitCon==True:
                    hit()
                if gameOn==True and standCon==True:
                    stand()
            if turn==5 and bj=='null':
                if gameOn==True and hitCon==True:
                    hit()
                if gameOn==True and standCon==True:
                    stand()
            for i in range(0, len(player)):
                player[i].draw(win, "player", i)
            for i in range(0, len(diller)):
                diller[i].draw(win, "diller", i)
            if bj!='null':
                gameOn = False
                #pygame.draw.rect(win, white, (100, 600, 150, 75))
                win.blit(button4,(100,600))
                makeText("Play again", black, 120, 615, 2)
                if bj=='win':
                    if sumi(player)==21 and turn==1:
                        makeText("You won "+str(totalBet*2.5+totalBet)+"$!",white,515,425,1)
                        if money == currentMoney:
                            money+=totalBet*2.5+totalBet
                    elif sumi(player)==21:
                        makeText("You won " + str(totalBet*2+totalBet) + "$!", white, 515, 425, 1)
                        if money == currentMoney:
                            money += totalBet*2+totalBet
                    else:
                        makeText("You won " + str(totalBet*2) + "$!", white, 515, 425, 1)
                        if money == currentMoney:
                            money += totalBet*2
                if bj=='lost':
                    makeText("You lost " + str(totalBet) + "$.", white, 515, 425, 1)
                if bj=='draw':
                    makeText("Draw, no winner.", white, 515, 425, 1)
                    if money == currentMoney:
                        money += totalBet
        if betCon == False:
            for i in range(0, 4, 1):
                #pygame.draw.rect(win, white, (125, 225 + 85 * i, 100, 60))
                win.blit(button2,(125,225+85*i))
                mark = round((-25*i**3)/6+30*i**2-(125*i)/6 + 5, 1)
                makeText(str(mark) + "$", black, 140, 225 + 85 * i + 10, 1)
            #pygame.draw.rect(win, white, (125, 600, 100, 75))
            win.blit(button1, (125, 600))
            makeText(str(totalBet) + '$', black, 135+10*(4-len(str(totalBet))), 615, 1)
            #pygame.draw.rect(win, white, (525, 400, 100, 75))
            win.blit(button1, (525, 400))
            makeText("Bet!", black, 550, 415, 1)
    if mode == "Horse Race":
        win.blit(background,(0, 0))
        pygame.time.delay(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (450 + 100 > mouse[0] > 450) and (575 + 75 > mouse[1] > 575) and betCon==False and noWinner()==True and betRatio!=1 and totalBet>0:
                    betCon = True
                    currentMoney = money
                if (400 + 150 > mouse[0] > 400) and (575 + 75 > mouse[1] > 575) and noWinner()==False and betCon==True:
                    for i in range(0, 5):
                        horses[i].placement = 0
                    betCon = False
                    count = 0
                    currentMoney = money
                    totalBet = 0
                for i in range(0, 5, 1):
                    if (140+150*i+135>mouse[0]>140+150*i) and (250+50>mouse[1]>250) and noWinner() == True and betCon == False:
                        betRatio = horses[i].ratio
                        selectedColor = colorsNames[i]
                for i in range(0,4,1):
                    if (225+150*i+100>mouse[0]>225+i*150) and (350+60 > mouse[1] > 350) and noWinner() == True and betCon == False:
                        if i==0 and money>=5:
                            totalBet+=5
                            money-=5
                        if i==1 and money>=10:
                            totalBet+=10
                            money -= 10
                        if i==2 and money>=50:
                            totalBet+=50
                            money -= 50
                        if i==3 and money>=100:
                            totalBet+=100
                            money -= 100
                if (450+100 > mouse[0] > 450) and (475 + 75 > mouse[1] > 475) and noWinner()==True and betCon==False:
                    money+=totalBet
                    totalBet=0
                if (1000 > mouse[0] > 0) and (50 > mouse[1] > 0):
                    if betCon==True and noWinner()==False:
                        mode = "Home page"
                        for i in range(0, 5):
                            horses[i].placement = 0
                        count = 0
                        currentMoney = money
                        totalBet = 0
                    if betCon==False:
                        mode = "Home page"
                        for i in range(0, 5):
                            horses[i].placement = 0
                        count = 0
                        money+=totalBet
                        currentMoney = money
                        totalBet = 0
        pygame.draw.rect(win,white,(100,200,800,500),5)
        pygame.draw.line(win,white,(0,50),(1000,50),2)
        win.blit(track,(100,200))
        if betCon == True and mode == "Horse Race":
            #pygame.draw.rect(win, white, (100, 200, 50, 500)) #x,y,width,height
            #pygame.draw.rect(win, white, (850, 200, 50, 500))
            if noWinner()==True:
                for i in range(0, len(horses)):
                    horses[i].placement += step
                if count%10==0:
                    choice = random.choice(list)
                    horses[choice].placement += (1 - horses[choice].p) * step
                count+=1
            else:
                for i in range(0, len(horses)):
                    if max(horses[0].placement, horses[1].placement, horses[2].placement, horses[3].placement,horses[4].placement) == horses[i].placement:
                        josh: str = colorsNames[i]+" "+"horse won."
                        txt2 = font1.render(josh, 1, colors[i])
                        win.blit(txt2,(screenWidth/2-120,screenHeight/2-30))
                        if selectedColor==colorsNames[i]:
                            bob: str = "You won "+str(round(totalBet*betRatio,1))+"$!"
                            makeText(bob,white,screenWidth/2-120,screenHeight/2+40,1)
                            if money == currentMoney:
                                money+=totalBet*betRatio
                        else:
                            bob: str = "You lost " + str(int(totalBet))+"$."
                            makeText(bob, white, screenWidth / 2 - 120, screenHeight / 2 + 40, 1)
                #pygame.draw.rect(win, white, (400, 575, 150, 75))
                win.blit(button4,(400,575))
                makeText("Play again",black,415,590,1)
            for i in range(0, len(horses)):
                horses[i].draw(win)
            makeText(str(currentMoney) + '$', white, screenWidth/2-9*len(str(currentMoney)), 10, 1)
        if betCon == False and mode == "Horse Race":
            for i in range(0,4,1):
                #pygame.draw.rect(win, white, (225+i*150, 350, 100, 60))
                win.blit(button2,(225+i*150,350))
                mark = round((-25*i**3)/6+30*i**2-(125*i)/6+5,1)
                makeText(str(mark)+"$", black, 245+150*i,365, 1)
            for i in range(0, 5, 1):
                if selectedColor==colorsNames[i]:
                    #pygame.draw.rect(win, colors[i], (140 + 150 * i, 250, 135, 50))
                    win.blit(coloredButtonsPics[i],(140+150*i,250))
                    steve: str = colorsNames[i] + ":" + str(horses[i].ratio)
                    if len(steve)>9:
                        makeText(steve, white, 150 + 150 * i, 255, 2)
                    else:
                        makeText(steve, white, 150 + 150 * i, 255, 1)
                else:
                    #pygame.draw.rect(win, white, (140 + 150 * i, 250, 135, 50))
                    win.blit(button3,(140+150*i,250))
                    steve: str = colorsNames[i] + ":" + str(horses[i].ratio)
                    if len(steve) > 9:
                        makeText(steve, colors[i], 150 + 150 * i, 255, 2)
                    else:
                        makeText(steve,colors[i], 150 + 150 * i, 255, 1)
            #pygame.draw.rect(win, white, (450, 475, 100, 75))
            win.blit(button1,(450,475))
            makeText(str(totalBet)+'$', black, 465+10*(4-len(str(totalBet))), 490, 1)
            #pygame.draw.rect(win, white, (450, 575, 100, 75))
            win.blit(button1, (450, 575))
            makeText("Bet!",black,475,590,1)
            makeText(str(currentMoney) + '$', white, screenWidth/2-9*len(str(currentMoney)), 10, 1)
    pygame.display.update()
pygame.quit()