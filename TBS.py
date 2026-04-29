from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Set, Union


class Condition:
    def check(self, state: "GameState") -> bool:
        raise NotImplementedError

@dataclass(frozen=True)
class FlagCondition(Condition):
    flag: str

    def check(self, state: "GameState") -> bool:
        return self.flag in state.flags

@dataclass
class Exit:
    direction: str
    target: Optional[str] = None
    condition: Optional[Condition] = None

    def allowed(self, state: "GameState") -> bool:
        return self.condition.check(state) if self.condition else True

@dataclass
class Room:
    id: str
    desc: str
    ldesc: Optional[str] = None
    exits: Dict[str, Exit] = field(default_factory=dict)
    action: Optional[Callable[["GameState", "Room", str], None]] = None
    flags: Set[str] = field(default_factory=set)

    def describe(self) -> str:
        return self.desc
    
    def look(self) -> str:
        return self.ldesc

    def try_move(self, state: "GameState", direction: str) -> Optional[str]:
        ex = self.exits.get(direction.upper())
        if not ex:
            return None

        # condition (e.g. IF WON-FLAG / IF KITCHEN-WINDOW IS OPEN)
        if not ex.allowed(state):
            return None
        
        return ex.target

        # blocked message exit (e.g. EAST "The door is boarded...")
"""       if ex.blocked_msg:
            state.output(ex.blocked_msg)
            return None"""

                

@dataclass
class GameState:
    flags: Set[str] = field(default_factory=set)
    objects: Dict[str, Dict[str, object]] = field(default_factory=dict)
    messages: list[str] = field(default_factory=list)

    def output(self, msg: str) -> None:
        self.messages.append(msg)

    def flush_output(self) -> None:
        for m in self.messages:
            print(m)
        self.messages.clear()

#_______________________Rooms__________________________
"""
END = Room(
    id="END",
    desc="END",
    ldesc="Du hast das Ende des Labyrinths erreicht. Glückwunsch!",
    flags={"WON-FLAG"},
    exits={},
)

MIDDLE = Room(
    id="MIDDLE",
    desc="MIDDLE",
    ldesc=("Du bist in mitten eines Labyrinths, nach Süden und Osten sind Wege."),
    exits={
        "EAST":  Exit("EAST", target="ROOM1_4"),
        "SOUTH": Exit("SOUTH", target="ROOM1_6"),
    },
)

ROOM1_1 = Room(
    id="ROOM1_1",
    desc="ROOM1_1",
    ldesc="Du in einer Kurve. Es gibt einen Weg nach Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM1_8"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM1_2 = Room(
    id="ROOM1_2",
    desc="ROOM1_2",
    ldesc="Du bist in einer Sackgasse.",
    exits={
        "EAST": Exit("EAST", target="MIDDLE"),
    },
)

ROOM1_3 = Room(
    id="ROOM1_3",
    desc="ROOM1_3",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Westen und Süden.",
    exits={
        "WEST": Exit("WEST", target="ROOM1_2"),
        "SOUTH": Exit("SOUTH", target="ROOM1_4"),
    },
)

ROOM1_4 = Room(
    id="ROOM1_4",
    desc="ROOM1_4",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Osten und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_3"),
        "EAST": Exit("EAST", target="MIDDLE"),
        "SOUTH": Exit("SOUTH", target="ROOM1_5"),
    },
)

ROOM1_5 = Room(
    id="ROOM1_5",
    desc="ROOM1_5",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Norden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_4"),
    },
)

ROOM1_6 = Room(
    id="ROOM1_6",
    desc="ROOM1_6",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Westen und Norden.",
    exits={
        "NORTH": Exit("NORTH", target="MIDDLE"),
        "WEST": Exit("WEST", target="ROOM1_7"),
    },
)

ROOM1_7 = Room(
    id="ROOM1_7",
    desc="ROOM1_7",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_8"),
        "EAST": Exit("EAST", target="ROOM1_6"),
    },
)

ROOM1_8 = Room(
    id="ROOM1_8",
    desc="ROOM1_8",
    ldesc="Du bist in einerKurve. Es gibt einen Weg nach Süden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_1"),
        "SOUTH": Exit("SOUTH", target="ROOM1_7"),
    },
)   


#_______________________Loop__________________________

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
"""    