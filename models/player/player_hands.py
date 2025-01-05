from models.cards.card import Card


class PlayerHands:
    def __init__(self):
        self.slots = []

    def add(self, card: Card): ...
