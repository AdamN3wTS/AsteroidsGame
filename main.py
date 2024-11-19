import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    
    FPS = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x,y)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    dt =0 
    my_group = pygame.sprite.Group()
    Player.containers = (my_group)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player1.draw(screen)
        player1.update(dt)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = FPS.tick(60) / 1000
    
    

if __name__ == "__main__":
    main()
