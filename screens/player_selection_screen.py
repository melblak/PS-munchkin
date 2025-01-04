import sys

import pygame

from constants import BACKGROUND_IMAGE, ARROW_UP, ARROW_DOWN
from screens.player_name_input_screen import PlayerNameInputScreen
from text_button import TextButton


class PlayerSelectionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.button_font = pygame.font.Font(None, 48)

        self.screen.blit(BACKGROUND_IMAGE, (0, 0))

        self.num_players = 3
        self.min_players = 3
        self.max_players = 6

        self.title_text = self.font.render(
            "Select number of players", True, (255, 255, 255)
        )
        self.title_rect = self.title_text.get_rect(center=(960, 200))

        self.arrow_up_rect = ARROW_UP.get_rect(center=(960, 400))
        self.arrow_down_rect = ARROW_DOWN.get_rect(center=(960, 600))

        self.confirm_button = TextButton(center=(960, 750), text="Confirm")

        self.num_players_text = self.font.render(
            str(self.num_players), True, (255, 255, 255)
        )
        self.num_players_rect = self.num_players_text.get_rect(center=(960, 500))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.arrow_up_rect.collidepoint(event.pos):
                        if self.num_players < self.max_players:
                            self.num_players += 1
                    elif self.arrow_down_rect.collidepoint(event.pos):
                        if self.num_players > self.min_players:
                            self.num_players -= 1
                    elif self.confirm_button.rect.collidepoint(event.pos):
                        name_input_screen = PlayerNameInputScreen(
                            self.screen, self.num_players
                        )
                        name_input_screen.run()

            self.screen.blit(BACKGROUND_IMAGE, (0, 0))

            self.screen.blit(self.title_text, self.title_rect)

            self.screen.blit(ARROW_UP, self.arrow_up_rect)
            self.screen.blit(ARROW_DOWN, self.arrow_down_rect)

            self.confirm_button.draw(self.screen)

            self.num_players_text = self.font.render(
                str(self.num_players), True, (255, 255, 255)
            )
            self.num_players_rect = self.num_players_text.get_rect(center=(960, 500))
            self.screen.blit(self.num_players_text, self.num_players_rect)

            pygame.display.flip()
