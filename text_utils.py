import text

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
        return "Es gibt keine Ausgänge."

    if len(names) == 1:
        return f"Es gibt einen Weg nach {names[0]}."

    if len(names) == 2:
        return f"Es gibt Wege nach {names[0]} und {names[1]}."

    return f"Es gibt Wege nach {', '.join(names[:-1])} und {names[-1]}."