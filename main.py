import pygame
import sys

import settings

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Quiz de conhecimentos gerais')
        self.screen = pygame.display.set_mode((settings.width, settings.height))

        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(settings.fps)

Game.run()
