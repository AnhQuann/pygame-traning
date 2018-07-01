import pygame
from game_object import GameObject

class PlayerBullet(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/player-bullet.png")

    def update(self):
        self.y -= 10
        self.deactivate_if_needed()

    def deactivate_if_needed(self):
        if self.y < 0:
            self.deactivate()