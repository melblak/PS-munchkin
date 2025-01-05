import pygame

PLAY_BUTTON = pygame.image.load("assets/assets_menu/botao_jogar_local.png")
QUIT_BUTTON = pygame.image.load("assets/assets_menu/botao_sair.png")
MENU_BACKGROUND_IMAGE = pygame.image.load("assets/assets_menu/menu.png")
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("assets/background_table.jpg"), (1920, 1080)
)

ARROW_UP = pygame.transform.scale(
    pygame.image.load("assets/assets_menu/arrow_up.png"), (100, 100)
)
ARROW_DOWN = pygame.transform.scale(
    pygame.image.load("assets/assets_menu/arrow_down.png"), (100, 100)
)
