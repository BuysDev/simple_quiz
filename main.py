import pygame
import random
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definindo o tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Quiz de Inglês - Can, Could, Be Able To')

# Definindo as fontes
font = pygame.font.Font(None, 50)

# Definindo as questões e respostas
questions = [
    ("She _____ sing very well when she was younger.", "could"),
    ("They _____ go to the concert last night.", "couldn't"),
    ("Will you ________ come the party?", "be able to"),
    ("I _____ play the piano.", "can"),
    ("He _____ swim across the river.", "could"),
]

# Função para exibir texto na tela
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Função principal do jogo
def game_loop():
    current_question_index = 0
    user_answer = ''
    game_over = False

    while True:
        screen.fill(WHITE)

        if game_over:
            draw_text('Você errou! Jogo terminado.', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text('Pressione qualquer tecla para reiniciar', font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)
        else:
            question_text = questions[current_question_index][0]
            draw_text(question_text, font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text(user_answer, font, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game_over:
                    game_loop()
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                elif event.key == pygame.K_RETURN:
                    correct_answer = questions[current_question_index][1]
                    if user_answer.lower() == correct_answer:
                        current_question_index += 1
                        user_answer = ''
                        if current_question_index == len(questions):
                            draw_text('Parabéns! Você completou o quiz!', font, GREEN, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            game_loop()
                    else:
                        game_over = True
                else:
                    user_answer += event.unicode

        pygame.display.update()

# Iniciar o jogo
game_loop()