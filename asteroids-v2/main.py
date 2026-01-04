import pygame
import constants
from logger import log_state

version = pygame.version.ver
width = constants.SCREEN_WIDTH
height = constants.SCREEN_HEIGHT

def main():
    #initializing pygame
    pygame.init()

    #creating display area
    screen = pygame.display.set_mode((width,height))

    while True:
        #Calling LogState
        log_state()

        #allowing game to close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Filling screen with black
        screen.fill("black")

        #flip refreshes screen
        pygame.display.flip()
    print(f'Starting Asteroids with pygame version: {version}')
    print(f'Screen width: {width}')
    print(f'Screen height: {height}')
    # print(version)


if __name__ == "__main__":
    main()
#Continue https://www.boot.dev/lessons/268bb0d0-3e63-4218-aacc-cba3247a1af5