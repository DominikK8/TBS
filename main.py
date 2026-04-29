
from TBS import GameState, Room
from Rooms import ROOMS

DIR_ALIASES = {
    "N":     "NORTH",
    "NORD":  "NORTH",
    "NORDEN":"NORTH",

    "S":     "SOUTH",
    "SÜD":   "SOUTH",
    "SÜDEN": "SOUTH",

    "O":     "EAST",
    "OST":   "EAST",
    "OSTEN": "EAST",

    "W":     "WEST",
    "WEST":  "WEST",
    "WESTEN":"WEST",
}

def show_room(room: Room) -> None:
    print(f"\n== {room.desc} ==")
    print(room.describe())
    

def looking_room(room: Room) -> None:
    print(room.look())
    exits = ", ".join(sorted(room.exits.keys()))
    print(f"[Exits: {exits}]")

def normalize_dir(token: str) -> str:
    t = token.strip().upper()
    return DIR_ALIASES.get(t, t)

def game_loop(start_room: str = "MIDDLE") -> None:
    state = GameState(
        flags=set(),
    )
    current = ROOMS[start_room]
    show_room(current)

    while True:
        cmd = input("\n> ").strip()
        if not cmd:
            continue

        parts = cmd.split()
        head = parts[0].lower()

        # --- quit/help/look ---
        if head in ("quit", "exit", "q"):
            print("Bye!")
            break

        if head in ("help", "?"):
            print("Commands: look|l, go <dir>, or just <dir> (n,s,o,w,...)")
            print("          flag <NAME>   (e.g. flag WON-FLAG)")
            print("          flags         (show flags)")
            print("          quit")
            continue

        if head in ("look", "l"):
            show_room(current)        # Name + Beschreibung
            looking_room(current)     # Exits
            continue

        # --- set flag quickly for testing ---
        if head == "flag" and len(parts) >= 2:
            flag_name = parts[1].upper()
            state.flags.add(flag_name)
            print(f"Flag set: {flag_name}")
            continue

        if head == "flags":
            print("Flags:", ", ".join(sorted(state.flags)) if state.flags else "(none)")
            continue

        # --- movement: "go east" or just "east"/"e" ---
        direction = None
        if head == "go" and len(parts) >= 2:
            direction = normalize_dir(parts[1])
        else:
            direction = normalize_dir(parts[0])

        target = current.try_move(state, direction)
        if target and target in ROOMS:
            current = ROOMS[target]
            show_room(current)
        else:
            # either blocked message already printed, or not possible
            if not state.messages:
                print("You can't go that way.")
        state.flush_output()


if __name__ == "__main__":
    game_loop()