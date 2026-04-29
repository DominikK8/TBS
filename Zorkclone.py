"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Set, Union

# ---------------- Conditions ----------------

class Condition:
    def check(self, state: "GameState") -> bool:
        raise NotImplementedError

@dataclass(frozen=True)
class FlagCondition(Condition):
    flag: str

    def check(self, state: "GameState") -> bool:
        return self.flag in state.flags

@dataclass(frozen=True)
class ObjectStateCondition(Condition):
    obj: str
    key: str
    expected: object = True

    def check(self, state: "GameState") -> bool:
        return state.objects.get(self.obj, {}).get(self.key) == self.expected

# ---------------- Core model ----------------

@dataclass
class Exit:
    direction: str
    target: Optional[str] = None
    blocked_msg: Optional[str] = None
    condition: Optional[Condition] = None

    def allowed(self, state: "GameState") -> bool:
        return self.condition.check(state) if self.condition else True

@dataclass
class Room:
    id: str
    in_group: str
    desc: str
    ldesc: Optional[str] = None
    exits: Dict[str, Exit] = field(default_factory=dict)
    action: Optional[Callable[["GameState", "Room", str], None]] = None
    flags: Set[str] = field(default_factory=set)
    global_objects: Set[str] = field(default_factory=set)

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

        # blocked message exit (e.g. EAST "The door is boarded...")
        if ex.blocked_msg:
            state.output(ex.blocked_msg)
            return None

        return ex.target

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

# ---------------- Action hooks (placeholders) ----------------

def west_house_action(state: GameState, room: Room, verb: str) -> None:
    # Placeholder for (ACTION WEST-HOUSE)
    pass

def stone_barrow_fcn(state: GameState, room: Room, verb: str) -> None:
    pass

def east_house_action(state: GameState, room: Room, verb: str) -> None:
    pass

def forest_room_action(state: GameState, room: Room, verb: str) -> None:
    pass

# ---------------- Rooms (yours, translated) ----------------

WEST_OF_HOUSE = Room(
    id="WEST-OF-HOUSE",
    in_group="ROOMS",
    desc="West of House",
    exits={
        "NORTH": Exit("NORTH", target="NORTH-OF-HOUSE"),
        "SOUTH": Exit("SOUTH", target="SOUTH-OF-HOUSE"),
        "NE":    Exit("NE",    target="NORTH-OF-HOUSE"),
        "SE":    Exit("SE",    target="SOUTH-OF-HOUSE"),
        "WEST":  Exit("WEST",  target="FOREST-1"),
        "EAST":  Exit("EAST",  blocked_msg="The door is boarded and you can't remove the boards."),
        "SW":    Exit("SW",    target="STONE-BARROW", condition=FlagCondition("WON-FLAG")),
        "IN":    Exit("IN",    target="STONE-BARROW", condition=FlagCondition("WON-FLAG")),
    },
    action=west_house_action,
    flags={"RLANDBIT", "ONBIT", "SACREDBIT"},
    global_objects={"WHITE-HOUSE", "BOARD", "FOREST"},
)

STONE_BARROW = Room(
    id="STONE-BARROW",
    in_group="ROOMS",
    desc="Stone Barrow",
    ldesc=("You are standing in front of a massive barrow of stone. In the east face\n"
           "is a huge stone door which is open. You cannot see into the dark of the tomb."),
    exits={
        "NE": Exit("NE", target="WEST-OF-HOUSE"),
    },
    action=stone_barrow_fcn,
    flags={"RLANDBIT", "ONBIT", "SACREDBIT"},
)

NORTH_OF_HOUSE = Room(
    id="NORTH-OF-HOUSE",
    in_group="ROOMS",
    desc="North of House",
    ldesc=("You are facing the north side of a white house. There is no door here,\n"
           "and all the windows are boarded up. To the north a narrow path winds through\n"
           "the trees."),
    exits={
        "SW":    Exit("SW", target="WEST-OF-HOUSE"),
        "SE":    Exit("SE", target="EAST-OF-HOUSE"),
        "WEST":  Exit("WEST", target="WEST-OF-HOUSE"),
        "EAST":  Exit("EAST", target="EAST-OF-HOUSE"),
        "NORTH": Exit("NORTH", target="PATH"),
        "SOUTH": Exit("SOUTH", blocked_msg="The windows are all boarded."),
    },
    flags={"RLANDBIT", "ONBIT", "SACREDBIT"},
    global_objects={"BOARDED-WINDOW", "BOARD", "WHITE-HOUSE", "FOREST"},
)

SOUTH_OF_HOUSE = Room(
    id="SOUTH-OF-HOUSE",
    in_group="ROOMS",
    desc="South of House",
    ldesc=("You are facing the south side of a white house. There is no door here,\n"
           "and all the windows are boarded."),
    exits={
        "WEST":  Exit("WEST", target="WEST-OF-HOUSE"),
        "EAST":  Exit("EAST", target="EAST-OF-HOUSE"),
        "NE":    Exit("NE", target="EAST-OF-HOUSE"),
        "NW":    Exit("NW", target="WEST-OF-HOUSE"),
        "SOUTH": Exit("SOUTH", target="FOREST-3"),
        "NORTH": Exit("NORTH", blocked_msg="The windows are all boarded."),
    },
    flags={"RLANDBIT", "ONBIT", "SACREDBIT"},
    global_objects={"BOARDED-WINDOW", "BOARD", "WHITE-HOUSE", "FOREST"},
)

EAST_OF_HOUSE = Room(
    id="EAST-OF-HOUSE",
    in_group="ROOMS",
    desc="Behind House",
    exits={
        "NORTH": Exit("NORTH", target="NORTH-OF-HOUSE"),
        "SOUTH": Exit("SOUTH", target="SOUTH-OF-HOUSE"),
        "SW":    Exit("SW", target="SOUTH-OF-HOUSE"),
        "NW":    Exit("NW", target="NORTH-OF-HOUSE"),
        "EAST":  Exit("EAST", target="CLEARING"),
        "WEST":  Exit("WEST", target="KITCHEN",
                     condition=ObjectStateCondition("KITCHEN-WINDOW", "open", True)),
        "IN":    Exit("IN", target="KITCHEN",
                     condition=ObjectStateCondition("KITCHEN-WINDOW", "open", True)),
    },
    action=east_house_action,
    flags={"RLANDBIT", "ONBIT", "SACREDBIT"},
    global_objects={"WHITE-HOUSE", "KITCHEN-WINDOW", "FOREST"},
)

FOREST_1 = Room(
    id="FOREST-1",
    in_group="ROOMS",
    desc="Forest",
    ldesc=("This is a forest, with trees in all directions. To the east,\n"
           "there appears to be sunlight."),
    exits={
        "UP":    Exit("UP", blocked_msg="There is no tree here suitable for climbing."),
        "NORTH": Exit("NORTH", target="EAST-OF-HOUSE"),
        "EAST":  Exit("EAST", target="PATH"),
        "SOUTH": Exit("SOUTH", target="FOREST-3"),
        "WEST":  Exit("WEST", blocked_msg="You would need a machete to go further west."),
    },
    action=forest_room_action,
    flags={"RLANDBIT", "ONBIT", "SACREDBIT"},
    global_objects={"TREE", "SONGBIRD", "WHITE-HOUSE", "FOREST"},
)

ROOMS: Dict[str, Room] = {
    r.id: r for r in [WEST_OF_HOUSE, STONE_BARROW, NORTH_OF_HOUSE, SOUTH_OF_HOUSE, EAST_OF_HOUSE, FOREST_1]
}

# ---------------- Minimal loop ----------------

DIR_ALIASES = {
    "N": "NORTH", "S": "SOUTH", "E": "EAST", "W": "WEST",
    "NE": "NE", "NW": "NW", "SE": "SE", "SW": "SW",
    "U": "UP", "D": "DOWN",
    "IN": "IN", "OUT": "OUT",
}

def show_room(room: Room) -> None:
    print(f"\n== {room.desc} ==")
    print(room.describe())
    exits = ", ".join(sorted(room.exits.keys()))
    print(f"[Exits: {exits}]")

def normalize_dir(token: str) -> str:
    t = token.strip().upper()
    return DIR_ALIASES.get(t, t)

def game_loop(start_room: str = "WEST-OF-HOUSE") -> None:
    state = GameState(
        flags=set(),
        objects={"KITCHEN-WINDOW": {"open": False}},  # start: closed
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
            print("Commands: look|l, go <dir>, or just <dir> (n,sw,in,...)")
            print("          open window | close window")
            print("          flag <NAME>   (e.g. flag WON-FLAG)")
            print("          flags         (show flags)")
            print("          quit")
            continue

        if head in ("look", "l"):
            if current.action:
                current.action(state, current, "LOOK")
            show_room(current)
            state.flush_output()
            continue

        # --- toggle window (to satisfy 'IF KITCHEN-WINDOW IS OPEN') ---
        if head in ("open", "close") and len(parts) >= 2 and parts[1].lower() == "window":
            new_val = (head == "open")
            state.objects.setdefault("KITCHEN-WINDOW", {})["open"] = new_val
            print(f"KITCHEN-WINDOW is now {'open' if new_val else 'closed'}.")
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
            if current.action:
                current.action(state, current, "ENTER")
            show_room(current)
        else:
            # either blocked message already printed, or not possible
            if not state.messages:
                print("You can't go that way.")
        state.flush_output()


if __name__ == "__main__":
    game_loop()
    """