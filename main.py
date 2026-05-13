
from TBS import GameState, Room
from Rooms import ROOMS
import random

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
WALL = ["**BOOF** Du läufst vor eine Wand!", 
        "BÄM! Du bist gegen eine Wand gelaufen!", 
        "Du stößt gegen eine Wand. Autsch!", 
        "Puh, du warst dieses Mal ganz vorsichtig und hast rechtzeitig gesehen, dass da eine Wand ist.",
        "Verd***t, genau mit dem großen Zeh zuerst mitten im Schritt gegen eine Wand.",
        "Tränen schießen dir in die Augen, eine Wand hat dich und vor allem deine Nase abrupt gebremst."]

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
            print("Du hast einen Ausgang gefunden. Herzlichen Glückwunsch!")
            print("Drücke 'Q' zum Beenden oder 'N' für ein neues Spiel.")

            while True:
                choice = input("> ").strip().lower()

                if choice in ("q", "quit", "exit"):
                    print("Bye!")
                    return   # game_loop beenden

                elif choice in ("n", "new", "neu"):
                    print("Neues Spiel startet...")
                    return "NEW"  # Signal nach außen

                else:
                    print("Bitte 'Q' oder 'N' eingeben.")

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
            print("Befehle: umschauen|u, gehe <dir>, oder einfach <dir> (n,s,o,w,...)")
            #print("          flag <NAME>   (e.g. flag WON-FLAG)")
            #print("          flags         (show flags)")
            print("          quit")
            print("\n")
            print("Commands: look|l, go <dir>, or just <dir> (n,s,o,w,...)")
            #print("          flag <NAME>   (e.g. flag WON-FLAG)")
            #print("          flags         (show flags)")
            print("          quit")
            continue

        if head in ("look", "l", "umschauen", "u"):
            show_room(current)        # Name
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
            print(f"Ich kenne die Bedeutung von '{head}' nicht.")
            continue
        else:
            target = current.try_move(state, direction)
            if target and target in ROOMS:
                current = ROOMS[target]
                show_room(current)
                
                if current.action:
                    current.action(state, current, cmd)

            else:
                print(random.choice(WALL))

        #state.flush_output()

# Hauptprogramm: Spiel starten und ggf. Neustart ermöglichen
if __name__ == "__main__":
    print( "\n Das war keine gute Entscheidung, diese Eingabe zu machen. Du bist in einem Labyrinth gelandet. \n Du kannst es nicht sehen, aber es ist da. Du musst einen weg herausfinden. \n Es wäre eine Gute Idee sich umzuschauen, oder nach Hilfe zu Fragen. \n Viel Glück!")
    while True:
        result = game_loop(START_ROOM)

        if result != "NEW":
            break