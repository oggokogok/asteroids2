import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.width = LINE_WIDTH

    def draw(self,screen):
        #self.position was needed as the x and y don't exist by themselves, position is created in circleshape
        pygame.draw.circle(screen,"white",self.position,self.radius,self.width)
    
    def update(self,dt):
        pos_test = self.position
        self.position += (self.velocity * dt)
        if self.position[0]+self.radius <= 0-(self.radius+1):
            self.position = [SCREEN_WIDTH,self.position[1]+self.radius]
        # elif self.position[0] >= SCREEN_WIDTH+(self.radius+1):
        #     self.position = [0,self.position[1]]
        # elif self.position[1] <= 0-(self.radius+1):
        #     self.position = [self.position[0],SCREEN_HEIGHT]
        # elif self.position[1] >= SCREEN_HEIGHT+(self.radius+1):
        #     self.position = [self.position[0],0]


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            split1 = pygame.Vector2(self.velocity).rotate(angle)
            split2 = pygame.Vector2(self.velocity).rotate(-angle)
            new_radii = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0],self.position[1],new_radii)
            ast1.velocity = split1*1.2
            ast2 = Asteroid(self.position[0],self.position[1],new_radii)
            ast2.velocity = split2*1.2
