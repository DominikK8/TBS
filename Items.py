from TBS import Item

ALL_ITEMS = {
    "MATCHBOX": Item(
        flag_name="ITEM_MATCHBOX",
        name="Matchbox-Auto",
        item_desc="Du findest ein Matchbox-Auto und nimmst es mit.",
        item_reaktion="Dieses Modell suche ich schon seit ich ein kleiner Mann war.",
        used_flag="MATCHBOX_USED",
        solves= ["BLOCK_REDBUG"]
    ),
    "KEY": Item(
        flag_name="ITEM_KEY",
        name="Schlüssel",
        item_desc="Ein alter Schlüssel liegt hier.",
        item_reaktion="Der Schlüssel passt perfekt.",
        used_flag="KEY_USED"
    ),
        "LIGHTER": Item(
        flag_name="ITEM_LIGHTER",
        name="Feuerzeug",
        item_desc="In der Ecke liegt ein Feuerzeug, du steckst es in deine Tasche.",
        item_reaktion="Nur Raucher brauchen ein Feuerzeug in der Tasche, damit kann ich nichts anfangen.",
        used_flag="LIGHTER_USED"
    ),
}
