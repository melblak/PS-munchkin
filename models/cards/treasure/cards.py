from models.cards.treasure.consumable import Consumable
from models.cards.treasure.equipment import Equipment, BodyPart

invocar_regras_obscuras = Consumable(
    name="Invocar Regras Obscuras",
    description="Suba um nivel",
    strength=None,
    value=None,
)

armadura_gosmenta = Equipment(
    name="Armadura Gosmenta",
    description=None,
    strength=1,
    body_part=BodyPart.CHEST,
)

missil_magico = Consumable(
    name="Missil Mágico",
    description="Use durante o combate. +5 para qualquer um dos lados. Consumível",
    strength=5,
    value=300,
)

varinha_de_radiestesia = Consumable(
    name="Varinha de Radiestesia",
    description="Percorra as pilhas de descarte e escolha uma carta. Pegue-a e descarte essa.",
    strength=None,
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
    body_part=BodyPart.HEAD,
    value=400,
)

reserva = Consumable(
    name="Reserva!",
    description="Compre mais 3 tesouros imediatamente. Eles são virados para baixo se você comprou essa carta virada para baixo; do contrário, são virados para cima.",
    strength=None,
    value=None,
)

pocao_de_halitose = Consumable(
    name="Poção de Halitose",
    description="Use durante o combate. +2 para qualquer um dos lados, ou instantaneamente mata o Nariz Flutuante. Consumível.",
    strength=2,
    value=100,
)

pocao_da_amizade = Consumable(
    name="Poção da Amizade",
    description="Use durante o combate. Discarte todos os monstros em combate. Nenhum tesouro é ganho, mas o jogador poderá Saquear a Sala. Consumível.",
    strength=None,
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

anel_do_desejo = Consumable(
    name="Anel do Desejo",
    description="Cancela qualquer maldição. Jogue a qualquer momento. Consumível.",
    strength=None,
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

pocao_de_transferencia = Consumable(
    name="Poção de Transferência",
    description="Use durante o combate. Qualquer jogador(de sua escolha) enfrenta o(s) monstro(s), pode pedir ajuda normalmente e recebe os tesouros e níveis se vencer. O jogador original em seguida continua seu turno, e pode Saquear a Sala tendo o combate sido vencido ou perdido. Consumível.",
    strength=None,
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

tubo_de_cola = Consumable(
    name="Tubo de Cola",
    description="Use quando alguém fugir de um combate com sucesso de qualquer forma. O jogador precisará rolar o dado novamente para fugir(Mesmo se tiver sido automático da primeira vez). Consumível.",
    strength=None,
    value=100,
)

agua_mineral_de_marca = Consumable(
    name="Água Mineral de Marca",
    description="Use durante o combate. +2 para cada Elfo em batalha. Consumível.",
    strength=2,
    value=100,
)

florete_da_injustica = Equipment(
    name="Florete da Injustiça",
    description=None,
    strength=3,
    body_part=BodyPart.HAND,
    value=600,
)

joelheiras_pontiagudas = Equipment(
    name="Joelheiras Pontiagudas",
    description=None,
    strength=1,
    value=200,
)

escudo_onipresente = Equipment(
    name="Escudo Onipresente",
    description="Só para Guerreiros",
    strength=4,
    body_part=BodyPart.HAND,
    is_big=True,
    value=600,
)

elmo_chifrudo = Equipment(
    name="Elmo Chifrudo",
    description=None,
    strength=1,
    body_part=BodyPart.HEAD,
    value=600,
)

cocao_de_ponfusao = Consumable(
    name="Poção de Ponfusão",
    description="Use durante o combate. +3 para qualquer um dos lados. Consumível.",
    strength=3,
    value=300,
)

armadura_rechonchuda = Equipment(
    name="Armadura Rechonchuda",
    description="Só para Anões",
    strength=3,
    body_part=BodyPart.CHEST,
    value=400,
)

mutilar_os_corpos = Consumable(
    name="Mutilar os Corpos",
    description="Use após o combate. Suba um nível. Consumível.",
)

pocao_de_polimorfia = Consumable(
    name="Poção de Polimorfia",
    description="Use durante o combate. Transforme um monstro em um papagaio que voa deixando seus Tesouros. Consumível.",
    value=1300,
)

ferver_um_formigueiro = Consumable(
    name="Ferver um Formigueiro",
    description="Suba um nível.",
)

armadura_de_couro = Equipment(
    name="Armadura de Couro",
    description=None,
    strength=1,
    body_part=BodyPart.CHEST,
    value=200,
)

dado_viciado = Consumable(
    name="Dado Viciado",
    description="Jogue após rolar o dado, por qualquer motivo. Vire a face de sua escola para cima. Consumível.",
    value=300,
)

martelo_detona_joelho = Equipment(
    name="Martelo Detona Joelho",
    description="Só para Anões.",
    strength=4,
    body_part=BodyPart.HAND,
    value=600,
)

subornar_o_mestre_com_comida = Consumable(
    name="Subornar o Mestre com Comida",
    description="Suba um nível.",
)

roube_um_nivel = Consumable(
    name="Roube um Nível",
    description="Roube um nível de outro jogador. Consumível.",
)

maca_do_cavaleiro = Equipment(
    name="Maça do Cavaleiro",
    description="Só para Homens.",
    strength=4,
    body_part=BodyPart.HAND,
    value=400,
)

mil_pecas_de_ouro = Consumable(
    name="1000 Peças de Ouro",
    description="Suba um nível.",
)

pocao_eletrica_radioativa = Consumable(
    name="Poção Elétrica Radioativa",
    description="Use durante o combate. +5 para qualquer um dos lados. Consumível.",
    strength=5,
    value=200,
)

doppleganger = Consumable(
    name="Doppleganger",
    description="Use durante o combate. Invoca uma cópia exata do jogador, dobrando sua força. Você só pode usar a carta se for o único jogador em combate. Consumível.",
    strength=None,
    value=300,
)

escada = Equipment(
    name="Escada",
    description="Só para Halflings.",
    strength=3,
    is_big=True,
    value=400,
)

armadura_de_mithril = Equipment(
    name="Armadura de Mithril",
    description="Não pode ser usada por magos.",
    strength=3,
    body_part=BodyPart.CHEST,
    is_big=True,
    value=600,
)

pedra_gigante = Equipment(
    name="Pedra Gigante",
    description=None,
    strength=3,
    body_part=BodyPart.HAND,
    is_big=True,
)

hamburguer_de_anchovas = Equipment(
    name="Hamburguer de Anchovas",
    description="Só para Halflings.",
    strength=3,
    value=400,
)

pocao_do_sono = Consumable(
    name="Poção do Sono",
    description="Use durante o combate. +2 para qualquer um dos lados. Consumível.",
    strength=2,
    value=100,
)

erro_conveniente_de_adicao = Consumable(
    name="Erro Conveniente de Adição",
    description="Suba um nível.",
)
