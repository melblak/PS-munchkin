from enum import Enum
from typing import Optional

from treasure import Treasure


class BodyPart(Enum):
    HEAD = "HEAD"
    HAND = "HAND"
    CHEST = "CHEST"
    FEET = "FEET"


class Equipment(Treasure):
    def __init__(
        self,
        name,
        description,
        strength,
        item_type,
        is_big: bool = False,
        is_two_hands: bool = False,
        body_part: Optional[BodyPart] = None,
    ):
        super().__init__(name, description, strength, item_type)
        self.is_big = is_big
        self.is_two_hands = is_two_hands
        self.body_part = body_part

    def equip(self, player):
        """
        Equip the equipment card to the player.
        Ensure the player can only equip one item of each type (weapon, armor).
        """
        if self.item_type == "weapon" and any(
            item.item_type == "weapon" for item in player.items
        ):
            print(
                f"{player.name} already has a weapon equipped! You cannot equip another weapon."
            )
        elif self.item_type == "armor" and any(
            item.item_type == "armor" for item in player.items
        ):
            print(
                f"{player.name} already has armor equipped! You cannot equip another armor."
            )
        else:
            super().equip(player)
            print(f"{player.name} equipped {self.name} ({self.item_type})")

    def __str__(self):
        return f"{super().__str__()} (Equippable as {self.item_type})"
