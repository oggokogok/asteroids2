import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state

version = pygame.version.ver
width = constants.SCREEN_WIDTH
height = constants.SCREEN_HEIGHT

def main():
    #initializing pygame
    pygame.init()

    #creating display area
    screen = pygame.display.set_mode((width,height))

    #creating groups, blank atm
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    

    #Adding items to groups
    Player.containers = (updatable, drawable)
    Asteroid.container = (asteroids,updatable,drawable)
    AsteroidField.container = (updatable)

    #creating clock and variable
    clock = pygame.time.Clock()
    dt = 0
    
    #creating asteroid field object
    ast_field = AsteroidField()

    #instantiate a player
    player = Player(int(width / 2), int(height / 2))

    while True:
        #Calling LogState
        log_state()

        #allowing game to close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #updating updatable group
        updatable.update(dt)

        #Filling screen with black
        screen.fill("black")
        #player.update(dt)
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        #flip refreshes screen
        pygame.display.flip()
        

        #Doing Clock Ticks
        dt = clock.tick(60)/1000
        #print(dt)
    print(f'Starting Asteroids with pygame version: {version}')
    print(f'Screen width: {width}')
    print(f'Screen height: {height}')
    # print(version)


if __name__ == "__main__":
    main()
#Continue https://www.boot.dev/lessons/268bb0d0-3e63-4218-aacc-cba3247a1af5