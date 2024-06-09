import pygame

#set window para
width = 800
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



##### creating a sprite
# sprite is an object
class Player(pygame.sprite.Sprite):    #player sprite
    # now to initialize
    # this code runs whenever player object gets made
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50)) # what the sprite looks li
        self.image.fill(green)

        self.rect = self.image.get_rect()  # encloses the sprite, helps moving it etc
        self.rect.center = ((width/2, height/2))     #the center of rect will be where we have set position


    def update(self):
        self.rect.x +=5        # moves to right
        # make sure not get out of screen
        if self.rect.left > width:
            self.rect.right = 0

####

# make a sprite group to make work easy
all_sprites = pygame.sprite.Group()       # put all ur sprites in this group, and ref in update and draw
player = Player()    # player is an instance of the Player class, can create many such instances
player1 = Player()
all_sprites.add(player1)   #added instance of class player to the group



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