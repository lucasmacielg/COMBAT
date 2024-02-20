import pygame
import math

BULLET_SPEED = 10

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, start_x, start_y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (start_x, start_y)
        self.angle =  angle
        self.direction_vector = pygame.math.Vector2(math.cos(math.radians(self.angle)),
                                                    -math.sin(math.radians(self.angle))) * BULLET_SPEED

    def update(self):
        self.rect.move_ip(self.direction_vector)

        # Se a bala sair da tela, destruí-la
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            self.kill()
