import sys

import pygame

from constants import MENU_BACKGROUND_IMAGE
from models.player.player import Player
from screens.munchkin import Munchkin
from components.text_button import TextButton


class PlayerNameInputScreen:
    def __init__(self, screen, num_players):
        self.screen = screen
        self.font = pygame.font.Font(None, 48)
        self.input_font = pygame.font.Font(None, 36)
        self.num_players = num_players

        self.players_names = [""] * num_players

        self.confirm_button = TextButton(center=(960, 750), text="Confirm")

        self.input_boxes = []
        self.input_boxes_rects = []
        for i in range(num_players):
            input_box = pygame.Surface((400, 50))
            input_box.fill((255, 255, 255))
            self.input_boxes.append(input_box)
            self.input_boxes_rects.append(
                input_box.get_rect(center=(960, 300 + i * 100))
            )

        self.player_labels = []
        for i in range(num_players):
            label_text = self.font.render(f"Player {i + 1}:", True, (255, 255, 255))
            self.player_labels.append(label_text)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(self.input_boxes_rects):
                        if rect.collidepoint(event.pos):
                            self.focused_input_box = i
                            break
                    if self.confirm_button.rect.collidepoint(event.pos):
                        players = [Player(name=i) for i in self.players_names]
                        munchkin = Munchkin(screen=self.screen, players=players)
                        munchkin.run()

                if event.type == pygame.KEYDOWN:
                    if hasattr(self, "focused_input_box"):
                        if event.key == pygame.K_BACKSPACE:
                            self.players_names[self.focused_input_box] = (
                                self.players_names[self.focused_input_box][:-1]
                            )
                        elif event.key == pygame.K_RETURN:
                            self.focused_input_box = None
                        else:
                            self.players_names[self.focused_input_box] += event.unicode

                    if event.key == pygame.K_RETURN:

                        if all(name != "" for name in self.players_names):
                            print("Starting game with players:", self.players_names)
                            pygame.quit()
                            sys.exit()

            self.screen.blit(MENU_BACKGROUND_IMAGE, (0, 0))

            for i in range(self.num_players):
                label_x = 460
                label_y = 300 + i * 100 - 30
                self.screen.blit(self.player_labels[i], (label_x, label_y))

                self.screen.blit(self.input_boxes[i], self.input_boxes_rects[i])

                input_text = self.input_font.render(
                    self.players_names[i], True, (0, 0, 0)
                )
                self.screen.blit(
                    input_text,
                    (
                        self.input_boxes_rects[i].x + 10,
                        self.input_boxes_rects[i].y + 10,
                    ),
                )

            self.confirm_button.draw(self.screen)
            pygame.display.flip()
