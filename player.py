import pygame
from pygame.locals import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from mapa import generate_walls


PLAYER_SPEED = 5
obstacles=generate_walls(40,40)
BLOCK_SIZE = 10

class Player(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, controls):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.angle = 0
        self.controls = controls
        self.obstacles = generate_walls(40, 40)
        self.wall_rects = [pygame.Rect(wall[0], wall[1], BLOCK_SIZE, BLOCK_SIZE) for wall in self.obstacles]

    def update(self, obstacles, players):
        keys = pygame.key.get_pressed()
        new_rect = self.rect.copy()
        if keys[self.controls['up']]:
            self.rect.y -= PLAYER_SPEED
        if keys[self.controls['down']]:
            self.rect.y += PLAYER_SPEED
        if keys[self.controls['left']]:
            self.rect.x -= PLAYER_SPEED
        if keys[self.controls['right']]:
            self.rect.x += PLAYER_SPEED

        wall_rects = [pygame.Rect(wall[0], wall[1], BLOCK_SIZE, BLOCK_SIZE) for wall in obstacles]

            # Verifica a colisão com as paredes
        for wall_rect in self.wall_rects:
            if new_rect.colliderect(wall_rect):
                return  # Se houver colisão com uma parede, retorna sem atualizar a posição

            # Verifica a colisão com outros jogadores
        for player in players:
            if player != self and new_rect.colliderect(player.rect):
                return  # Se houver colisão com outro jogador, retorna sem atualizar a posição

            # Se não houver colisões, atualiza a posição do jogador
        self.rect = new_rect

        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.rect.clamp_ip(screen_rect)