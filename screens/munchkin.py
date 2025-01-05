import sys

import pygame

from constants import BACKGROUND_IMAGE
from models.player.player import Player


class Munchkin:
    def __init__(self, screen, players: list[Player]):
        self.players = players

        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.input_font = pygame.font.Font(None, 36)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    ...

            self.screen.blit(BACKGROUND_IMAGE, (0, 0))

            pygame.display.flip()
