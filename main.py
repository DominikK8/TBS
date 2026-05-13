
from TBS import GameState, Room
from Rooms import ROOMS
import random
import text

#Variablen Definitionen
DIR_ALIASES = {
    "N":     "NORTH",
    "NORD":  "NORTH",
    "NORDEN":"NORTH",

    "S":     "SOUTH",
    "SÜD":   "SOUTH",
    "SÜDEN": "SOUTH",

    "O":     "EAST",
    "E":     "EAST",
    "OST":   "EAST",
    "OSTEN": "EAST",

    "W":     "WEST",
    "WEST":  "WEST",
    "WESTEN":"WEST",
}

VALID_DIRECTIONS = {"NORTH", "SOUTH", "EAST", "WEST"}
START_ROOM = "MIDDLE"

#Funktionen

# Ausgabe des Raumnamens
def show_room(room: Room) -> None:
    print(f"\n== {room.desc} ==")

# Ausgabe der detaillierten Beschreibung eines Raumes
def looking_room(room: Room) -> None:
    print(room.ldesc)

# Normalisierung/ Übersetzung der Richtungsangaben (z.B. "n" -> "NORTH")
def normalize_dir(token: str) -> str:
    t = token.strip().upper()
    return DIR_ALIASES.get(t, t)

# Definition des Hauptspiel-Loops und des Startpunktes (über Variable START_ROOM)
def game_loop(start_room: str = START_ROOM) -> None:
    state = GameState(
        flags=set(),
    )
    current = ROOMS[start_room]
    show_room(current)

# Hauptspiel-Loop
    while True:

        # überprüfen, ob das Spiel vorbei ist (z.B. durch Erreichen eines Ausgangs) und ggf. Neustart oder Beenden anbieten  
        if state.game_over:
            print(text.GAME_OVER)

            while True:
                choice = input("> ").strip().lower()

                if choice in ("q", "quit", "exit"):
                    print("Bye!")
                    return   # game_loop beenden

                elif choice in ("n", "new", "neu"):
                    print(text.NEW_GAME)
                    return "NEW"  # Signal nach außen

                else:
                    print(text.END_GAME_INPUT_REPETITION)

        # Eingabeaufforderung und Verarbeitung der Befehle
        cmd = input("\n> ").strip()
        if not cmd:
            continue

        # einfache Aufteilung des Befehls in Wörter, um z.B. "go east" zu erkennen   
        parts = cmd.split()
        head = parts[0].lower()
        
        # Befehle: "quit", "hilfe", "umschauen", "gehe <dir>", "<dir>", ...
        if head in ("quit", "exit", "q"):
            print("Bye!")
            break

        if head in ("help", "hilfe", "h", "?"):
            print(text.HELP)
            continue

        if head in ("look", "l", "umschauen", "u"):
            looking_room(current)     # Detaillierte Beschreibung
            continue

        # --- set flag quickly for testing ---
        #    if head == "flag" and len(parts) >= 2:
        #     flag_name = parts[1].upper()
        #     state.flags.add(flag_name)
        #     print(f"Flag set: {flag_name}")
        #     continue

        # if head == "flags":
        #     print("Flags:", ", ".join(sorted(state.flags)) if state.flags else "(none)")
        #     continue

        # Richtung aus dem Befehl extrahieren (z.B. "go east" -> "EAST", "n" -> "NORTH", ...)
        direction = None
        if head in ("go", "gehe") and len(parts) >= 2:
            direction = normalize_dir(parts[1])
        else:
            direction = normalize_dir(parts[0])

        # Überprüfen, ob die Richtung gültig ist und ggf. Raumwechsel durchführen
        if direction not in VALID_DIRECTIONS:
            print(f"{text.INVALID_COMMAND1} '{head}' {text.INVALID_COMMAND2}")
            continue
        else:
            target = current.try_move(state, direction)
            if target and target in ROOMS:
                current = ROOMS[target]
                show_room(current)
                
                if current.action:
                    current.action(state, current, cmd)

            else:
                print(random.choice(text.WALL))

        #state.flush_output()

# Hauptprogramm: Spiel starten und ggf. Neustart ermöglichen
if __name__ == "__main__":
    print(text.WELCOME)
    while True:
        result = game_loop(START_ROOM)

        if result != "NEW":
            break