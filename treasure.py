from card import Card


class Treasure(Card):
    def __init__(
        self,
        name,
        description,
        strength,
        special_effect=None,
        value=None,
    ):
        """
        Treasure cards have a name, description, and a strength boost.
        Additional attributes like item_type and special_effect can be used
        to define the type of treasure (e.g., weapon, armor) and special abilities.
        """
        super().__init__(name, description)
        self.strength = strength  # The strength boost this treasure gives
        self.special_effect = special_effect  # Any special effect (optional)
        self.value = value

    def consume(self, player): ...

    def play(self, player):
        """
        When a treasure card is played, it can be equipped by the player.
        """
        self.consume(player)

    def __str__(self):
        return f"{super().__str__()} (Boosts strength by {self.strength})"
