from main_menu import main_menu
import pygame
from main import screen

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