from card import Card


class Monster(Card):
    def __init__(self, name, description, level, treasures=None):
        """
        Monster cards have a name, description, level (strength), and optional treasures.
        """
        super().__init__(name, description)
        self.level = level  # Monster strength
        self.treasures = treasures if treasures else []

    def fight(self, player):
        """
        Resolve combat between the player and this monster.
        """
        player_strength = player.level  # Player strength based on their level
        for item in player.items:  # Add items that modify player strength
            player_strength += item.strength

        if player_strength >= self.level:
            player.level_up()  # Player wins and levels up
            return True
        return False

    def play(self, player):
        """
        When a monster card is played, the player must fight it.
        """
        print(f"A wild monster appears: {self.name}!")
        return self.fight(player)

    def __str__(self):
        return f"{super().__str__()} (Level {self.level})"
