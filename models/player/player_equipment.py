from models.cards.treasure.equipment import Equipment
from models.player.body_part import BodyPart


class PlayerEquipment:
    def __init__(self):
        self.head = None
        self.chest = None
        self.feet = None
        self.hands = []
        self.other = []

    @property
    def busy_hands(self):
        busy_hands = 0
        for equipment in self.hands:
            if equipment.is_two_hands:
                busy_hands += 2
            elif not equipment.is_two_hands:
                busy_hands += 1
        return busy_hands

    def _can_equip_hands(self, equipment: Equipment):
        if equipment.is_two_hands and self.busy_hands == 0:
            return True
        if not equipment.is_two_hands and self.busy_hands <= 1:
            return True
        return False

    def equip(self, equipment: Equipment):
        if equipment.body_part == BodyPart.HEAD and not self.head:
            self.head = equipment
        elif equipment.body_part == BodyPart.CHEST and not self.chest:
            self.chest = equipment
        elif equipment.body_part == BodyPart.FEET and not self.feet:
            self.feet = equipment
        elif equipment.body_part == BodyPart.HAND and self._can_equip_hands(equipment):
            self.hands = equipment
        elif equipment.body_part == BodyPart.OTHER:
            self.other.append(equipment)
