from models.cards.door.door import Door
from models.cards.treasure.treasure import Treasure


class Monster(Door):
    def __init__(
        self, name: str, description: str, level: int, treasures: list[Treasure]
    ):
        super().__init__(name, description, False)
        self.level = level
        self.treasures = treasures
        self.strength = level

    def fight(self, player):
        player_strength = player.level  # Player strength based on their level
        for item in player.items:  # Add items that modify player strength
            player_strength += item.strength

        if player_strength >= self.level:
            player.level_up()  # Player wins and levels up
            return True
        return False

    def play(self, player):

        return self.fight(player)

    def __str__(self):
        return f"{super().__str__()} (Level {self.level})"
