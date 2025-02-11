import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (tuple(self.position)), self.radius, 2)

    def update(self, delta):
        self.position += (self.velocity * delta)

    pass