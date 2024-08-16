import pygame
import sys
import buttons
import settings
import quiz_buttons

pygame.init()

screen = pygame.display.set_mode((settings.width, settings.height))

restart_img = pygame.image.load('restart.png').convert_alpha()

restart = buttons.Button(800, 500, restart_img, 1)

def you_lose():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Verifica se o mouse foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o botão foi clicado
                if restart.is_clicked(pygame.mouse.get_pos()):
                    main_menu()  # Retorna ao menu principal ou reinicia o jogo

        screen.fill((255, 255, 255))  # Limpa a tela com a cor branca
        restart.draw(screen)
        pygame.display.update()

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Limpa a tela com a cor branca

        pygame.display.update()

you_lose()
