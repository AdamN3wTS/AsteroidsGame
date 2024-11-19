import pygame
from asteroidfield import *
from constants import *
from player import Player
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    FPS = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    AsteroidField1 = AsteroidField()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x,y)
    dt =0 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = FPS.tick(60) / 1000
    
    

if __name__ == "__main__":
    main()
