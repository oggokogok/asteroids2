import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        if self.position[0] <= 0:
            self.position = [SCREEN_WIDTH,self.position[1]]
        elif self.position[0] >= SCREEN_WIDTH:
            self.position = [0,self.position[1]]
        elif self.position[1] <= 0:
            self.position = [self.position[0],SCREEN_HEIGHT]
        elif self.position[1] >= SCREEN_HEIGHT:
            self.position = [self.position[0],0]


    def shoot(self, score):
        if self.cooldown <= 0:
            shot = Shot(self.position[0],self.position[1])
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            if score < 10:
                self.cooldown = PLAYER_SHOOT_COOLDOWN
            if score >= 10 and score <= 50:
                self.cooldown = PLAYER_SHOOT_COOLDOWN/2
            if score > 50:
                self.cooldown = PLAYER_SHOOT_COOLDOWN/50

    def update(self, dt, score):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if keys[pygame.K_a]:            
            self.rotate((dt*-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_s]:            
            self.move((dt*-1))
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot(score)