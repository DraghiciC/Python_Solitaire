import pygame
import numpy as np
screen=pygame.display.set_mode((1400,1000))
pygame.init()
pygame.display.set_caption("Solitaire")
clock = pygame.time.Clock()
#initialisaion
_BACK=(pygame.transform.scale(pygame.image.load('PNG\\gray_back.png'),(120,160)),0)
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
R7H=[_BACK,_BACK,_BACK,_BACK,_BACK,_BACK,R7[6]]
R6H=[_BACK,_BACK,_BACK,_BACK,_BACK,R6[5]]
R5H=[_BACK,_BACK,_BACK,_BACK,R5[4]]
R4H=[_BACK,_BACK,_BACK,R4[3]]
R3H=[_BACK,_BACK,R3[2]]
R2H=[_BACK,R2[1]]
R1H=[R1[0]]
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
    draw(BACK,40,20,0)
    draw(C, 240, 20, 0)
    draw(F1, 640, 20, 0)
    draw(F2, 840, 20, 0)
    draw(F3, 1040, 20, 0)
    draw(F4, 1240, 20, 0)
    draw(R1H,40,200)
    draw(R2H, 240, 200)
    draw(R3H, 440, 200)
    draw(R4H, 640, 200)
    draw(R5H, 840, 200)
    draw(R6H, 1040, 200)
    draw(R7H, 1240, 200)
    draw(HAND,x,y,1,0)

def remove(L1,L2):
    for card1 in L1:
        for card2 in L2:
            if card1[1]==card2[1]:
                L2.remove(card2)
    return L2


hcih=False
running=True
crd=0
fr=0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,100,0))
    x, y = pygame.mouse.get_pos()
    drawcards(x,y)
    if event.type==pygame.MOUSEBUTTONDOWN:
        pygame.time.wait(100)
        if event.button==1:
            mx,my=pygame.mouse.get_pos()
            pygame.draw.rect(screen, (255, 0, 0), (mx, my, 15, 15))
            if my < 200:
                if mx>40 and mx <200 and hcih==False:
                    if len(cards)!=0:
                        C=cards[crd:crd+1]
                        crd=crd+1
                        if crd==len(cards):
                            crd=0
                elif mx>240 and mx <400 and hcih==False and crd!=0:
                    HAND=C
                    cards=remove(HAND,cards)
                    fr=0
                    crd=crd-1
                    hcih=True
            if my>200:
                if mx>40 and mx<160 and hcih==False:
                    print("COLUMN 1")
                    poz=(my-200)//40
                    print(poz)
                    if poz<=len(R1H):
                        HAND=R1H[poz:]
                        R1H=remove(HAND,R1H)
                        fr=1
                        hcih=True
                elif mx > 240 and mx < 360 and hcih == False:
                    print("COLUMN 2")
                    poz = (my - 200) // 40
                    print(poz)
                    if poz <= len(R2H):
                        HAND = R2H[poz:]
                        R2H = remove(HAND, R2H)
                        fr = 2
                        hcih = True
                elif mx > 440 and mx < 560 and hcih == False:
                    print("COLUMN 3")
                    poz = (my - 200) // 40
                    print(poz)
                    if poz <= len(R3H):
                        HAND = R3H[poz:]
                        R3H = remove(HAND, R3H)
                        fr = 3
                        hcih = True
                elif mx > 640 and mx < 760 and hcih == False:
                    print("COLUMN 4")
                    poz = (my - 200) // 40
                    print(poz)
                    if poz <= len(R4H):
                        HAND = R4H[poz:]
                        R4H = remove(HAND, R4H)
                        fr = 4
                        hcih = True
                elif mx > 840 and mx < 960 and hcih == False:
                    print("COLUMN 5")
                    poz = (my - 200) // 40
                    print(poz)
                    if poz <= len(R5H):
                        HAND = R5H[poz:]
                        R5H = remove(HAND, R5H)
                        fr = 5
                        hcih = True
                elif mx > 1040 and mx < 1160 and hcih == False:
                    print("COLUMN 6")
                    poz = (my - 200) // 40
                    print(poz)
                    if poz <= len(R6H):
                        HAND = R6H[poz:]
                        R6H = remove(HAND, R6H)
                        fr = 6
                        hcih = True
                elif mx > 1240 and mx < 1360 and hcih == False:
                    print("COLUMN 7")
                    poz = (my - 200) // 40
                    print(poz)
                    if poz <= len(R7H):
                        HAND = R7H[poz:]
                        R7H = remove(HAND, R7H)
                        fr = 7
                        hcih = True






        elif event.button==3 and hcih==True:
            print("test")
            if fr==0:
                cards.insert(crd,HAND[0])
                HAND=[]
                crd=crd+1
                hcih=False
            elif fr==1:
                R1H.extend(HAND)
                HAND=[]
                hcih=False
            elif fr==2:
                R2H.extend(HAND)
                HAND=[]
                hcih=False
            elif fr==3:
                R3H.extend(HAND)
                HAND=[]
                hcih=False
            elif fr==4:
                R4H.extend(HAND)
                HAND=[]
                hcih=False
            elif fr==5:
                R5H.extend(HAND)
                HAND=[]
                hcih=False
            elif fr==6:
                R6H.extend(HAND)
                HAND=[]
                hcih=False
            elif fr==7:
                R7H.extend(HAND)
                HAND=[]
                hcih=False











    pygame.display.update()