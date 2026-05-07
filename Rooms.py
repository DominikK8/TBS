from TBS import Room, Exit
from typing import Dict

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
        "WEST": Exit("WEST", target="ROOM2_16"),
    },
)

ROOM1_2 = Room(
    id="ROOM1_2",
    desc="ROOM1_2",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Osten.",
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
        "EAST": Exit("EAST", target="MIDDLE"),
        "SOUTH": Exit("SOUTH", target="ROOM1_5"),
    },
)

ROOM1_5 = Room(
    id="ROOM1_5",
    desc="ROOM1_5",
    ldesc="Du bist in einer Kurve, es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_4"),
        "WEST" : Exit("WEST", target="ROOM2_8"),
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
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_1"),
        "SOUTH": Exit("SOUTH", target="ROOM1_7"),
    },
)   

ROOM2_1 = Room(
    id="ROOM2_1",
    desc="ROOM2_1",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_2"),
        "SOUTH": Exit("SOUTH", target="ROOM2_16"),
    },
)

ROOM2_2 = Room(
    id="ROOM2_2",
    desc="ROOM2_2",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Osten.",
    exits={
        "EAST": Exit("EAST", target="ROOM2_3"),
    },
)

ROOM2_3 = Room(
    id="ROOM2_3",
    desc="ROOM2_3",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Osten und Süden.",
    exits={
        "EAST": Exit("EAST", target="ROOM2_4"),
        "WEST": Exit("WEST", target="ROOM2_2"),
        "NORTH": Exit("NORTH", target="ROOM3_4"),
    },
)

ROOM2_4 = Room(
    id="ROOM2_4",
    desc="ROOM2_4",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Osten und Süden.",
    exits={
        "EAST": Exit("EAST", target="ROOM2_5"),
        "WEST": Exit("WEST", target="ROOM2_3"),
        "NORTH": Exit("NORTH", target="ROOM2_5"),
    },
)

ROOM2_5 = Room(
    id="ROOM2_5",
    desc="ROOM2_5",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Süden, Osten und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_6"),
        "WEST": Exit("WEST", target="ROOM2_4"),
        "EAST": Exit("EAST", target="ROOM3_8"),
    },
)

ROOM2_6 = Room(
    id="ROOM2_6",
    desc="ROOM2_6",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Norden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_5"),
    
    },
)

ROOM2_7 = Room(
    id="ROOM2_7",
    desc="ROOM2_7",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Süden.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_8"),
        
        
    },
)

ROOM2_8 = Room(
    id="ROOM2_8",
    desc="ROOM2_8",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Süden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_7"),
        "SOUTH": Exit("SOUTH", target="ROOM2_9"),
        "EAST": Exit("EAST", target="ROOM1_5"),
    },
)

ROOM2_9 = Room(
    id="ROOM2_9",
    desc="ROOM2_9",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_8"),
        "EAST": Exit("EAST", target="ROOM2_10"),
    },
)

ROOM2_10 = Room(
    id="ROOM2_10",
    desc="ROOM2_10",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "WEST": Exit("WEST", target="ROOM2_9"),
        "EAST": Exit("EAST", target="ROOM2_11"),
    },
)

ROOM2_11 = Room(
    id="ROOM2_11",
    desc="ROOM2_11",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "WEST": Exit("WEST", target="ROOM2_10"),
        "EAST": Exit("EAST", target="ROOM2_12"),
    },
)

ROOM2_12 = Room(
    id="ROOM2_12",
    desc="ROOM2_12",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Osten.",
    exits={
        "SOUTH": Exit("SOUTH", target="3_15"),
        "EAST": Exit("EAST", target="ROOM2_11"),
    },
)

ROOM2_13 = Room(
    id="ROOM2_13",
    desc="ROOM2_13",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_16"),
        "NORTH": Exit("NORTH", target="ROOM2_14"),
    },
)

ROOM2_14 = Room(
    id="ROOM2_14",
    desc="ROOM2_14",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Süden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_15"),
        "SOUTH": Exit("SOUTH", target="ROOM2_13"),
        "WEST": Exit("WEST", target="ROOM3_19"),
    },
)

ROOM2_15 = Room(
    id="ROOM2_15",
    desc="ROOM2_15",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_14"),
        "NORTH": Exit("NORTH", target="ROOM2_16"),
    },
)

ROOM2_16 = Room(
    id="ROOM2_16",
    desc="ROOM2_16",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Süden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_1"),
        "SOUTH": Exit("SOUTH", target="ROOM2_15"),
        "EAST": Exit("EAST", target="ROOM1_1"),
    },
)

ROOM3_1 = Room(
    id="ROOM3_1",
    desc="ROOM3_1",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "EAST": Exit("EAST", target="ROOM3_2"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM3_2 = Room(
    id="ROOM3_2",
    desc="ROOM3_2",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Süden und Osten und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="END"),
        "SOUTH": Exit("SOUTH", target="ROOM2_1"),
        "EAST": Exit("EAST", target="ROOM3_3"),
        "WEST": Exit("WEST", target="ROOM3_1"),
    },
)

ROOM3_3 = Room(
    id="ROOM3_3",
    desc="ROOM3_3",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "EAST": Exit("EAST", target="ROOM3_4"),
        "WEST": Exit("WEST", target="ROOM3_2"),
    },
)

ROOM3_4 = Room(
    id="ROOM3_4",
    desc="ROOM3_4",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_3"),
        "WEST": Exit("WEST", target="ROOM3_3"),
    },
)

ROOM3_5 = Room(
    id="ROOM3_5",
    desc="ROOM3_5",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Osten.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_4"),
        "EAST": Exit("EAST", target="ROOM3_6"),
    },
)

ROOM3_6 = Room(
    id="ROOM3_6",
    desc="ROOM3_6",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Osten und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="END"),
        "EAST": Exit("EAST", target="ROOM3_7"),
        "WEST": Exit("WEST", target="ROOM3_5"),
    },
)

ROOM3_7 = Room(
    id="ROOM3_7",
    desc="ROOM3_7",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM3_6"),
        "EAST": Exit("EAST", target="END"),
    },
)

ROOM3_8 = Room(
    id="ROOM3_8",
    desc="ROOM3_8",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Westen und Süden.",
    exits={
        "WEST": Exit("WEST", target="ROOM2_5"),
        "SOUTH": Exit("SOUTH", target="ROOM3_9"),
    },
)

ROOM3_9 = Room(
    id="ROOM3_9",
    desc="ROOM3_9",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_8"),
        "EAST": Exit("EAST", target="END"),
    },
)

ROOM3_10 = Room(
    id="ROOM3_10",
    desc="ROOM3_10",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Osten.",
    exits={
        "EAST": Exit("EAST", target="END"),
    },
)

ROOM3_11 = Room(
    id="ROOM3_11",
    desc="ROOM3_11",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Süden, Osten und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="END"),
        "EAST": Exit("EAST", target="END"),
        "WEST": Exit("WEST", target="ROOM3_12"),
    },
)

ROOM3_12 = Room(
    id="ROOM3_12",
    desc="ROOM3_12",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM3_13"),
        "EAST": Exit("EAST", target="ROOM3_11"),
    },
)

ROOM3_13 = Room(
    id="ROOM3_13",
    desc="ROOM3_13",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM3_14"),
        "EAST": Exit("EAST", target="ROOM3_12"),
    },
)

ROOM3_14 = Room(
    id="ROOM3_14",
    desc="ROOM3_14",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM3_15"),
        "EAST": Exit("EAST", target="ROOM3_13"),
    },
)

ROOM3_15 = Room(
    id="ROOM3_15",
    desc="ROOM3_15",
    ldesc="Du bist in einer Spaltung des Weges. Es gibt Wege nach Norden, Süden, Osten und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="END"),
        "EAST": Exit("EAST", target="ROOM3_14"),
        "WEST": Exit("WEST", target="ROOM3_16"),
        "NORTH": Exit("NORTH", target="ROOM2_12"),
    },
)

ROOM3_16 = Room(
    id="ROOM3_16",
    desc="ROOM3_16",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_13"),
        "EAST": Exit("EAST", target="ROOM3_15"),
    },
)

ROOM3_17 = Room(
    id="ROOM3_17",
    desc="ROOM3_17",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_18"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM3_18 = Room(
    id="ROOM3_18",
    desc="ROOM3_18",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_17"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM3_19 = Room(
    id="ROOM3_19",
    desc="ROOM3_19",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_20"),
        "EAST": Exit("EAST", target="ROOM2_14"),
    },
)

ROOM3_20 = Room(
    id="ROOM3_20",
    desc="ROOM3_20",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_21"),
        "SOUTH": Exit("SOUTH", target="ROOM3_19"),
    },
)

ROOM3_21 = Room(
    id="ROOM3_21",
    desc="ROOM3_21",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_22"),
        "SOUTH": Exit("SOUTH", target="ROOM3_20"),
    },
)

ROOM3_22 = Room(
    id="ROOM3_22",
    desc="ROOM3_22",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_21"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM4_1 = Room(
    id="ROOM4_1",
    desc="ROOM4_1",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Osten.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_2"),
        "EAST": Exit("EAST", target="ROOM4_2"),
    },
)

ROOM4_2 = Room(
    id="ROOM4_2",
    desc="ROOM4_2",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM4_1"),
        "EAST": Exit("EAST", target="ROOM4_3"),
    },
)

ROOM4_3 = Room(
    id="ROOM4_3",
    desc="ROOM4_3",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM4_2"),
        "EAST": Exit("EAST", target="ROOM4_4"),
    },
)



ROOMS: Dict[str, Room] = {
    r.id: r for r in [MIDDLE, END, ROOM1_1, ROOM1_2, ROOM1_3, ROOM1_4, ROOM1_5, ROOM1_6, ROOM1_7, ROOM1_8, ROOM2_1, ROOM2_2, ROOM2_3, ROOM2_4, ROOM2_5, ROOM2_6, ROOM2_7, ROOM2_8, ROOM2_9, ROOM2_10, ROOM2_11, ROOM2_12, ROOM2_13, ROOM2_14, ROOM2_15, ROOM2_16, ROOM3_1, ROOM3_2, ROOM3_3, ROOM3_4, ROOM3_5, ROOM3_6, ROOM3_7, ROOM3_8, ROOM3_9, ROOM3_10, ROOM3_11, ROOM3_12, ROOM3_13, ROOM3_14, ROOM3_15, ROOM3_16, ROOM3_17, ROOM3_18, ROOM3_19, ROOM3_20, ROOM3_21, ROOM3_22, ROOM4_1, ROOM4_2 ]
}