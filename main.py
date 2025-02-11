import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta = 0

    

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Groups will be declared here
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group,)
    Asteroid.containers = (updatable_group, drawable_group, asteroid_group,)
    AsteroidField.containers = (updatable_group,)
    Shot.containers = (updatable_group, drawable_group, shots_group,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0,0,0))

        updatable_group.update(delta)

        for member in drawable_group:
            member.draw(screen)

        pygame.display.flip()

        for member in asteroid_group:
            if player.check_collision(member):
                print("Game over!")
                raise SystemExit()

        delta = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    

