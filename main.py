import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption('Basic Pygame Window')

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.display.flip()

pygame.quit()
sys.exit()
