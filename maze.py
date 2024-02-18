import pygame
from constants import SCREEN_HEIGHT
from mapa import WHITE


def load_maze():
    maze = []
    with open('labirinto.txt', 'r') as file:
        for line in file:
            row = line.strip().split(",")
            maze.append(row)
    return maze

# Função para desenhar o labirinto na tela
def draw_maze(screen, maze):
    block_size = 10
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '1':
                pygame.draw.rect(screen, WHITE, (x * block_size, y * block_size, block_size, block_size))