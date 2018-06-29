import pygame

class PlayerBullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/player-bullet.png")

    def update(self):
        self.y -= 10