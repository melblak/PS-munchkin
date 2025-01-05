from constants import PLAY_BUTTON, QUIT_BUTTON, MENU_BACKGROUND_IMAGE

import pygame

from screens.player_selection_screen import PlayerSelectionScreen


class Menu:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1920, 1080))
        self.screen.blit(MENU_BACKGROUND_IMAGE, (0, 0))

        self.play_button_rect = PLAY_BUTTON.get_rect(center=(320, 200))
        self.quit_button_rect = QUIT_BUTTON.get_rect(center=(320, 800))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        self.start_game()
                    elif self.quit_button_rect.collidepoint(event.pos):
                        pygame.quit()
                        return

            self.screen.blit(PLAY_BUTTON, self.play_button_rect)
            self.screen.blit(QUIT_BUTTON, self.quit_button_rect)

            pygame.display.flip()

    def start_game(self):
        player_selection_screen = PlayerSelectionScreen(self.screen)
        player_selection_screen.run()
