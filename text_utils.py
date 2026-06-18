import text
import random

DIRECTION_NAMES = {
    "NORTH": "Norden",
    "SOUTH": "Süden",
    "EAST":  "Osten",
    "WEST":  "Westen"
}

ORDER = ["NORTH", "EAST", "SOUTH", "WEST"]

def format_exit_text(directions):
    directions = [d for d in ORDER if d in directions]
    names = [DIRECTION_NAMES[d] for d in directions]

    if not names:
        return random.choice(text.NO_EXITS)

    if len(names) == 1:
        return random.choice(text.ONE_EXIT).format(names[0])

    if len(names) == 2:
        return random.choice(text.TWO_EXITS).format(names[0], names[1])

    if len(names) == 3:
        return random.choice(text.THREE_EXITS).format(names[0], names[1], names[2])

    return random.choice(text.FOUR_EXITS).format(names[0], names[1], names[2], names[3])