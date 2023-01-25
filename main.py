import pygame
import random
pygame.init()

#Defining Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (50,0,0)

#Open new window
size = (700,500)
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
loc1 = [(700/2)-100, 0]

instruction = [blueImage, redImage, greenImage,yellowImage]
#loc = [loc1, loc2, loc3, loc4]
 #font
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Arial', 30)

# -------- Main Program Loop -----------
while play:
    # --- Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # If user clicked close
              play = False # Flag that we are done so we can exit the while loop
        
    
    
    
    # --- Game logic should go here

 
    # --- Drawing code should go here
    # First, clear the screen to white. 
    screen.fill(WHITE)
    screen.blit(instruction[random.randint(0, 3)], (loc1))
    
    
    #text_surface = my_font.render('Click on matching color', False, (0, 0, 0))
    



     #The you can draw different shapes and lines or add text to your background stage.
    
 
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(1)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()