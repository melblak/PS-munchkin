import pygame


class Menu:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the screen

        self.screen = pygame.display.set_mode((1920, 1080))
        background = pygame.image.load("assets/assets_menu/menu.png")
        self.screen.blit(background, (0, 0))

        # Load assets
        self.play_button = pygame.image.load("assets/assets_menu/botao_jogar_local.png")
        self.quit_button = pygame.image.load("assets/assets_menu/botao_sair.png")

        # Set button positions
        self.play_button_rect = self.play_button.get_rect(center=(320, 200))
        self.quit_button_rect = self.quit_button.get_rect(center=(320, 800))

    def run(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        # Start the game
                        pass
                    elif self.quit_button_rect.collidepoint(event.pos):
                        # Quit the game
                        pygame.quit()
                        return

            # Draw buttons
            self.screen.blit(self.play_button, self.play_button_rect)
            self.screen.blit(self.quit_button, self.quit_button_rect)

            # Update the display
            pygame.display.flip()
