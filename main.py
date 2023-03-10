#Created by Mei Slifka
#1/27/22
import pygame
import random
import time
pygame.init()

#Defining Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (240,195,185)

XMAX = 700
YMAX = 500
#Open new window
size = (XMAX,YMAX)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Color Square Game")

#Contintue until the user exits the game (e.g. clicks the close button).
play = True
 
#how fast the screen updates
clock = pygame.time.Clock()

#loading images
blueImage = pygame.image.load("./iBlue.png")
redImage = pygame.image.load("./iRed.png")
greenImage = pygame.image.load("./iGreen.png")
yellowImage = pygame.image.load("./iYellow.png")
Blue = pygame.image.load("./Blue.png")
Blue1 = pygame.image.load("./Blue1.png")
Blue2 = pygame.image.load("./Blue2.png")
Green = pygame.image.load("./Green.png")
Green1 = pygame.image.load("./Green1.png")
Green2 = pygame.image.load("./Green2.png")
Red = pygame.image.load("./Red.png")
Red1 = pygame.image.load("./Red1.png")
Red2 = pygame.image.load("./Red2.png")
Yellow = pygame.image.load("./Yellow.png")
Yellow1 = pygame.image.load("./Yellow1.png")
Yellow2 = pygame.image.load("./Yellow2.png")
again = pygame.image.load("./again.png")
quit = pygame.image.load("./quit.png")

#Buttons to answer
upperleftX = 160
upperleftY = 150
loc1 = [upperleftX, upperleftY]
loc2 = [upperleftX+170, upperleftY]
loc3 = [upperleftX, upperleftY+60]
loc4 = [upperleftX+170, upperleftY+60]

instruction = [Blue, Blue1, Blue2, Green, Green1, Green2, Red, Red1, Red2, Yellow, Yellow1, Yellow2]
loc = [loc1, loc2, loc3, loc4]
 #font
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Arial', 30)

maxTime = 3
inst = int(random.randint(0,11))
counter = maxTime
score = 0
# -------- Main Program Loop -----------
while play:
    # --- Main event loop
    for event in pygame.event.get():
        #speed up 
        if(score >5):
            maxTime = 2
        if event.type == pygame.QUIT: # If user clicked close
              play = False # Flag that we are done so we can exit the while loop
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = list(pygame.mouse.get_pos())
            coord = colorMatch()
            if(coord[2]==0): #red blue
                if((mousePos[0]-coord[0]) < 124 and (mousePos[0]-coord[0]) >0 and mousePos[1]-coord[1] < 50 and mousePos[1]-coord[1] >0):
                    #print("correct")
                    score = score + 1
                    inst = int(random.randint(0,11))
                else: #Yellow Green
                    #print("WRONG")
                    play = endGame()  
            elif(coord[2]==1):
                if((mousePos[0]-coord[0]) < 200 and (mousePos[0]-coord[0]) >0 and mousePos[1]-coord[1] < 50 and mousePos[1]-coord[1] >0):
                    #print("correct")
                    score = score + 1
                    inst = int(random.randint(0,11))
                else:
                    #print("WRONG")
                    play = endGame()
                    
                    
                    
            counter = maxTime
    
    #Returns which color/word is up
    def colorMatch():
        if(inst <= 2): #blue
            print("blue")
            return [186,162,0]
        elif(inst <=5):  #green
            print("green")
            return [325, 162,1]
        elif(inst <= 8): #red
            print("red")
            return [186, 221,0]
        else:  #yellow
            print("yellow")
            return [325, 221,1]

    

    def endGame():
        cont = True
        while(cont):
            screen.fill(PINK)
            endText = my_font.render("Game over! Final score: "+ str(score), False, (0, 0, 0))                
            screen.blit(endText, [(XMAX/2)-160,40])
            screen.blit(again, loc1)
            screen.blit(quit, loc2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    mousePos = list(pygame.mouse.get_pos())
                    print(mousePos)
                    if((mousePos[0]-186) < 124 and mousePos[1]-162 < 50 and mousePos[1]-162 >0): 
                        #print("A")
                        return(True)
                    if((mousePos[0]-325) < 200 and mousePos[1]-162 < 50 and mousePos[1]-162>0):
                        #print("q")
                        return(False)
            clock.tick(1)
       

    # --- Drawing code should go here
    
    screen.fill(PINK)
    screen.blit(instruction[inst],  ((XMAX/2)-100, 60))
    screen.blit(blueImage, loc1)
    screen.blit(greenImage, loc2)
    screen.blit(redImage, loc3)
    screen.blit(yellowImage, loc4)
    cText = my_font.render(str(int(counter)), False, (0, 0, 0))
    screen.blit(cText, [0,0])

    scoreText = my_font.render("Score: "+str(score), False, (0, 0, 0))
    screen.blit(scoreText, [0,YMAX-40])
    pygame.display.flip()
        
     
    # --- Limit to 60 frames per second
    counter = counter -1
    if counter < 0:
        endGame()
        screen.fill(BLACK)
        pygame.display.flip()  
            

    clock.tick(1)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()

