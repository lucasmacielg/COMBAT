import pygame
from pygame.locals import *
from bullet import Bullet
from maze import draw_maze, load_maze
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RED, BLUE, WHITE


# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Combat_atari")
clock = pygame.time.Clock()

def main():
    maze = load_maze()
    players = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player1 = Player(BLUE, 50, 50, {'up': K_w, 'down': K_s, 'left': K_a, 'right': K_d})
    player2 = Player(RED, SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50, {'up': K_UP, 'down': K_DOWN, 'left': K_LEFT, 'right': K_RIGHT})

    players.add(player1, player2)

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_maze(screen, maze)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bullet = Bullet(WHITE, player1.rect.centerx, player1.rect.centery, player1.angle)
                    bullets.add(bullet)
                elif event.key == K_RETURN:
                    bullet = Bullet(WHITE, player2.rect.centerx, player2.rect.centery, player2.angle)
                    bullets.add(bullet)

        players.update()
        bullets.update()
        players.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()