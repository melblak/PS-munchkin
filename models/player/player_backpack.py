from models.cards.treasure.treasure import Treasure


class PlayerBackpack:
    def __init__(self):
        self.slots = []

    def add(self, treasure: Treasure): ...
