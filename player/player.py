import pygame
from player.player_bullet import PlayerBullet
import game_object

class Player:
    def __init__(self, x, y, input_manager):
        self.x = x
        self.y = y
        self.input_manager = input_manager
        self.image = pygame.image.load("images/player/player1.png")
        self.shoot_lock = False
        self.count = 0

    def update(self):
        self.move()
        self.shoot()

    def move(self):
        dx = 0
        dy = 0
        step = 5

        if self.input_manager.up_pressed:
            dy -= step
        if self.input_manager.down_pressed:
            dy += step
        if self.input_manager.left_pressed:
            dx -= step
        if self.input_manager.right_pressed:
            dx += step

        self.x += dx
        self.y += dy

    def shoot(self):
        if self.input_manager.x_pressed and not self.shoot_lock:
            bullet = PlayerBullet(self.x, self.y)
            game_object.add(bullet)
            self.shoot_lock = True

        if self.shoot_lock:
            self.count += 1
            if self.count == 20:
                self.count = 0
                self.shoot_lock = False