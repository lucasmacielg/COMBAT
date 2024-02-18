import pygame

BULLET_SPEED = 10

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, direction):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.direction = direction

    def update(self):
        if self.direction == 'up':
            self.rect.y -= BULLET_SPEED
        elif self.direction == 'down':
            self.rect.y += BULLET_SPEED
        elif self.direction == 'left':
            self.rect.x -= BULLET_SPEED
        elif self.direction == 'right':
            self.rect.x += BULLET_SPEED