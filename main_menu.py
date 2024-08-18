import pygame
from main import screen

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Limpa a tela com a cor branca

        pygame.display.update()