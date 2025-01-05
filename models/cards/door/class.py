from models.cards.door.door import Door


class Class(Door):
    def __init__(self, name, description, skills, abilities):
        super().__init__(name, description, False)
        self.skills = skills
        self.abilities = abilities

    def apply(self): ...

    def make(self, player): ...

    def play(self, player):
        return self.make(player)
