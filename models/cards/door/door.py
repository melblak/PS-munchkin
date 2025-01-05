from models.cards.card import Card


class Door(Card):
    def __init__(self, name, description, usable_during_combat):
        super().__init__(name, description, usable_during_combat)
