import pygame
import numpy as np
screen=pygame.display.set_mode((1400,1000))
pygame.init()
pygame.display.set_caption("Solitaire")
clock = pygame.time.Clock()
#initialisaion
_BACK=(pygame.transform.scale(pygame.image.load('PNG\\gray_back.png'),(120,160)),0)
_sAC=(pygame.transform.scale(pygame.image.load('PNG\\AC.png'),(60,80)),0)
_AC=(pygame.transform.scale(pygame.image.load('PNG\\AC.png'),(120,160)),1)
_2C=(pygame.transform.scale(pygame.image.load('PNG\\2C.png'),(120,160)),2)
_3C=(pygame.transform.scale(pygame.image.load('PNG\\3C.png'),(120,160)),3)
_4C=(pygame.transform.scale(pygame.image.load('PNG\\4C.png'),(120,160)),4)
_5C=(pygame.transform.scale(pygame.image.load('PNG\\5C.png'),(120,160)),5)
_6C=(pygame.transform.scale(pygame.image.load('PNG\\6C.png'),(120,160)),6)
_7C=(pygame.transform.scale(pygame.image.load('PNG\\7C.png'),(120,160)),7)
_8C=(pygame.transform.scale(pygame.image.load('PNG\\8C.png'),(120,160)),8)
_9C=(pygame.transform.scale(pygame.image.load('PNG\\9C.png'),(120,160)),9)
_10C=(pygame.transform.scale(pygame.image.load('PNG\\10C.png'),(120,160)),10)
_JC=(pygame.transform.scale(pygame.image.load('PNG\\JC.png'),(120,160)),11)
_QC=(pygame.transform.scale(pygame.image.load('PNG\\QC.png'),(120,160)),12)
_KC=(pygame.transform.scale(pygame.image.load('PNG\\KC.png'),(120,160)),13)
_sAS=(pygame.transform.scale(pygame.image.load('PNG\\AS.png'),(60,80)),0)
_AS=(pygame.transform.scale(pygame.image.load('PNG\\AS.png'),(120,160)),14)
_2S=(pygame.transform.scale(pygame.image.load('PNG\\2S.png'),(120,160)),15)
_3S=(pygame.transform.scale(pygame.image.load('PNG\\3S.png'),(120,160)),16)
_4S=(pygame.transform.scale(pygame.image.load('PNG\\4S.png'),(120,160)),17)
_5S=(pygame.transform.scale(pygame.image.load('PNG\\5S.png'),(120,160)),18)
_6S=(pygame.transform.scale(pygame.image.load('PNG\\6S.png'),(120,160)),19)
_7S=(pygame.transform.scale(pygame.image.load('PNG\\7S.png'),(120,160)),20)
_8S=(pygame.transform.scale(pygame.image.load('PNG\\8S.png'),(120,160)),21)
_9S=(pygame.transform.scale(pygame.image.load('PNG\\9S.png'),(120,160)),22)
_10S=(pygame.transform.scale(pygame.image.load('PNG\\10S.png'),(120,160)),23)
_JS=(pygame.transform.scale(pygame.image.load('PNG\\JS.png'),(120,160)),24)
_QS=(pygame.transform.scale(pygame.image.load('PNG\\QS.png'),(120,160)),25)
_KS=(pygame.transform.scale(pygame.image.load('PNG\\KS.png'),(120,160)),26)
_sAH=(pygame.transform.scale(pygame.image.load('PNG\\AH.png'),(60,80)),0)
_AH=(pygame.transform.scale(pygame.image.load('PNG\\AH.png'),(120,160)),27)
_2H=(pygame.transform.scale(pygame.image.load('PNG\\2H.png'),(120,160)),28)
_3H=(pygame.transform.scale(pygame.image.load('PNG\\3H.png'),(120,160)),29)
_4H=(pygame.transform.scale(pygame.image.load('PNG\\4H.png'),(120,160)),30)
_5H=(pygame.transform.scale(pygame.image.load('PNG\\5H.png'),(120,160)),31)
_6H=(pygame.transform.scale(pygame.image.load('PNG\\6H.png'),(120,160)),32)
_7H=(pygame.transform.scale(pygame.image.load('PNG\\7H.png'),(120,160)),33)
_8H=(pygame.transform.scale(pygame.image.load('PNG\\8H.png'),(120,160)),34)
_9H=(pygame.transform.scale(pygame.image.load('PNG\\9H.png'),(120,160)),35)
_10H=(pygame.transform.scale(pygame.image.load('PNG\\10H.png'),(120,160)),36)
_JH=(pygame.transform.scale(pygame.image.load('PNG\\JH.png'),(120,160)),37)
_QH=(pygame.transform.scale(pygame.image.load('PNG\\QH.png'),(120,160)),38)
_KH=(pygame.transform.scale(pygame.image.load('PNG\\KH.png'),(120,160)),39)
_sAD=(pygame.transform.scale(pygame.image.load('PNG\\AD.png'),(60,80)),0)
_AD=(pygame.transform.scale(pygame.image.load('PNG\\AD.png'),(120,160)),40)
_2D=(pygame.transform.scale(pygame.image.load('PNG\\2D.png'),(120,160)),41)
_3D=(pygame.transform.scale(pygame.image.load('PNG\\3D.png'),(120,160)),42)
_4D=(pygame.transform.scale(pygame.image.load('PNG\\4D.png'),(120,160)),43)
_5D=(pygame.transform.scale(pygame.image.load('PNG\\5D.png'),(120,160)),44)
_6D=(pygame.transform.scale(pygame.image.load('PNG\\6D.png'),(120,160)),45)
_7D=(pygame.transform.scale(pygame.image.load('PNG\\7D.png'),(120,160)),46)
_8D=(pygame.transform.scale(pygame.image.load('PNG\\8D.png'),(120,160)),47)
_9D=(pygame.transform.scale(pygame.image.load('PNG\\9D.png'),(120,160)),48)
_10D=(pygame.transform.scale(pygame.image.load('PNG\\10D.png'),(120,160)),49)
_JD=(pygame.transform.scale(pygame.image.load('PNG\\JD.png'),(120,160)),50)
_QD=(pygame.transform.scale(pygame.image.load('PNG\\QD.png'),(120,160)),51)
_KD=(pygame.transform.scale(pygame.image.load('PNG\\KD.png'),(120,160)),52)
_GRBACK=(pygame.transform.scale(pygame.image.load('PNG\\green_back.png'),(60,80)),60)

cards=[_AC,_2C,_3C,_4C,_5C,_6C,_7C,_8C,_9C,_10C,_JC,_QC,_KC,_AS,_2S,_3S,_4S,_5S,_6S,_7S,_8S,_9S,_10S,_JS,_QS,_KS,_AH,_2H,_3H,_4H,_5H,_6H,_7H,_8H,_9H,_10H,_JH,_QH,_KH,_AD,_2D,_3D,_4D,_5D,_6D,_7D,_8D,_9D,_10D,_JD,_QD,_KD]
np.random.shuffle(cards)
R1=cards[:1]
cards=cards[1:]
R2=cards[:2]
cards=cards[2:]
R3=cards[:3]
cards=cards[3:]
R4=cards[:4]
cards=cards[4:]
R5=cards[:5]
cards=cards[5:]
R6=cards[:6]
cards=cards[6:]
R7=cards[:7]
cards=cards[7:]
R=[R1,R2,R3,R4,R5,R6,R7]
R7H=[_BACK,_BACK,_BACK,_BACK,_BACK,_BACK,R7[6]]
R6H=[_BACK,_BACK,_BACK,_BACK,_BACK,R6[5]]
R5H=[_BACK,_BACK,_BACK,_BACK,R5[4]]
R4H=[_BACK,_BACK,_BACK,R4[3]]
R3H=[_BACK,_BACK,R3[2]]
R2H=[_BACK,R2[1]]
R1H=[R1[0]]
RH=[R1H,R2H,R3H,R4H,R5H,R6H,R7H]
C=[]
F1=[]
F2=[]
F3=[]
F4=[]
HAND=[]
EMPTY=[]
BACK=[_BACK]
def draw(stack,x,y,c=1,r=1):
    i=0
    l=len(stack)
    if r==1:
        pygame.draw.rect(screen,(0,50,0),(x,y,120,160))
    for card in stack:
        screen.blit(card[0],(x,y+i*40))
        if c==1:
            i=i+1

def drawcards(x,y):
    ######## extra cards
    if len(cards)==0:
        draw(EMPTY,40,20,0)
    else:
        draw(BACK,40,20,0)
    draw(C, 240, 20, 0)
    ######## iconos
    draw([_sAC], 640, 20, 0)
    draw([_sAS], 840, 20, 0)
    draw([_sAH], 1040, 20, 0)
    draw([_sAD], 1240, 20, 0)
    ######## finished stacks
    draw(F1, 640, 20, 0,0)
    draw(F2, 840, 20, 0,0)
    draw(F3, 1040, 20, 0,0)
    draw(F4, 1240, 20, 0,0)
    ######## columns
    draw(RH[0],40,200)
    draw(RH[1], 240, 200)
    draw(RH[2], 440, 200)
    draw(RH[3], 640, 200)
    draw(RH[4], 840, 200)
    draw(RH[5], 1040, 200)
    draw(RH[6], 1240, 200)
    ######## cards in hand
    draw(HAND,x,y,1,0)
    ########
def remove(L1,L2):
    for card1 in L1:
        for card2 in L2:
            if card1[1]==card2[1]:
                L2.remove(card2)
    return L2

def canDrop(L1,L2):
    return True


print(cards)
hcih=False
running=True
crd=-1
fr=0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,100,0))
    x, y = pygame.mouse.get_pos()
    if crd==-1:
        C=[]
    drawcards(x,y)
    if event.type==pygame.MOUSEBUTTONDOWN:
        pygame.time.wait(100)
        if event.button==1:
            mx,my=pygame.mouse.get_pos()
            pygame.draw.rect(screen, (255, 0, 0), (mx, my, 15, 15))
            if my < 200:
                if mx>40 and mx <160 and hcih==False:
                    if len(cards)!=0:
                        if crd==len(cards) or crd<0:
                            crd=-1
                        crd=crd+1
                        C = cards[crd:crd + 1]
                        print(len(cards), crd)
                elif mx>240 and mx <360 and hcih==False and len(cards)>0 and crd>=0:
                    HAND=C
                    fr=0
                    crd = crd - 1
                    if crd<0:
                        C=[]
                    else:
                        C = cards[crd:crd+1]
                    cards = remove(HAND, cards)
                    hcih=True
            if my>200:
                for i in range(7):
                    if mx>40+(200*i) and mx<160+(200*i):
                        print("COLUMN 1")
                        poz=(my-200)//40
                        print(poz)
                        if poz<=len(RH[i]):
                            if hcih == False:
                                HAND=RH[i][poz:]
                                RH[i]=remove(HAND,RH[i])
                                fr=i+1
                                print(fr)
                                hcih=True
                            elif hcih==True and canDrop(HAND,RH[i])==True:
                                RH[i].extend(HAND)
                                HAND=[]
                                hcih=False

        elif event.button==3 and hcih==True:
            print("test",fr)
            if fr==0:
                print(crd,HAND,C,cards)
                crd = crd + 1
                cards.insert(crd,HAND[0])
                C = cards[crd:crd + 1]
                HAND=[]
                print(crd,HAND,C,cards)
                hcih=False
            elif fr<8 and fr>0:
                print(fr,"RH")
                RH[fr-1].extend(HAND)
                HAND=[]
                hcih=False




    pygame.display.update()