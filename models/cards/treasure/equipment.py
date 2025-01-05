from typing import Optional

from models.player.body_part import BodyPart
from models.cards.treasure.treasure import Treasure


class Equipment(Treasure):
    def __init__(
        self,
        name,
        description,
        strength,
        value=None,
        is_big: bool = False,
        is_two_hands: bool = False,
        body_part: Optional[BodyPart] = None,
    ):
        super().__init__(name, description, False)
        self.strength = strength
        self.value = value
        self.is_big = is_big
        self.is_two_hands = is_two_hands
        self.body_part = body_part
