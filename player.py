import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    def shoot(self):
        if self.timer<=0:
            shot = Shot(self.position.x,self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity += forward * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN
        
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
        self.rotation += PLAYER_TURN_SPEED * dt
    def update(self,dt):
        self.timer -=dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_a]:
                self.rotate(-dt)
            elif keys[pygame.K_LEFT]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            elif keys[pygame.K_RIGHT]:
                self.rotate(dt)
        # move
            if keys[pygame.K_w]:
                self.move(dt+0.02)
            elif keys[pygame.K_UP]:
                self.move(dt+0.02)
            elif keys[pygame.K_s]:
                self.move(-dt+0.02)
            elif keys[pygame.K_DOWN]:
                self.move(-dt+0.02)
        else:
            if keys[pygame.K_a]:
                self.rotate(-dt)
            elif keys[pygame.K_LEFT]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            elif keys[pygame.K_RIGHT]:
                self.rotate(dt)
        # move
            if keys[pygame.K_w]:
                self.move(dt)
            elif keys[pygame.K_UP]:
                self.move(dt)
            elif keys[pygame.K_s]:
                self.move(-dt)
            elif keys[pygame.K_DOWN]:
                self.move(-dt)
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def boost(self):
        PLAYER_SPEED = 350
        