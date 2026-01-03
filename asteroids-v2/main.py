import pygame
import constants

version = pygame.version.ver
width = constants.SCREEN_WIDTH
height = constants.SCREEN_HEIGHT
def main():
    print(f'Starting Asteroids with pygame version: {version}')
    print(f'Screen width: {width}')
    print(f'Screen height: {height}')
    # print(version)


if __name__ == "__main__":
    main()
#Continue https://www.boot.dev/lessons/268bb0d0-3e63-4218-aacc-cba3247a1af5