from equipment import Equipment, BodyPart
from treasure import Treasure

invocar_regras_obscuras = Treasure(
    "Invocar regras obscuras",
    "Suba um nivel",
    strength=None,
    special_effect=None,
    value=None,
)

armadura_gosmenta = Equipment(
    name="Armadura gosmenta",
    description=None,
    strength=1,
    item_type=None,
    body_part=BodyPart.CHEST,
)
