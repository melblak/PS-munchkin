from itertools import count

from models.cards.treasure.treasure import Treasure
from models.player.player_backpack import PlayerBackpack
from models.cards.treasure.equipment import Equipment
from models.player.player_hands import PlayerHands
from models.player.player_equipment import PlayerEquipment

id_counter = count(1)


class Player:
    def __init__(self, name):
        self.id = next(id_counter)
        self.name = name
        self.level = 1
        self.races = []
        self.classes = []
        self.curses = []
        self.equipment = PlayerEquipment()
        self.backpack = PlayerBackpack()
        self.in_hands = PlayerHands()

    def equip(self, equipment: Equipment): ...

    def calculate_strength(self) -> int: ...

    def run(self): ...

    def fight(self): ...

    def sell_item(self, treasure: Treasure): ...

    def kick_door(self): ...

    def look_for_trouble(self): ...

    def loot_the_room(self): ...

    def jump_in(self): ...  # se intrometer no combate de outro jogador
