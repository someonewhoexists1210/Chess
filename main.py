import pygame
import os, sys
import time

#Pygame Intialization
pygame.font.init()
WID,HEI = 400,400
WIN = pygame.display.set_mode((WID,HEI))
pygame.display.set_caption('Chess')


abcs = 'abcdefgh'

boardpositions = {
'a1': (0,350),
'a2': (0,300),
'a3': (0,250),
'a4': (0,200),
'a5': (0,150),
'a6': (0,100),
'a7': (0,50),
'a8': (0,0),

'b1': (50,350),
'b2': (50,300),
'b3': (50,250),
'b4': (50,200),
'b5': (50,150),
'b6': (50,100),
'b7': (50,50),
'b8': (50,0),

'c1': (100,350),
'c2': (100,300),
'c3': (100,250),
'c4': (100,200),
'c5': (100,150),
'c6': (100,100),
'c7': (100,50),
'c8': (100,0),

'd1': (150,350),
'd2': (150,300),
'd3': (150,250),
'd4': (150,200),
'd5': (150,150),
'd6': (150,100),
'd7': (150,50),
'd8': (150,0),

'e1': (200,350),
'e2': (200,300),
'e3': (200,250),
'e4': (200,200),
'e5': (200,150),
'e6': (200,100),
'e7': (200,50),
'e8': (200,0),

'f1': (250,350),
'f2': (250,300),
'f3': (250,250),
'f4': (250,200),
'f5': (250,150),
'f6': (250,100),
'f7': (250,50),
'f8': (250,0),

'g1': (300,350),
'g2': (300,300),
'g3': (300,250),
'g4': (300,200),
'g5': (300,150),
'g6': (300,100),
'g7': (300,50),
'g8': (300,0),

'h1': (350,350),
'h2': (350,300),
'h3': (350,250),
'h4': (350,200),
'h5': (350,150),
'h6': (350,100),
'h7': (350,50),
'h8': (350,0)
}

# Images
BPAWN = pygame.transform.scale(pygame.image.load('imgs/blpawn.png'), (50,50))
BROOK = pygame.transform.scale(pygame.image.load('imgs/blrook.png'), (50,50))
BKNIGHT = pygame.transform.scale(pygame.image.load('imgs/blknight.png'), (50,50))
BBISHOP = pygame.transform.scale(pygame.image.load('imgs/blbishop.png'), (50,50))
BQUEEN = pygame.transform.scale(pygame.image.load('imgs/blqueen.png'), (50,50))
BKING = pygame.transform.scale(pygame.image.load('imgs/blking.png'), (50,50))

WPAWN = pygame.transform.scale(pygame.image.load('imgs/wpawn.png'), (50,50))
WROOK = pygame.transform.scale(pygame.image.load('imgs/wrook.png'), (50,50))
WKNIGHT = pygame.transform.scale(pygame.image.load('imgs/wknight.png'), (50,50))
WBISHOP = pygame.transform.scale(pygame.image.load('imgs/wbishop.png'), (50,50))
WQUEEN = pygame.transform.scale(pygame.image.load('imgs/wqueen.png'), (50,50))
WKING = pygame.transform.scale(pygame.image.load('imgs/wking.png'), (50,50))


edit = lambda sq : [sq[0],int(sq[1])]
join = lambda a : a[0] + str(a[1])











#Board Initialization
for i in range(0,8):
    for n in range(8):
        if i%2==0:
            if n%2==1:
                pygame.draw.rect(WIN, (0,153,51), (n*50,i*50,50,50))
            else:
                pygame.draw.rect(WIN, (255,255,255), (n*50,i*50,50,50))
        else:
            if n%2==0:
                pygame.draw.rect(WIN, (0,153,51), (n*50,i*50,50,50))
            else:
                pygame.draw.rect(WIN, (255,255,255), (n*50,i*50,50,50))

               
pygame.display.update()

for m in range(0, 8):
    WIN.blit(BPAWN, boardpositions[abcs[m]+'7'])  
WIN.blit(BROOK, boardpositions['a8'])
WIN.blit(BROOK, boardpositions['h8'])
WIN.blit(BKNIGHT, boardpositions['b8'])
WIN.blit(BKNIGHT, boardpositions['g8'])
WIN.blit(BBISHOP, boardpositions['c8'])
WIN.blit(BBISHOP, boardpositions['f8'])
WIN.blit(BQUEEN, boardpositions['d8'])
WIN.blit(BKING, boardpositions['e8'])






#Current pieces on board
pieces = []


def square_occupied(sq):
    for l in pieces:
        if l.square == sq:
            return True
        else:
            return False

class piece:
    def __init__(self, square, color, img, worth, start):
        self.square = square
        self.x, self.y = boardpositions[square]
        self.moves = []
        self.startingpos = start
        self.color = color
        self.img = img
        self.worth = worth
        

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def draw_moves(self, win):
        for x in self.moves:
            pygame.draw.circle(win, (125,125,125), (boardpositions[x][0] + 50, boardpositions[x][1] - 50), 30)
        pygame.display.update()

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 < self.y + self.height:
            return True
        else:
            return False

    def capture(self, capturedpiece, player):
        pieces.remove(capturedpiece)
        player.points += capturedpiece.worth
        self.x, self.y = boardpositions[capturedpiece.square]
    
class pawn(piece):
    def __init__(self, square, color, img):
        super().__init__(square, color, img, 1)


    
    

def diagonal(sq, piece=None):
    
    if piece != 'pawn':
        sq1 = abcs[abcs.index(sq[0]) + 1]+str(int(sq[1])+1)
        sq2 = abcs[abcs.index(sq[0]) - 1]+str(int(sq[1])+1)
        return [sq1, sq2]
    tempsq = sq
    tr = []
    bl = []
    tl = []
    br = []
    
    # Check Top-Right Diagonal
    while tempsq[0] != 'h' and tempsq[1] != ' 8':
            tempsq = abcs[abcs.index(tempsq[0]) + 1]+str(int(tempsq[1])+1)
            if square_occupied(tempsq):
                break
            tr.append(tempsq)
            
    #Reset while loop
    tempsq = sq

    # Check Bottom-Left Diagonal
    while tempsq[0] != 'a' and tempsq[1] != '1':
        tempsq = abcs[abcs.index(tempsq[0]) - 1]+str(int(tempsq[1])-1)
        if square_occupied(tempsq):
                break
        bl.append(tempsq)


    tempsq = sq
    
    # Check Top-Left Diagonal
    while tempsq[0] != 'a' and tempsq[1] != '8':
        tempsq = abcs[abcs.index(tempsq[0]) - 1]+str(int(tempsq[1])+1)
        if square_occupied(tempsq):
                break
        tl.append(tempsq)

    tempsq = sq

    # Check Bottom-Right Diagonal
    while tempsq[0] != 'h' and tempsq[1] != '1':
        tempsq = abcs[abcs.index(tempsq[0]) + 1]+str(int(tempsq[1])-1)
        if square_occupied(tempsq):
                break
        br.append(tempsq)

    return tr + tl + br +bl



def check_pawn_moves(pawn):
    if pawn.color == 'b':
        if  not square_occupied(pawn.square[0]+ str(int(pawn.square[1])-1)):
            pawn.moves.add(pawn.square[0]+ str(int(pawn.square[1])-1))
            if pawn.square[1] == '7' and not square_occupied(pawn.square[0]+ str(int(pawn.square[1])-2)):
                pawn.moves.add(pawn.square[0]+ str(int(pawn.square[1])-2))
    elif pawn.color == 'w':
        if  not square_occupied(pawn.square[0]+ str(int(pawn.square[1])+1)):
            pawn.moves.add(pawn.square[0]+ str(int(pawn.square[1])+1))
            if pawn.square[1] == '7' and not square_occupied(pawn.square[0]+ str(int(pawn.square[1])+2)):
                pawn.moves.add(pawn.square[0]+ str(int(pawn.square[1])+2))
    



pygame.display.flip()
while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for i in pieces:
                        if i.click(pos):
                            i.draw_moves()
        pygame.display.update()
