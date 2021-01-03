import pygame
import numpy as np

screen = pygame.display.set_mode((1400, 1000))
pygame.init()
pygame.display.set_caption("Solitaire")
clock = pygame.time.Clock()
# initialisaion
_BACK = (pygame.transform.scale(pygame.image.load('PNG\\gray_back.png'), (120, 160)), 0, 0, 0)
_sAC = (pygame.transform.scale(pygame.image.load('PNG\\AC.png'), (60, 80)), 0, 0, 0)
_AC = (pygame.transform.scale(pygame.image.load('PNG\\AC.png'), (120, 160)), 1, 1, 0)
_2C = (pygame.transform.scale(pygame.image.load('PNG\\2C.png'), (120, 160)), 2, 2, 0)
_3C = (pygame.transform.scale(pygame.image.load('PNG\\3C.png'), (120, 160)), 3, 3, 0)
_4C = (pygame.transform.scale(pygame.image.load('PNG\\4C.png'), (120, 160)), 4, 4, 0)
_5C = (pygame.transform.scale(pygame.image.load('PNG\\5C.png'), (120, 160)), 5, 5, 0)
_6C = (pygame.transform.scale(pygame.image.load('PNG\\6C.png'), (120, 160)), 6, 6, 0)
_7C = (pygame.transform.scale(pygame.image.load('PNG\\7C.png'), (120, 160)), 7, 7, 0)
_8C = (pygame.transform.scale(pygame.image.load('PNG\\8C.png'), (120, 160)), 8, 8, 0)
_9C = (pygame.transform.scale(pygame.image.load('PNG\\9C.png'), (120, 160)), 9, 9, 0)
_10C = (pygame.transform.scale(pygame.image.load('PNG\\10C.png'), (120, 160)), 10, 10, 0)
_JC = (pygame.transform.scale(pygame.image.load('PNG\\JC.png'), (120, 160)), 11, 11, 0)
_QC = (pygame.transform.scale(pygame.image.load('PNG\\QC.png'), (120, 160)), 12, 12, 0)
_KC = (pygame.transform.scale(pygame.image.load('PNG\\KC.png'), (120, 160)), 13, 13, 0)
_sAS = (pygame.transform.scale(pygame.image.load('PNG\\AS.png'), (60, 80)), 0, 0, 0)
_AS = (pygame.transform.scale(pygame.image.load('PNG\\AS.png'), (120, 160)), 14, 1, 1)
_2S = (pygame.transform.scale(pygame.image.load('PNG\\2S.png'), (120, 160)), 15, 2, 1)
_3S = (pygame.transform.scale(pygame.image.load('PNG\\3S.png'), (120, 160)), 16, 3, 1)
_4S = (pygame.transform.scale(pygame.image.load('PNG\\4S.png'), (120, 160)), 17, 4, 1)
_5S = (pygame.transform.scale(pygame.image.load('PNG\\5S.png'), (120, 160)), 18, 5, 1)
_6S = (pygame.transform.scale(pygame.image.load('PNG\\6S.png'), (120, 160)), 19, 6, 1)
_7S = (pygame.transform.scale(pygame.image.load('PNG\\7S.png'), (120, 160)), 20, 7, 1)
_8S = (pygame.transform.scale(pygame.image.load('PNG\\8S.png'), (120, 160)), 21, 8, 1)
_9S = (pygame.transform.scale(pygame.image.load('PNG\\9S.png'), (120, 160)), 22, 9, 1)
_10S = (pygame.transform.scale(pygame.image.load('PNG\\10S.png'), (120, 160)), 23, 10, 1)
_JS = (pygame.transform.scale(pygame.image.load('PNG\\JS.png'), (120, 160)), 24, 11, 1)
_QS = (pygame.transform.scale(pygame.image.load('PNG\\QS.png'), (120, 160)), 25, 12, 1)
_KS = (pygame.transform.scale(pygame.image.load('PNG\\KS.png'), (120, 160)), 26, 13, 1)
_sAH = (pygame.transform.scale(pygame.image.load('PNG\\AH.png'), (60, 80)), 0, 0, 0)
_AH = (pygame.transform.scale(pygame.image.load('PNG\\AH.png'), (120, 160)), 27, 1, 2)
_2H = (pygame.transform.scale(pygame.image.load('PNG\\2H.png'), (120, 160)), 28, 2, 2)
_3H = (pygame.transform.scale(pygame.image.load('PNG\\3H.png'), (120, 160)), 29, 3, 2)
_4H = (pygame.transform.scale(pygame.image.load('PNG\\4H.png'), (120, 160)), 30, 4, 2)
_5H = (pygame.transform.scale(pygame.image.load('PNG\\5H.png'), (120, 160)), 31, 5, 2)
_6H = (pygame.transform.scale(pygame.image.load('PNG\\6H.png'), (120, 160)), 32, 6, 2)
_7H = (pygame.transform.scale(pygame.image.load('PNG\\7H.png'), (120, 160)), 33, 7, 2)
_8H = (pygame.transform.scale(pygame.image.load('PNG\\8H.png'), (120, 160)), 34, 8, 2)
_9H = (pygame.transform.scale(pygame.image.load('PNG\\9H.png'), (120, 160)), 35, 9, 2)
_10H = (pygame.transform.scale(pygame.image.load('PNG\\10H.png'), (120, 160)), 36, 10, 2)
_JH = (pygame.transform.scale(pygame.image.load('PNG\\JH.png'), (120, 160)), 37, 11, 2)
_QH = (pygame.transform.scale(pygame.image.load('PNG\\QH.png'), (120, 160)), 38, 12, 2)
_KH = (pygame.transform.scale(pygame.image.load('PNG\\KH.png'), (120, 160)), 39, 13, 2)
_sAD = (pygame.transform.scale(pygame.image.load('PNG\\AD.png'), (60, 80)), 0, 0, 0)
_AD = (pygame.transform.scale(pygame.image.load('PNG\\AD.png'), (120, 160)), 40, 1, 3)
_2D = (pygame.transform.scale(pygame.image.load('PNG\\2D.png'), (120, 160)), 41, 2, 3)
_3D = (pygame.transform.scale(pygame.image.load('PNG\\3D.png'), (120, 160)), 42, 3, 3)
_4D = (pygame.transform.scale(pygame.image.load('PNG\\4D.png'), (120, 160)), 43, 4, 3)
_5D = (pygame.transform.scale(pygame.image.load('PNG\\5D.png'), (120, 160)), 44, 5, 3)
_6D = (pygame.transform.scale(pygame.image.load('PNG\\6D.png'), (120, 160)), 45, 6, 3)
_7D = (pygame.transform.scale(pygame.image.load('PNG\\7D.png'), (120, 160)), 46, 7, 3)
_8D = (pygame.transform.scale(pygame.image.load('PNG\\8D.png'), (120, 160)), 47, 8, 3)
_9D = (pygame.transform.scale(pygame.image.load('PNG\\9D.png'), (120, 160)), 48, 9, 3)
_10D = (pygame.transform.scale(pygame.image.load('PNG\\10D.png'), (120, 160)), 49, 10, 3)
_JD = (pygame.transform.scale(pygame.image.load('PNG\\JD.png'), (120, 160)), 50, 11, 3)
_QD = (pygame.transform.scale(pygame.image.load('PNG\\QD.png'), (120, 160)), 51, 12, 3)
_KD = (pygame.transform.scale(pygame.image.load('PNG\\KD.png'), (120, 160)), 52, 13, 3)
_GRBACK = (pygame.transform.scale(pygame.image.load('PNG\\green_back.png'), (60, 80)), 60, 0, 0)

cards = [_AC, _2C, _3C, _4C, _5C, _6C, _7C, _8C, _9C, _10C, _JC, _QC, _KC, _AS, _2S, _3S, _4S, _5S, _6S, _7S, _8S, _9S,
         _10S, _JS, _QS, _KS, _AH, _2H, _3H, _4H, _5H, _6H, _7H, _8H, _9H, _10H, _JH, _QH, _KH, _AD, _2D, _3D, _4D, _5D,
         _6D, _7D, _8D, _9D, _10D, _JD, _QD, _KD]

np.random.shuffle(cards)
R1 = cards[:1]
cards = cards[1:]
R2 = cards[:2]
cards = cards[2:]
R3 = cards[:3]
cards = cards[3:]
R4 = cards[:4]
cards = cards[4:]
R5 = cards[:5]
cards = cards[5:]
R6 = cards[:6]
cards = cards[6:]
R7 = cards[:7]
cards = cards[7:]
R = [R1, R2, R3, R4, R5, R6, R7]
R7H = [_BACK, _BACK, _BACK, _BACK, _BACK, _BACK, R7[6]]
R6H = [_BACK, _BACK, _BACK, _BACK, _BACK, R6[5]]
R5H = [_BACK, _BACK, _BACK, _BACK, R5[4]]
R4H = [_BACK, _BACK, _BACK, R4[3]]
R3H = [_BACK, _BACK, R3[2]]
R2H = [_BACK, R2[1]]
R1H = [R1[0]]
RH = [R1H, R2H, R3H, R4H, R5H, R6H, R7H]
C = []
F = [[], [], [], []]
HAND = []
EMPTY = []
BACK = [_BACK]


def draw(stack, x1, y1, c=1, r=1):
    j = 0
    if r == 1:
        pygame.draw.rect(screen, (0, 50, 0), (x1, y1, 120, 160))
    for card in stack:
        screen.blit(card[0], (x1, y1 + j * 40))
        if c == 1:
            j = j + 1


def drawcards(x_hnd, y_hnd):
    # extra cards
    if len(cards) == 0:
        draw(EMPTY, 40, 20, 0)
    else:
        draw(BACK, 40, 20, 0)
    draw(C, 240, 20, 0)
    # finished stacks
    draw(F[0], 640, 20, 0)
    draw(F[1], 840, 20, 0)
    draw(F[2], 1040, 20, 0)
    draw(F[3], 1240, 20, 0)
    # columns
    draw(RH[0], 40, 200)
    draw(RH[1], 240, 200)
    draw(RH[2], 440, 200)
    draw(RH[3], 640, 200)
    draw(RH[4], 840, 200)
    draw(RH[5], 1040, 200)
    draw(RH[6], 1240, 200)
    # cards in hand
    draw(HAND, x_hnd, y_hnd, 1, 0)
    #


def remove(l1, l2):
    for card1 in l1:
        for card2 in l2:
            if card1[1] == card2[1]:
                l2.remove(card2)
    return l2


def can_drop(hand, l2):
    if len(l2) > 0:
        print(l2[-1][2])
        print(hand[0][2])
        if l2[-1][2] == hand[0][2] + 1:
            if l2[-1][3] <= 1 and hand[0][3] >= 2:
                return True
            elif l2[-1][3] >= 2 and hand[0][3] <= 1:
                return True
            else:
                return False
    elif hand[0][2] == 13:
        return True
    else:
        return False

font2 = pygame.font.SysFont(None, 45)
img = font2.render('GIVE UP', True, (180,0,0))
font = pygame.font.SysFont(None, 400)
print(cards)
hcih = False
running = True
crd = -1
fr = 0
while running:
    clock.tick(60)
    screen.fill((0, 100, 0))
    x, y = pygame.mouse.get_pos()
    if crd == -1:
        C = []
    drawcards(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.wait(100)
            if event.button == 1:
                mx, my = pygame.mouse.get_pos()
                #pygame.draw.rect(screen, (255, 0, 0), (mx, my, 15, 15))
                if my < 200:
                    if 440<mx<560 and 53<my<103:
                        img = font.render('YOU LOST', True, (180, 0, 0))
                        screen.blit(img, (0, 400))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        running = False
                    elif hcih is False and 40 < mx < 160:
                        if len(cards) != 0:
                            if crd == len(cards) or crd < 0:
                                crd = -1
                            crd = crd + 1
                            C = cards[crd:crd + 1]
                            # print(len(cards), crd)
                    elif 240 < mx < 360 and hcih is False and len(cards) > 0 and crd >= 0:
                        HAND = C
                        fr = 0
                        crd = crd - 1
                        if crd < 0:
                            C = []
                        else:
                            C = cards[crd:crd + 1]
                        cards = remove(HAND, cards)
                        hcih = True
                    else:
                        for i in range(4):
                            if 640 + (200 * i) < mx < 760 + (200 * i) and hcih is True:
                                if len(HAND) == 1:
                                    if len(F[i]) == 0:
                                        if HAND[0][2] == 1:
                                            F[i].extend(HAND)
                                            HAND = []
                                            hcih = False
                                    elif HAND[0][2] == F[i][-1][2] + 1 and HAND[0][3] == F[i][-1][3]:
                                        F[i].extend(HAND)
                                        HAND = []
                                        hcih = False
                if my > 200:
                    for i in range(7):
                        if 40 + (200 * i) < mx < 160 + (200 * i):
                            # print("COLUMN 1")
                            poz = (my - 200) // 40
                            # print(poz, len(RH[i]))
                            if len(RH[i]) + 3 > poz >= len(RH[i]):
                                poz = len(RH[i]) - 1
                            # print(poz, len(RH[i]))
                            if poz <= len(RH[i]):
                                if hcih is False and len(RH[i]) != 0:
                                    if RH[i][poz][1] != 0:
                                        HAND = RH[i][poz:]
                                        RH[i] = remove(HAND, RH[i])
                                        fr = i + 1
                                        hcih = True
                                elif hcih is True and can_drop(HAND, RH[i]) is True:
                                    RH[i].extend(HAND)
                                    HAND = []
                                    hcih = False

            elif event.button == 3 and hcih is True:
                if fr == 0:
                    # print(crd, HAND, C, cards)
                    crd = crd + 1
                    cards.insert(crd, HAND[0])
                    C = cards[crd:crd + 1]
                    HAND = []
                    # print(crd, HAND, C, cards)
                    hcih = False
                elif 8 > fr > 0:
                    RH[fr - 1].extend(HAND)
                    HAND = []
                    hcih = False
            # revealing new cards
        if hcih is False:
            for i in range(7):
                if len(RH[i]) > 0:
                    if RH[i][-1][1] == 0:
                        # print(i)
                        RH[i][-1] = R[i][-2]
                        R[i].pop()
    pygame.draw.rect(screen, (35, 35, 35), (440, 53, 120, 50))
    screen.blit(img, (440, 65))
    #if F[0][-1][2] == F[1][-1][2] == F[2][-1][2] == F[3][-1][2] == 13:
    if len(F[0]) == len(F[1]) == len(F[2]) == len(F[3]) == 13:
        img = font.render('YOU WON!', True, (180, 0, 0))
        screen.blit(img, (0, 400))
        pygame.display.update()
        pygame.time.wait(5000)
        running = False
    pygame.display.update()
