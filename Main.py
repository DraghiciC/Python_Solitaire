import pygame
import numpy as np

# initialisaion - loading all the images
def init():
    card_width = 120
    card_height = 160
    _AC = (pygame.transform.scale(pygame.image.load('PNG\\AC.png'), (card_width,card_height)), 1, 1, 0)
    _2C = (pygame.transform.scale(pygame.image.load('PNG\\2C.png'), (card_width,card_height)), 2, 2, 0)
    _3C = (pygame.transform.scale(pygame.image.load('PNG\\3C.png'), (card_width,card_height)), 3, 3, 0)
    _4C = (pygame.transform.scale(pygame.image.load('PNG\\4C.png'), (card_width,card_height)), 4, 4, 0)
    _5C = (pygame.transform.scale(pygame.image.load('PNG\\5C.png'), (card_width,card_height)), 5, 5, 0)
    _6C = (pygame.transform.scale(pygame.image.load('PNG\\6C.png'), (card_width,card_height)), 6, 6, 0)
    _7C = (pygame.transform.scale(pygame.image.load('PNG\\7C.png'), (card_width,card_height)), 7, 7, 0)
    _8C = (pygame.transform.scale(pygame.image.load('PNG\\8C.png'), (card_width,card_height)), 8, 8, 0)
    _9C = (pygame.transform.scale(pygame.image.load('PNG\\9C.png'), (card_width,card_height)), 9, 9, 0)
    _10C = (pygame.transform.scale(pygame.image.load('PNG\\10C.png'), (card_width,card_height)), 10, 10, 0)
    _JC = (pygame.transform.scale(pygame.image.load('PNG\\JC.png'), (card_width,card_height)), 11, 11, 0)
    _QC = (pygame.transform.scale(pygame.image.load('PNG\\QC.png'), (card_width,card_height)), 12, 12, 0)
    _KC = (pygame.transform.scale(pygame.image.load('PNG\\KC.png'), (card_width,card_height)), 13, 13, 0)
    _AS = (pygame.transform.scale(pygame.image.load('PNG\\AS.png'), (card_width,card_height)), 14, 1, 1)
    _2S = (pygame.transform.scale(pygame.image.load('PNG\\2S.png'), (card_width,card_height)), 15, 2, 1)
    _3S = (pygame.transform.scale(pygame.image.load('PNG\\3S.png'), (card_width,card_height)), 16, 3, 1)
    _4S = (pygame.transform.scale(pygame.image.load('PNG\\4S.png'), (card_width,card_height)), 17, 4, 1)
    _5S = (pygame.transform.scale(pygame.image.load('PNG\\5S.png'), (card_width,card_height)), 18, 5, 1)
    _6S = (pygame.transform.scale(pygame.image.load('PNG\\6S.png'), (card_width,card_height)), 19, 6, 1)
    _7S = (pygame.transform.scale(pygame.image.load('PNG\\7S.png'), (card_width,card_height)), 20, 7, 1)
    _8S = (pygame.transform.scale(pygame.image.load('PNG\\8S.png'), (card_width,card_height)), 21, 8, 1)
    _9S = (pygame.transform.scale(pygame.image.load('PNG\\9S.png'), (card_width,card_height)), 22, 9, 1)
    _10S = (pygame.transform.scale(pygame.image.load('PNG\\10S.png'), (card_width,card_height)), 23, 10, 1)
    _JS = (pygame.transform.scale(pygame.image.load('PNG\\JS.png'), (card_width,card_height)), 24, 11, 1)
    _QS = (pygame.transform.scale(pygame.image.load('PNG\\QS.png'), (card_width,card_height)), 25, 12, 1)
    _KS = (pygame.transform.scale(pygame.image.load('PNG\\KS.png'), (card_width,card_height)), 26, 13, 1)
    _AH = (pygame.transform.scale(pygame.image.load('PNG\\AH.png'), (card_width,card_height)), 27, 1, 2)
    _2H = (pygame.transform.scale(pygame.image.load('PNG\\2H.png'), (card_width,card_height)), 28, 2, 2)
    _3H = (pygame.transform.scale(pygame.image.load('PNG\\3H.png'), (card_width,card_height)), 29, 3, 2)
    _4H = (pygame.transform.scale(pygame.image.load('PNG\\4H.png'), (card_width,card_height)), 30, 4, 2)
    _5H = (pygame.transform.scale(pygame.image.load('PNG\\5H.png'), (card_width,card_height)), 31, 5, 2)
    _6H = (pygame.transform.scale(pygame.image.load('PNG\\6H.png'), (card_width,card_height)), 32, 6, 2)
    _7H = (pygame.transform.scale(pygame.image.load('PNG\\7H.png'), (card_width,card_height)), 33, 7, 2)
    _8H = (pygame.transform.scale(pygame.image.load('PNG\\8H.png'), (card_width,card_height)), 34, 8, 2)
    _9H = (pygame.transform.scale(pygame.image.load('PNG\\9H.png'), (card_width,card_height)), 35, 9, 2)
    _10H = (pygame.transform.scale(pygame.image.load('PNG\\10H.png'), (card_width,card_height)), 36, 10, 2)
    _JH = (pygame.transform.scale(pygame.image.load('PNG\\JH.png'), (card_width,card_height)), 37, 11, 2)
    _QH = (pygame.transform.scale(pygame.image.load('PNG\\QH.png'), (card_width,card_height)), 38, 12, 2)
    _KH = (pygame.transform.scale(pygame.image.load('PNG\\KH.png'), (card_width,card_height)), 39, 13, 2)
    _AD = (pygame.transform.scale(pygame.image.load('PNG\\AD.png'), (card_width,card_height)), 40, 1, 3)
    _2D = (pygame.transform.scale(pygame.image.load('PNG\\2D.png'), (card_width,card_height)), 41, 2, 3)
    _3D = (pygame.transform.scale(pygame.image.load('PNG\\3D.png'), (card_width,card_height)), 42, 3, 3)
    _4D = (pygame.transform.scale(pygame.image.load('PNG\\4D.png'), (card_width,card_height)), 43, 4, 3)
    _5D = (pygame.transform.scale(pygame.image.load('PNG\\5D.png'), (card_width,card_height)), 44, 5, 3)
    _6D = (pygame.transform.scale(pygame.image.load('PNG\\6D.png'), (card_width,card_height)), 45, 6, 3)
    _7D = (pygame.transform.scale(pygame.image.load('PNG\\7D.png'), (card_width,card_height)), 46, 7, 3)
    _8D = (pygame.transform.scale(pygame.image.load('PNG\\8D.png'), (card_width,card_height)), 47, 8, 3)
    _9D = (pygame.transform.scale(pygame.image.load('PNG\\9D.png'), (card_width,card_height)), 48, 9, 3)
    _10D = (pygame.transform.scale(pygame.image.load('PNG\\10D.png'), (card_width,card_height)), 49, 10, 3)
    _JD = (pygame.transform.scale(pygame.image.load('PNG\\JD.png'), (card_width,card_height)), 50, 11, 3)
    _QD = (pygame.transform.scale(pygame.image.load('PNG\\QD.png'), (card_width,card_height)), 51, 12, 3)
    _KD = (pygame.transform.scale(pygame.image.load('PNG\\KD.png'), (card_width,card_height)), 52, 13, 3)
    _BACK = (pygame.transform.scale(pygame.image.load('PNG\\gray_back.png'), (card_width,card_height)), 0, 0, 0)
    return [_AC, _2C, _3C, _4C, _5C, _6C, _7C, _8C, _9C, _10C, _JC, _QC, _KC, _AS, _2S, _3S, _4S, _5S, _6S, _7S, _8S, _9S,
             _10S, _JS, _QS, _KS, _AH, _2H, _3H, _4H, _5H, _6H, _7H, _8H, _9H, _10H, _JH, _QH, _KH, _AD, _2D, _3D, _4D, _5D,
             _6D, _7D, _8D, _9D, _10D, _JD, _QD, _KD] , _BACK

# shuffle and arrange cards
def arrange_cards(cards,_BACK):
    np.random.shuffle(cards)
    R = [[] for i in range(0,7)] # the values of the cards in each column
    for i in range(0,7):
        R[i] = cards[:i+1]
        cards = cards[i+1:]
    RH = [[] for i in range(0, 7)] # the columns of cards as they should be drawn (face-up or face-down)
    for i in range(0,7):
        for j in range(0,i):
            RH[i].append(_BACK)
        RH[i].append(R[i][i])
    C = [] # card displayed in the waste pile
    F = [[], [], [], []] # cards displayed in foundations (4 top right rectangles)
    HAND = [] # card or cards in hand
    EMPTY = [] # for drawing the empty draw pile
    BACK = [_BACK] # the back of the cards
    return C, F, HAND, EMPTY, BACK, R, RH, cards

# function that draws a card stack at given (x,y) coordinates
def draw(stack, x1, y1, c=1, r=1):
    j = 0
    if r == 1:
        pygame.draw.rect(screen, (0, 50, 0), (x1, y1, 120, 160))
    for card in stack:
        screen.blit(card[0], (x1, y1 + j * 40))
        if c == 1:
            j = j + 1

# draw all card piles
def drawcards(x_hnd, y_hnd):

    # display the draw pile
    if len(cards) == 0:
        draw(EMPTY, 40, 20, 0)
    else:
        draw(BACK, 40, 20, 0)

    # draw the card in the waste pile
    draw(C, 240, 20, 0)

    # display foundations
    for i in range(0,4):
        draw(F[i],640+i*200,20,0)

    # display card columns
    for i in range(0,7):
        draw(RH[i],40+i*200,200)

    # display card or cards in hand
    draw(HAND, x_hnd, y_hnd, 1, 0)

# remove card or stack of cards from list
def remove(l1, l2):
    for card1 in l1:
        for card2 in l2:
            if card1[1] == card2[1]:
                l2.remove(card2)
    return l2

# check if the stack of cards in hand can be placed down on another stack or empty space
def can_drop(hand, l2):
    if len(l2) > 0: # check where the cards in hand try to be placed
        # if placed on a stack of one or more cards
        if l2[-1][2] == hand[0][2] + 1: # check if the value of the bottom card in hand is 1 less than the value on top of the stack
            if l2[-1][3] <= 1 and hand[0][3] >= 2: # if trying to place red card on black card
                return True
            elif l2[-1][3] >= 2 and hand[0][3] <= 1: # if trying to place black card on red card
                return True
            else: # if the cards have the same color
                return False
    # if placed on an empty stack
    elif hand[0][2] == 13: # check if the bottom card in hand is a K
        return True
    else:
        return False

# check if the game is won
def check_win(F):
    if len(F[0]) == len(F[1]) == len(F[2]) == len(F[3]) == 13:
        img = font.render('YOU WON!', True, (180, 0, 0))
        screen.blit(img, (0, 400))
        pygame.display.update()
        pygame.time.wait(5000)
        return True
    return False

# fucntion to check if "give up" buton is pressed
def give_up(x,y):
    if y < 200:
        if 440 < x < 560 and 53 < y < 103:  # give up button
            img = font.render('YOU LOST', True, (180, 0, 0))
            screen.blit(img, (0, 400))
            pygame.display.update()
            pygame.time.wait(4000)
            return True

# clicked card pile
def click_card_pile(x,y):
    if y < 200 and 40 < x <160:
        return True
    return False

# flip from card pile
def flip_from_pile(crd,cards,C):
    if hcih is False:  # flip next card
        if len(cards) != 0:
            if crd == len(cards) or crd < 0:
                crd = -1
            crd = crd + 1
            C = cards[crd:crd + 1]
    return crd,C

# clicked waste pile
def click_waste_pile(x,y):
    if y < 200 and 240 < x < 360:
        return True
    return False

# pick up card from waste pile
def pick_up_card_from_waste_pile(hcih,cards,crd,HAND,C,fr):
    if hcih is False and len(cards) > 0 and crd >= 0:  # pick up card
        HAND = C
        fr = 0
        crd = crd - 1
        cards = remove(HAND, cards)
        if crd < 0:
            C = []
        else:
            C = cards[crd:crd + 1]
        hcih = True
    return hcih,cards,crd,HAND,C,fr

# clicked final piles
def click_final_piles(x,y):
    if y < 200:
        for i in range(4):  # drop card in hand to final piles
            if 640 + (200 * i) < x < 760 + (200 * i):
                return i
    return -1

# put card in final piles
def put_card_in_final_piles(i,hcih,HAND,F):
    if hcih is True and len(HAND) == 1: # check if there is a single a card in hand
        if len(F[i]) == 0: # check fi final pile is empty
            if HAND[0][2] == 1: # check if the card in hand is an ace
                F[i].extend(HAND)
                HAND = []
                hcih = False
        elif HAND[0][2] == F[i][-1][2] + 1 and HAND[0][3] == F[i][-1][3]: # check if the card can be put on the final pile
            F[i].extend(HAND)
            HAND = []
            hcih = False
    return hcih,HAND,F

# clicked card piles
def click_card_piles(x,y):
    if y > 200:
        for i in range(7):  # drop card in hand to final piles
            if 40 + (200 * i) < x < 160 + (200 * i):
                return i
    return -1

# take/add cards to the card piles
def card_piles(y,i,hcih,HAND,RH,fr):
    poz = (y - 200) // 40 # check which card from the pile was clicked
    if len(RH[i]) + 3 > poz >= len(RH[i]): # check bigger area for the top card
        poz = len(RH[i]) - 1
    if poz <= len(RH[i]):
        if hcih is False and len(RH[i]) != 0: # if hand is empty and there are cards in the pile
            if RH[i][poz][1] != 0: # if the card is face-up
                HAND = RH[i][poz:]
                RH[i] = remove(HAND, RH[i])
                fr = i + 1
                hcih = True
        elif hcih and can_drop(HAND, RH[i]):
            RH[i].extend(HAND)
            HAND = []
            hcih = False
    return hcih,HAND,RH,fr

# return cards from hand
def return_cards(fr,crd,C,HAND,hcih,RH):
    if fr == 0:  # return to waste pile
        crd = crd + 1
        cards.insert(crd, HAND[0])
        C = cards[crd:crd + 1]
        HAND = []
        hcih = False
    elif 8 > fr > 0:  # return to card piles
        RH[fr - 1].extend(HAND)
        HAND = []
        hcih = False
    return fr,crd,C,HAND,hcih,RH

# reveal cards from card piles
def reveal_cards(hcih,RH,R):
    if hcih is False:  # revealing new cards
        for i in range(7):
            if len(RH[i]) > 0:
                if RH[i][-1][1] == 0:
                    # print(i)
                    RH[i][-1] = R[i][-2]
                    R[i].pop()
    return RH,R
# function to handle all mouse events
def handle_events(running,x,y,hcih,cards,crd,C,HAND,RH,R,fr,F):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the window is closed
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.time.wait(100)
            if event.button == 1: # if pressed left click
                cfp = click_final_piles(x,y)
                ccp = click_card_piles(x,y)
                if give_up(x,y) == True:
                    running = False
                elif click_card_pile(x,y):
                    crd,C = flip_from_pile(crd,cards,C)
                elif click_waste_pile(x,y):
                    hcih,cards,crd,HAND,C,fr = pick_up_card_from_waste_pile(hcih,cards,crd,HAND,C,fr)
                elif cfp != -1:
                    hcih,HAND,F = put_card_in_final_piles(cfp,hcih,HAND,F)
                elif ccp != -1:
                    hcih,HAND,RH,fr = card_piles(y,ccp,hcih,HAND,RH,fr)
            elif event.button == 3 and hcih is True: # if pressed right click
                fr,crd,C,HAND,hcih,RH = return_cards(fr,crd,C,HAND,hcih,RH)

        RH,R = reveal_cards(hcih,RH,R)  # reveal cards after a move (if necessary )
    return running,hcih,cards,crd,C,HAND,RH,R,fr,F


screen = pygame.display.set_mode((1400, 1000))
pygame.init()
pygame.display.set_caption("Solitaire")
clock = pygame.time.Clock()
font2 = pygame.font.SysFont(None, 45)
img = font2.render('GIVE UP', True, (180, 0, 0))
font = pygame.font.SysFont(None, 375)

cards , _BACK = init()  # loading the images
C, F, HAND, EMPTY, BACK, R, RH, cards = arrange_cards(cards,_BACK)  # shuffle and arrange cards
hcih = False # has card in hand = false
running = True # main loop is running = true
crd = -1
fr = 0 # current pile of hand cards, used to cancel move by right click

# main game loop
while running:
    clock.tick(60)
    screen.fill((0, 100, 0))
    x, y = pygame.mouse.get_pos() # get position in order to draw cards in hand and handle mouse events
    if crd == -1:
        C = []
    drawcards(x, y)
    running,hcih,cards,crd,C,HAND,RH,R,fr,F = handle_events(running,x,y,hcih,cards,crd,C,HAND,RH,R,fr,F)
    pygame.draw.rect(screen, (35, 35, 35), (440, 53, 120, 50))
    screen.blit(img, (440, 65))

    # end the game if the player won
    if (check_win(F)) == True:
        running = False
    pygame.display.update()
