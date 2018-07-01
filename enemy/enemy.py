import pygame
from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("images/enemy/bacteria1.png")

    def update(self):
        self.y += 3
        self.deactivate_if_needed()

    def deactivate_if_needed(self):
        if self.y > 800:
            self.deactivate()
    