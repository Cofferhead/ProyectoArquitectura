
from turtle import speed
import pygame
import sys 
import random
import ctypes
#Recordatorio los Rec se hacen desde la esquina superior izquierda
BLOCKSIZE = 40
pygame.init()
screenHeigh = 800
screeenWidth = 800
asm = ctypes.CDLL('C:/Users/felix/Downloads/ProyectoC/Debug/ProyectoC.dll')
entero = asm.rnd()
print(str(entero))
#Screen
screenHeigh = 600
screenWidth = 800
screenLimit = 400
screen = pygame.display.set_mode((screenWidth, screenHeigh))
clock = pygame.time.Clock()
#Images
centepideHeigh = 30
centepideWidth = 30       
headImage = pygame.image.load('C:/Users/felix/source/repos/ProyectoPrueba4/ProyectoPrueba4/Images/head.png').convert()
bodyImage = pygame.image.load('C:/Users/felix/source/repos/ProyectoPrueba4/ProyectoPrueba4/Images/body.png').convert()
bodyImage = pygame.transform.scale(bodyImage, (centepideWidth, centepideHeigh))
bodyImage.set_colorkey((0,0,0))
headImage = pygame.transform.scale(headImage, (centepideWidth, centepideHeigh))
headImage.set_colorkey((0,0,0))
#Obstacle images
obstacleSize = 30
obstacleImage = pygame.image.load('C:/Users/felix/source/repos/ProyectoPrueba4/ProyectoPrueba4/Images/obstacle.jpg').convert()
obstacleImage = pygame.transform.scale(obstacleImage, (obstacleSize, obstacleSize))
obstacleImage.set_colorkey((0,0,0))
class ship:
    def __init__ (self):
        self.x = screeenWidth/2
        self.y = screenHeigh/2
        self.speed = 20
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        self.x = random.randint(0, screeenWidth)
        self.x -= self.x%BLOCKSIZE
        #Nos aseguramos que no aparezca en las orillas de pantalla
        while self.x == 0 or self.x == screeenWidth-BLOCKSIZE:
            self.x = random.randint(0, screeenWidth)
            self.x -= self.x%BLOCKSIZE
        #O en el centepide
        self.y = random.randint(0, screenLimit)
        self.y -= self.y%BLOCKSIZE
        while self.y == BLOCKSIZE:
            self.y = random.randint(0, screenLimit)
            self.y -= self.y%BLOCKSIZE
        self.life = 2
        self.body = pygame.Rect(self.x, self.y, obstacleSize, obstacleSize)
        self.dead = False

    def update(self):
        if self.life <= 0:
            self.kill
#Centepide
class Centepide(pygame.sprite.Sprite):
    def __init__(self):
        self.x = BLOCKSIZE
        self.y = BLOCKSIZE
        self.pieces = 4
        self.speed = 10
        self.body = []
        self.dead = False
    def definePieces(self):
        for i in range(self.pieces):
            aux = Piece()
            aux.x += centepideWidth*i
            self.body.append(aux)
    def update(self):
        
        if len(self.body) == 0:
            self.dead = True
            
        for piece in self.body:
            piece.update()
        '''
        self.body.append(self.head)
        #Recorremos todo el cuerpo avanzando a donde estaba la siguiente pieza
        for i in range(len(self.body)-1):
            #self.body[i].x, self.body[i].y = self.body[i+1].x+(self.xDir*centepideWidth*(self.speed-1)), self.body[i+1].y
            #screen.blit(headImage, (self.body[i].x, self.body[i].y))
            if self.body[i].x+(self.speed * self.xDir[i]) in range(self.boundLeft, self.boundRight):
                self.body[i].x += self.speed * self.xDir[i]
            else:
                self.body[i].y += self.speed
                if self.body[i].y >= self.nextHeight:
                    self.xDir[i] = self.xDir[i]*-1
                    if i == 0:
                        self.nextHeight += BLOCKSIZE
                        self.boundLeft = 0
                        self.boundRight = screenWidth-25
                        #print("siguiente Altura:" + str(self.nextHeight) )
        self.head = self.body[len(self.body) - 1]        
        #Eliminamos la cabeza del cuerpo
        self.body.remove(self.head)
        '''
        if self.dead:
            self.kill
#Draw grid QUITAR DESPUES
def drawGrid():
    for x in range(0, screeenWidth, BLOCKSIZE):
        for y in range(0, screenHeigh, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)      
class Piece:
    def __init__(self):
        self.x = BLOCKSIZE
        self.y = BLOCKSIZE
        self.xDir = 1
        self.yDir = 0
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, centepideWidth, centepideHeigh)
        self.nextHeight = [self.y+BLOCKSIZE]
        self.dead = False
        self.boundLeft = 0
        self.boundRight = screeenWidth-25
        self.actualHeight = 0
    def update (self):
        
        if self.x+(self.speed * self.xDir) in range(self.boundLeft, self.boundRight):
                self.x += self.speed * self.xDir
        else:
            self.y += self.speed
            if self.y >= self.nextHeight[self.actualHeight]:
               self.xDir = self.xDir*-1
               self.nextHeight.append(self.nextHeight[self.actualHeight]+BLOCKSIZE)
                   #self.nextHeight += BLOCKSIZE
               self.boundLeft = 0 
               self.boundRight = screenWidth-25
               self.actualHeight += 1
               #print("siguiente Altura:" + str(self.nextHeight[]) )
        
#Main loop
numObs = 20            
centepide = Centepide()
centepide.definePieces()
obstacles = []
i = 0
for i in range(numObs):
    obstacles.append(Obstacle())
i = 1  
for obsAct in obstacles:
    for obsSec in obstacles:
        if obsSec.y-BLOCKSIZE == obsAct.y or obsSec.y+BLOCKSIZE == obsAct.y:
            while obsAct.x == obsSec.x+BLOCKSIZE or obsAct.x == obsSec.x-BLOCKSIZE:
                obsAct.x = random.randint(0, screeenWidth)
                obsAct.x -= obsAct.x%BLOCKSIZE
'''     
aux = Obstacle()
aux.x = BLOCKSIZE*5
aux.y = BLOCKSIZE*2
obstacles.append(aux)
aux = Obstacle()
aux.x = BLOCKSIZE*7
aux.y = BLOCKSIZE*3
obstacles.append(aux)
aux = Obstacle()
aux.x = BLOCKSIZE*4
aux.y = BLOCKSIZE*4
obstacles.append(aux)
'''
'''Prueba piezas
piezas = []
contAux = 0
for i in range(4):
    aux = Piece()
    aux.x += centepideWidth*contAux
    piezas.append(aux)
    contAux += 1
    '''
while True:
    #Background
    screen.fill('black')
    drawGrid()
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                 for piece in centepide.body:
                     piece.speed = 0

    
    #screen.blit(headImage, (centepide.head.x, centepide.head.y))    
    
    for piece in centepide.body:
        #Revisamos colisiones
        xHead = piece.x
        yHead = piece.y
        #print("XHEAD: " + str(xHead) + ", YHEAD: " + str(yHead))
        for obstacle in obstacles:
            xBoundObt = obstacle.x
            yBoundObt = obstacle.y
            #Si va hacia la Izquierda
            if xHead > xBoundObt:
                if xHead <= (xBoundObt+obstacleSize) and yHead == yBoundObt:
                    #print("Condicional: " + str(xHead == (xBoundObt+obstacleSize) and yHead == yBoundObt))
                    #print("XHEAD: " + str(xHead) + ", YHEAD: " + str(yHead))
                    #print("X: " + str(xBoundObt) + ", Y: " + str(yBoundObt))
                    #centepide.speed = 0
                    piece.boundLeft = xBoundObt+obstacleSize
            #Si va a la derecha
            elif xHead+centepide.speed+centepideWidth >= xBoundObt and yHead == yBoundObt:
                #print("X: " + str(obstacle.x ) + ", Y: " + str(yBoundObt))
                #print("XHEAD: " + str(xHead+centepideWidth+centepide.speed) + ", YHEAD: " + str(yHead))
                #centepide.speed = 0
                piece.boundRight = xBoundObt-centepideWidth+10
        
    #Impresiones             
    i = 0
    for piece in centepide.body:
        #print(str(i) + "| X:  " + str(piece.x) + ", Y: " + str(piece.y))
        if i != len(centepide.body)-1:
            screen.blit(bodyImage, (piece.x, piece.y))
        else:
            screen.blit(headImage, (piece.x, piece.y))
        i += 1
    centepide.update()
    #print("Size: " + str(len(obstacles)))
    for obstaculo in obstacles:
        screen.blit(obstacleImage, (obstaculo.x, obstaculo.y))
        #print(str((obstaculo.x, obstaculo.y)))
           
    


    pygame.display.update()
    clock.tick(20)


