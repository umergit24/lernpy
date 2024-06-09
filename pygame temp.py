import pygame

#set window para
width = 560
height = 600
fps = 30

#colors
white = (255 , 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#initialize pygame screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("umers game")
clock = pygame.time.Clock()

#loop (runs 30 times a second?)
running = True


# make a sprite group to make work easy
all_sprites = pygame.sprite.Group()       # put all ur sprites in this group, and ref in update and draw


while running:
    #keep loop speed correct to fps
    clock.tick(fps)
    #1. something happening/ event
    # process events that have happened before
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #2. update game
    all_sprites.update()



    #3. draw the update
    screen.fill(black)

    all_sprites.draw(screen)   # draws all the sprites at the surface of screen


    # after everything drawn, do this;
    pygame.display.flip()

pygame.quit()