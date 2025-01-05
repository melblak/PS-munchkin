from models.cards.treasure.treasure import Treasure


class Consumable(Treasure):
    def __init__(
        self,
        name,
        description,
        strength=None,
        effect=None,
        value=None,
    ):
        super().__init__(name, description, True)
        self.strength = strength
        self.effect = effect
        self.value = value

    def consume(self, player): ...

    def play(self, player):
        self.consume(player)
