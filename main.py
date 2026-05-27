from TBS import GameState, Room, FlagCondition
from Rooms import ROOMS
import random
import text
from typing import Optional
from Items import ALL_ITEMS
import time

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
    print(f"\n== {room.describe()} ==")

# Ausgabe der detaillierten Beschreibung eines Raumes
def looking_room(room: Room) -> None:
    print(room.look())

# Normalisierung/ Übersetzung der Richtungsangaben (z.B. "n" -> "NORTH")
def normalize_dir(token: str) -> str:
    t = token.strip().upper()
    return DIR_ALIASES.get(t, t)

def current_items_list(state):
    return [
        it for it in ALL_ITEMS.values()
        if it.flag_name in state.flags
        and (it.used_flag is None or it.used_flag not in state.flags)
    ]

def current_items_list_enumerate(current_items):
    result = []
    for i, it in enumerate(current_items, start=1):
        result.append(f"{i}) {it.display_name()}")
    return result

# Definition des Hauptspiel-Loops und des Startpunktes (über Variable START_ROOM)
def game_loop(start_room: str = START_ROOM) -> Optional[str]:
    state = GameState(
        flags=set(),
    )
    current = ROOMS[start_room]
    show_room(current)

# Hauptspiel-Loop
    while True:
        textwait = float(0.5)

        # überprüfen, ob das Spiel vorbei ist (z.B. durch Erreichen eines Ausgangs) und ggf. Neustart oder Beenden anbieten  
        if state.game_over:
            if "WON-FLAG" in state.flags:
                print(text.WON)
            
            else:
                print(text.GAME_OVER)

            while True:
                choice = input("> ").strip().lower()

                if choice in ("q", "quit", "exit"):
                    print(text.END)
                    return   # game_loop beenden

                elif choice in ("n", "new", "neu"):
                    print(text.NEW_GAME)
                    return "NEW"  # Signal nach außen
                
                if "WON-FLAG" not in state.flags:
                    if choice in ("z", "zurück", "b", "back"):
                        state.game_over = False  # Spiel zurücksetzen, aber im aktuellen Raum bleiben
                        show_room(current)
                        break  # Einfach den inneren Loop verlassen und zum Hauptloop zurückkehren
                    else:
                        print(text.END_GAME_INPUT_REPETITION_WON)
                    
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
            state.game_over = True  # Spiel beenden
            continue

        if head in ("help", "hilfe", "h", "?"):
            print(text.HELP)
            continue

        if head in ("look", "l", "umschauen", "u"):
            show_room(current)
            looking_room(current)

            itemtext = current.find_item(state)
            if itemtext:
                print(f"\n{itemtext}")

            blocker_flag = current.exit_blocked_flag(state)
            blocked_msg  = current.exit_blocked_message(state)
            if blocked_msg:
                print(blocked_msg)
                
                choice = input("> ").strip().lower()

                if choice in ("j", "ja"):
                    current_items = current_items_list(state)

                    if not current_items:
                        print(text.NO_ITEMS)
                        continue
                    # Liste einmal komplett ausgeben
                    
                    for line in current_items_list_enumerate(current_items):
                        print(line)

                    print(text.ITEM_CHOICE)

                    while True:
                        choice_loop = input("> ").strip().lower()

                        if choice_loop in ("z", "zurück", "zurueck"):
                            print(text.LEAVE_DIALOG)
                            break

                        if choice_loop.isdigit():

                            index = int(choice_loop) - 1
                            if not (0 <= index < len(current_items)):
                                print(f"'{choice_loop}' {text.NOT_IN_CHOICE}")
                                
                            else: 
                                chosen_item = current_items[index]
                                print(f"{text.GIVE_ITEM} {chosen_item.name}")
                                time.sleep(textwait)
                                print(chosen_item.item_reaktion)
                                time.sleep(textwait)
                                # optional: Item als benutzt markieren
                                if chosen_item.used_flag:
                                    state.flags.add(chosen_item.used_flag)

                                if blocker_flag in chosen_item.solves:
                                    state.flags.add(blocker_flag)
                                    print(text.REDBUG_UNBLOCK)
                                    break
                                else:
                                    print(text.REDBUG_STAYS)
                                    current_items = current_items_list(state)
                                    for line in current_items_list_enumerate(current_items):
                                        print(line)
                        else:
                            print(text.ITEM_CHOICE)

                elif choice in ("n", "nein"):
                    print(text.LEAVE_DIALOG)
                else:
                    print(text.DIALOG_OPTIONS)
                    continue

            continue

        # Richtung aus dem Befehl extrahieren (z.B. "go east" -> "EAST", "n" -> "NORTH", ...)
        direction = None
        if head in ("go", "gehe") and len(parts) >= 2:
            direction = normalize_dir(parts[1])
        elif head in ("go", "gehe") and len(parts) < 2:
            print(text.GO_WHERE)
            continue
        else:
            direction = normalize_dir(parts[0])
        
        # Überprüfen, ob die Richtung gültig ist und ggf. Raumwechsel durchführen
        if direction not in VALID_DIRECTIONS:
            print(text.INVALID_COMMAND1 + f" '{head}' " + text.INVALID_COMMAND2)
            continue
        else:
            target = current.try_move(state, direction)
            if target and target in ROOMS:
                current = ROOMS[target]
                show_room(current)
                
                if current.action:
                    current.action(state, current, cmd)
            #elif 
            else:
                print(random.choice(text.WALL))

# Hauptprogramm: Spiel starten und ggf. Neustart ermöglichen
if __name__ == "__main__":
    print(text.WELCOME)
    while True:
        result = game_loop(START_ROOM)

        if result != "NEW":
            break