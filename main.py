import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    updatable, drawable, asteroids = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    _ = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # Player actions
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        for ast in asteroids:
            if ast.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
