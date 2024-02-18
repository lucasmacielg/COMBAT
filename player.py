import pygame
from pygame.locals import *

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, controls):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.angle = 0
        self.controls = controls  

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls['up']]:
            self.rect.y -= PLAYER_SPEED
        if keys[self.controls['down']]:
            self.rect.y += PLAYER_SPEED
        if keys[self.controls['left']]:
            self.rect.x -= PLAYER_SPEED
        if keys[self.controls['right']]:
            self.rect.x += PLAYER_SPEED
        screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.rect.clamp_ip(screen_rect)