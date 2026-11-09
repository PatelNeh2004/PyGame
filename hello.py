import pygame ## Loads the Library

pygame.init() ## start the system

## This make screen with 720p qulity and 
## firs parameter is width and second is
## hieght
screen = pygame.display.set_mode((1280,720))

##This for the title of the window that will pop up
pygame.display.set_caption("Testing Pygame with Github and Nvim")

##while loop for game running until we press quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
##Quit the system
pygame.quit()

