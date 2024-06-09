import pygame
import os

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

# set up folders of assets
game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "images")


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
        # load image
        self.image = pygame.image.load(os.path.join(image_folder, "p1_jump.png")).convert()
        # theres black rectangle around image we want to remove
        self.image.set_colorkey(black)


        self.rect = self.image.get_rect()  # encloses the sprite, helps moving it etc
        self.rect.center = ((width/2, height/2))     #the center of rect will be where we have set position
        self.y_speed=5

    def update(self):
        self.rect.x +=5        # moves to right
        self.rect.y += self.y_speed     #moves up
        # make sure not get out of screen
        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.bottom > height-200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
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
    screen.fill(green)

    all_sprites.draw(screen)   # draws all the sprites at the surface of screen


    # after everything drawn, do this;
    pygame.display.flip()

pygame.quit()