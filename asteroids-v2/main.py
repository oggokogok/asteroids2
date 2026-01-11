import pygame
import constants
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state
from logger import log_event

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
    shots = pygame.sprite.Group()

    #Adding items to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable,updatable,shots)

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

        #Checking for asteroid collision
        for obj in asteroids:
            for bullet in shots:
                if obj.collides_with(bullet) == True:
                    obj.split()
                    bullet.kill()
                    log_event("asteroid_shot")
            if obj.collides_with(player) == True:
                log_event("player_hit")
                print('Game over!')
                sys.exit()
            

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