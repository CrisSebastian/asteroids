import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (tuple(self.position)), self.radius, 2)

    def update(self, delta):
        self.position += (self.velocity * delta)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
            
            
        
    