import pygame
import random
import sys
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

# The loop will carry on until the user exits the game (e.g. clicks the close button).
play = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

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

upperleftX = 160
upperleftY = 150
loc1 = [upperleftX, upperleftY]
loc2 = [upperleftX+170, upperleftY]
loc3 = [upperleftX, upperleftY+60]
loc4 = [upperleftX+170, upperleftY+60]

instruction = [Blue, Blue1, Blue2, Green, Green1, Green2, Red, Red1, Red2, Yellow, Yellow1, Yellow2]
instruction1 = ["Blue", "Blue1", "Blue2", "Green", "Green1", "Green2", "Red", "Red1", "Red2", "Yellow", "Yellow1", "Yellow2"]
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
        if(score >5):
            maxTime = 2
        if(score > 10):
            maxTime = 1

        if event.type == pygame.QUIT: # If user clicked close
              play = False # Flag that we are done so we can exit the while loop
        if event.type == pygame.MOUSEBUTTONUP:
            #print("LOOK HERE:" + str(pygame.mouse.get_pos()))
            mousePos = list(pygame.mouse.get_pos())
            #print("LOOK HERE:" + str(mousePos))
            #print(colorMatch())
            coord = colorMatch()
            #print(coord[0])
            #print(coord[1])
            #print(str(coord))
            #print((mousePos[0]-coord[0]))
            #print((mousePos[1]-coord[1]))
            if(coord[2]==0): #red blue
                if((mousePos[0]-coord[0]) < 124 and (mousePos[0]-coord[0]) >0 and mousePos[1]-coord[1] < 50 and mousePos[1]-coord[1] >0):
                    print("correct")
                    score = score + 1
                else:
                    print("WRONG")
            elif(coord[2]==1):
                if((mousePos[0]-coord[0]) < 200 and (mousePos[0]-coord[0]) >0 and mousePos[1]-coord[1] < 50 and mousePos[1]-coord[1] >0):
                    print("correct")
                    score = score + 1
                else:
                    print("WRONG")
            
            #inst = int(random.randint(0,11))
            counter = maxTime
    
    # --- Game logic should go here
    def colorMatch():
        
        c = instruction1[inst]
        print("C0: " + c[0])
        if(c[0]== 'Y'):
            return [325, 221,1]
        elif(c[0]== 'G'):
            return [325, 162,1]
        elif(c[0]== 'B'):
            return [186,162,0]
        else:
            return [186, 221,0]

    def highScore():
        print("high score")

    
    
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
    
    
     #The you can draw different shapes and lines or add text to your background stage.
    
 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
        
     
    # --- Limit to 60 frames per second
    
    counter = counter -1
    if counter < 0:
            counter = maxTime   
            

    clock.tick(1)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()

