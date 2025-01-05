class Card:
    def __init__(self, name, description, usable_during_combat=False):
        self.name = name
        self.description = description
        self.usable_during_combat = usable_during_combat

    def play(self, player):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def __str__(self):
        return f"{self.name}: {self.description}"
