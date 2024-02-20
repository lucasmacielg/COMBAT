from typing import List, Tuple

import pygame
import sys

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 10
WHITE = (255, 255, 255)

def generate_walls(x, y):
    obstacles = []
    with open('labirinto.txt', 'r') as file:
        walls = file.readlines()
        posy_block = 200
        for line in range(x):
            wall_row = walls[line].strip().split(",")
            posx_block = -353
            for column in range(y):
                if wall_row[column] == '1':
                    obstacles.append((posx_block, posy_block))
                    posx_block += BLOCK_SIZE
            posy_block -= BLOCK_SIZE
        return obstacles

def draw_obstacles(screen, obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, (obstacle[0], obstacle[1], BLOCK_SIZE, BLOCK_SIZE))

