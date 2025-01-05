from models.cards.door.door import Door


class Race(Door):
    def __init__(self, name, description, skills, abilities):
        super().__init__(name, description, False)
        self.skills = skills
        self.abilities = abilities

    def make(self, player): ...

    def play(self, player):
        return self.make(player)
