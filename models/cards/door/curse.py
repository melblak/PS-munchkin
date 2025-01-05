from models.cards.door.door import Door


class Curse(Door):
    def __init__(self, name, description, effect):
        super().__init__(name, description, True)
        self.effect = effect

    def curse(self, player): ...

    def play(self, player):
        return self.curse(player)
