import pygame
import math
from pygame.locals import *
from bullet import Bullet
from maze import draw_maze, load_maze
from player import Player
from mapa import generate_walls
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RED, BLUE, WHITE

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Combat_atari")
clock = pygame.time.Clock()


def main():
    maze = load_maze()
    obstacles = generate_walls(40, 40)
    players = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player1_x, player1_y = 50, 210
    player2_x, player2_y = 650, 210

    player1 = Player(player1_x, player1_y, {'up': K_w, 'down': K_s, 'left': K_a, 'right': K_d})
    player2 = Player(
        player2_x, player2_y, {'up': K_UP, 'down': K_DOWN, 'left': K_LEFT, 'right': K_RIGHT})

    players.add(player1, player2)

    # Dentro do seu loop principal
    for player in players:
        player.bullets.draw(screen)

    running = True
    while running:
        screen.fill((0, 0, 0))
        blocks = draw_maze(screen, maze)  # Aqui você obtém os blocos do labirinto

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot()
                elif event.key == pygame.K_RETURN:
                    player2.shoot()

        # Atualize todas as balas individualmente
        for bullet in bullets:
            bullet.update(blocks, players)

        player1.update(players, blocks)
        player2.update(players, blocks)

        players.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()