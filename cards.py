from equipment import Equipment, BodyPart
from treasure import Treasure

invocar_regras_obscuras = Treasure(
    name="Invocar Regras Obscuras",
    description="Suba um nivel",
    strength=None,
    special_effect=None,
    value=None,
)

armadura_gosmenta = Equipment(
    name="Armadura Gosmenta",
    description=None,
    strength=1,
    item_type=None,
    body_part=BodyPart.CHEST,
)

missil_magico = Treasure(
    name="Missil Mágico",
    description="Use durante o combate. +5 para qualquer um dos lados. Consumível",
    strength=5,
    special_effect=None,
    value=300,
)

varinha_de_radiestesia = Treasure(
    name="Varinha de Radiestesia",
    description="Percorra as pilhas de descarte e escolha uma carta. Pegue-a e descarte essa.",
    strength=None,
    special_effect=None,
    value=1100,
)

broquel_da_bravata = Equipment(
    name="Broquel da Bravata",
    description=None,
    strength=2,
    body_part=BodyPart.HAND,
    value=400,
)

bandana_de_machao = Equipment(
    name="Bandana de Machão",
    description="Só para Humanos",
    strength=3,
    item_type=None,
    body_part=BodyPart.HEAD,
    value=400,
)

reserva = Treasure(
    name="Reserva!",
    description="Compre mais 3 tesouros imediatamente. Eles são virados para baixo se você comprou essa carta virada para baixo; do contrário, são virados para cima.",
    strength=None,
    special_effect=None,
    value=None,
)

pocao_de_halitose = Treasure(
    name="Poção de Halitose",
    description="Use durante o combate. +2 para qualquer um dos lados, ou instantaneamente mata o Nariz Flutuante. Consumível.",
    strength=2,
    special_effect=None,
    value=100,
)

pocao_da_amizade = Treasure(
    name="Poção da Amizade",
    description="Use durante o combate. Discarte todos os monstros em combate. Nenhum tesouro é ganho, mas o jogador poderá Saquear a Sala. Consumível.",
    strength=None,
    special_effect=None,
    value=200,
)

alabarda_suica = Equipment(
    name="Alabarda Suíça",
    description="Só para Humanos",
    strength=4,
    body_part=BodyPart.HAND,
    is_big=True,
    is_two_hands=True,
    value=600,
)

anel_do_desejo = Treasure(
    name="Anel do Desejo",
    description="Cancela qualquer maldição. Jogue a qualquer momento. Consumível.",
    strength=None,
    special_effect=None,
    value=500,
)

serra_eletrica_de_mutilacao_sangrenta = Equipment(
    name="Serra Elétrica de Mutilação Sangrenta",
    description=None,
    strength=3,
    body_part=BodyPart.HAND,
    is_big=True,
    is_two_hands=True,
    value=600,
)

pocao_de_transferencia = Treasure(
    name="Poção de Transferência",
    description="Use durante o combate. Qualquer jogador(de sua escolha) enfrenta o(s) monstro(s), pode pedir ajuda normalmente e recebe os tesouros e níveis se vencer. O jogador original em seguida continua seu turno, e pode Saquear a Sala tendo o combate sido vencido ou perdido. Consumível.",
    strength=None,
    special_effect=None,
    value=300,
)

armadura_flamejante = Equipment(
    name="Armadura Flamejante",
    description=None,
    strength=2,
    body_part=BodyPart.CHEST,
    value=400,
)

espada_que_canta_e_danca = Equipment(
    name="Espada que Canta e Dança",
    description="Não pode ser usada por ladrões.",
    strength=2,
    value=400,
)

botas_de_chutar_a_bunda = Equipment(
    name="Botas de Chutar a Bunda",
    description=None,
    strength=2,
    body_part=BodyPart.FEET,
    value=400,
)

titulo_realmente_impressionante = Equipment(
    name="Título Realmente Impressionante",
    description=None,
    strength=3,
    )

tubo_de_cola= Treasure(
    name="Tubo de Cola",
    description="Use quando alguém fugir de um combate com sucesso de qualquer forma. O jogador precisará rolar o dado novamente para fugir(Mesmo se tiver sido automático da primeira vez). Consumível.",
    strength=None,
    special_effect=None,
    value=100,
)

agua_mineral_de_marca = Treasure(
    name="Água Mineral de Marca",
    description="Use durante o combate. +2 para cada Elfo em batalha. Consumível.",
    strength=2,
    special_effect=None,
    value=100,
)

florete_da_injustica = Equipment(
    name="Florete da Injustiça",
    description=None,
    strength=3,
    body_part=BodyPart.HAND,
    value=600,
)