import pygame

from components.text_button import TextButton
from models.cards.card import Card

pygame.init()


# class CardUI:
#     button_font = pygame.font.Font(None, 48)
#     width = 200
#     height = 80
#
#     def __init__(self, card: Card):
#         self._width = TextButton.width
#         self._height = TextButton.height
#
#         self.surface = pygame.Surface((self._width, self._height), pygame.SRCALPHA)
#         self.center = center
#
#         pygame.draw.rect(
#             self.surface, (0, 0, 0), (0, 0, self._width, self._height), border_radius=20
#         )
#
#         self.text = TextButton.button_font.render(text, True, (255, 255, 255))
#
#         self.text_rect = self.text.get_rect(
#             center=(self._width // 2, self._height // 2)
#         )
#
#         self.rect = self.surface.get_rect(center=self.center)
#
#     def draw(self, screen):
#         self.surface.blit(self.text, self.text_rect)
#         screen.blit(self.surface, self.rect)
