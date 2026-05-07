from TBS import Room, Exit
from typing import Dict

END = Room(
    id="END",
    desc="Ein Ausgang!",
    flags={"WON-FLAG"},
    exits={},
    action=Room.end_action,
)

MIDDLE = Room(
    id="MIDDLE",
    desc="Mitte",
    ldesc=("Du kannst nichts sehen. Es riecht modrig, du kannst kalte feuchte Wände nördlich und westlich von dir ertasten. \n Langsam gewöhnen sich deine Augen an die Dunkelheit und du kannst schemenhaft erkennen, \n dass Wege nach Osten und Süden führen."),
    exits={
        "EAST":  Exit("EAST", target="ROOM1_4"),
        "SOUTH": Exit("SOUTH", target="ROOM1_6"),
    },
)

ROOM1_1 = Room(
    id="ROOM1_1",
    desc="ROOM1_1",
    ldesc="Du in einer Kurve. Es gibt einen Weg nach Süden und nach Westen.",
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
        "EAST": Exit("EAST", target="ROOM1_3"),
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
        "WEST": Exit("WEST", target="MIDDLE"),
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

ROOMS: Dict[str, Room] = {
    r.id: r for r in [MIDDLE, END, ROOM1_1, ROOM1_2, ROOM1_3, ROOM1_4, ROOM1_5, ROOM1_6, ROOM1_7, ROOM1_8]
}