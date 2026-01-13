import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, circle):
        print(self.position)
        # print(circle.position)
        #using built in distance to logic, using self and player that's passed
        distance = pygame.Vector2.distance_to(self.position,circle.position)
        #if the distance is less than or equal to the 2 radii summed then they're hitting
        if distance <= self.radius+circle.radius:
            return True
        else:
            return False
        #Logic from boot: return self.position.distance_to(other.position) <= self.radius + other.radius