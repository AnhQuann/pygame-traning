import pygame
from player.player import Player
from enemy.enemy_spawner import EnemySpawner
import game_object
from input.input_manager import InputManager

BG_COLOR = (125, 125, 0)

# 1. init pygame
pygame.init()

# 2. Set up screen
SIZE = (600, 800)
canvas = pygame.display.set_mode(SIZE)
input_manager = InputManager()
player = Player(200, 300, input_manager)
enemy_spawner = EnemySpawner()

game_object.add(player)
game_object.add(enemy_spawner)

loop = True
clock = pygame.time.Clock()

while loop:
    # loop events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

        input_manager.update(event)

    game_object.update()

    canvas.fill(BG_COLOR)
    game_object.render(canvas)
    
    pygame.display.flip()
    clock.tick(60)