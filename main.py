import pygame
import sys
import buttons
import settings
import quiz_buttons

pygame.init()

screen = pygame.display.set_mode((settings.width, settings.height))

try_again_img = pygame.image.load('try_again.png').convert_alpha()
try_again = buttons.Button(800, 500, try_again_img, 1)

def you_lose():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Verifica se o mouse foi clicado
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o botão foi clicado
                if try_again.clicked(pygame.mouse.get_pos()):
                    main_menu()  # Retorna ao menu principal ou reinicia o jogo

        screen.fill((255, 255, 255))  # Limpa a tela com a cor branca
        try_again.draw(screen)
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
