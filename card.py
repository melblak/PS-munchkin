class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def play(self, player):
        """
        A generic play method that will be overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

    def __str__(self):
        return f"{self.name}: {self.description}"
