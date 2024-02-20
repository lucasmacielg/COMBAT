import pygame
from pygame.locals import *
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from mapa import generate_walls
from bullet import Bullet

PLAYER_SPEED = 5
obstacles = generate_walls(40, 40)
BLOCK_SIZE = 10 

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y, controls):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.controls = controls
        self.wall_rects = [] 
        self.health = 30  
        

    def hit(self):
        self.health -= 10  
        if self.health <= 0:
            self.kill()  
        

    def shoot(self, bullets):
        bullet = Bullet((255, 0, 0), self.rect.centerx, self.rect.centery, self.angle)
        bullets.add(bullet)
        
    def update(self, players, blocks):
        keys = pygame.key.get_pressed()
        new_rect = self.rect.copy()
        if keys[self.controls['up']]:
            new_rect.y -= PLAYER_SPEED
        if keys[self.controls['down']]:
            new_rect.y += PLAYER_SPEED
        if keys[self.controls['left']]:
            new_rect.x -= PLAYER_SPEED
        if keys[self.controls['right']]:
            new_rect.x += PLAYER_SPEED

        # Verifica a colisão com os blocos do labirinto
        for block in blocks:
            if new_rect.colliderect(block):
                return  # Se houver colisão com um bloco, retorna sem atualizar a posição

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