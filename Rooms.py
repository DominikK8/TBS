# Labyrinth Rooms

from TBS import Room, Exit
from typing import Dict
import text

END = Room(
    id="END",
    desc="Ein Ausgang!",
    flags={"WON-FLAG"},
    exits={},
    action=Room.end_action,
)

MIDDLE = Room(
    id="MIDDLE",
    desc=text.MIDDLE_DESC,
    ldesc=text.MIDDLE_LDESC,
    exits={
        "EAST":  Exit("EAST", target="ROOM1_4"),
        "SOUTH": Exit("SOUTH", target="ROOM1_6"),
    },
)

ROOM1_1 = Room(
    id="ROOM1_1",
    desc=text.ROOM1_1_DESC,
    ldesc=text.ROOM1_1_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM1_8"),
        "WEST": Exit("WEST", target="ROOM2_16"),
    },
)

ROOM1_2 = Room(
    id="ROOM1_2",
    desc=text.ROOM1_2_DESC,
    ldesc=text.ROOM1_2_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM1_3"),
    },
)

ROOM1_3 = Room(
    id="ROOM1_3",
    desc=text.ROOM1_3_DESC,
    ldesc=text.ROOM1_3_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM1_2"),
        "SOUTH": Exit("SOUTH", target="ROOM1_4"),
    },
)

ROOM1_4 = Room(
    id="ROOM1_4",
    desc=text.ROOM1_4_DESC,
    ldesc=text.ROOM1_4_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_3"),
        "WEST": Exit("WEST", target="MIDDLE"),
        "SOUTH": Exit("SOUTH", target="ROOM1_5"),
    },
)

ROOM1_5 = Room(
    id="ROOM1_5",
    desc=text.ROOM1_5_DESC,
    ldesc=text.ROOM1_5_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_4"),
        "EAST": Exit("EAST", target="ROOM2_8"),
    },
)

ROOM1_6 = Room(
    id="ROOM1_6",
    desc=text.ROOM1_6_DESC,
    ldesc=text.ROOM1_6_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="MIDDLE"),
        "WEST": Exit("WEST", target="ROOM1_7"),
    },
)

ROOM1_7 = Room(
    id="ROOM1_7",
    desc=text.ROOM1_7_DESC,
    ldesc=text.ROOM1_7_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_8"),
        "EAST": Exit("EAST", target="ROOM1_6"),
    },
)

ROOM1_8 = Room(
    id="ROOM1_8",
    desc=text.ROOM1_8_DESC,
    ldesc=text.ROOM1_8_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM1_1"),
        "SOUTH": Exit("SOUTH", target="ROOM1_7"),
    },
)   

ROOM2_1 = Room(
    id="ROOM2_1",
    desc=text.ROOM2_1_DESC,
    ldesc=text.ROOM2_1_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_2"),
        "SOUTH": Exit("SOUTH", target="ROOM2_16"),
    },
)

ROOM2_2 = Room(
    id="ROOM2_2",
    desc=text.ROOM2_2_DESC,
    ldesc=text.ROOM2_2_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM2_3"),
    },
)

ROOM2_3 = Room(
    id="ROOM2_3",
    desc=text.ROOM2_3_DESC,
    ldesc=text.ROOM2_3_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM2_4"),
        "WEST": Exit("WEST", target="ROOM2_2"),
        "NORTH": Exit("NORTH", target="ROOM3_4"),
    },
)

ROOM2_4 = Room(
    id="ROOM2_4",
    desc=text.ROOM2_4_DESC,
    ldesc=text.ROOM2_4_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM2_5"),
        "WEST": Exit("WEST", target="ROOM2_3"),
        "NORTH": Exit("NORTH", target="ROOM3_5"),
    },
)

ROOM2_5 = Room(
    id="ROOM2_5",
    desc=text.ROOM2_5_DESC,
    ldesc=text.ROOM2_5_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_6"),
        "WEST": Exit("WEST", target="ROOM2_4"),
        "EAST": Exit("EAST", target="ROOM3_8"),
    },
)

ROOM2_6 = Room(
    id="ROOM2_6",
    desc=text.ROOM2_6_DESC,
    ldesc=text.ROOM2_6_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_5"),
    
    },
)

ROOM2_7 = Room(
    id="ROOM2_7",
    desc=text.ROOM2_7_DESC,
    ldesc=text.ROOM2_7_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_8"),
        
        
    },
)

ROOM2_8 = Room(
    id="ROOM2_8",
    desc=text.ROOM2_8_DESC,
    ldesc=text.ROOM2_8_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_7"),
        "SOUTH": Exit("SOUTH", target="ROOM2_9"),
        "WEST": Exit("WEST", target="ROOM1_5"),
    },
)

ROOM2_9 = Room(
    id="ROOM2_9",
    desc=text.ROOM2_9_DESC,
    ldesc=text.ROOM2_9_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_8"),
        "WEST": Exit("WEST", target="ROOM2_10"),
    },
)

ROOM2_10 = Room(
    id="ROOM2_10",
    desc=text.ROOM2_10_DESC,
    ldesc=text.ROOM2_10_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM2_11"),
        "EAST": Exit("EAST", target="ROOM2_9"),
    },
)

ROOM2_11 = Room(
    id="ROOM2_11",
    desc=text.ROOM2_11_DESC,
    ldesc=text.ROOM2_11_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM2_12"),
        "EAST": Exit("EAST", target="ROOM2_10"),
    },
)

ROOM2_12 = Room(
    id="ROOM2_12",
    desc=text.ROOM2_12_DESC,
    ldesc=text.ROOM2_12_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_15"),
        "EAST": Exit("EAST", target="ROOM2_11"),
    },
)

ROOM2_13 = Room(
    id="ROOM2_13",
    desc=text.ROOM2_13_DESC,
    ldesc=text.ROOM2_13_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_16"),
        "NORTH": Exit("NORTH", target="ROOM2_14"),
    },
)

ROOM2_14 = Room(
    id="ROOM2_14",
    desc=text.ROOM2_14_DESC,
    ldesc=text.ROOM2_14_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_15"),
        "SOUTH": Exit("SOUTH", target="ROOM2_13"),
        "WEST": Exit("WEST", target="ROOM3_19"),
    },
)

ROOM2_15 = Room(
    id="ROOM2_15",
    desc=text.ROOM2_15_DESC,
    ldesc=text.ROOM2_15_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_14"),
        "NORTH": Exit("NORTH", target="ROOM2_16"),
    },
)

ROOM2_16 = Room(
    id="ROOM2_16",
    desc=text.ROOM2_16_DESC,
    ldesc=text.ROOM2_16_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_1"),
        "SOUTH": Exit("SOUTH", target="ROOM2_15"),
        "EAST": Exit("EAST", target="ROOM1_1"),
    },
)

ROOM3_1 = Room(
    id="ROOM3_1",
    desc=text.ROOM3_1_DESC,
    ldesc=text.ROOM3_1_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_2"),
        "WEST": Exit("WEST", target="ROOM4_27"),
    },
)

ROOM3_2 = Room(
    id="ROOM3_2",
    desc=text.ROOM3_2_DESC,
    ldesc=text.ROOM3_2_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_1"),
        "SOUTH": Exit("SOUTH", target="ROOM2_1"),
        "EAST": Exit("EAST", target="ROOM3_3"),
        "WEST": Exit("WEST", target="ROOM3_1"),
    },
)

ROOM3_3 = Room(
    id="ROOM3_3",
    desc=text.ROOM3_3_DESC,
    ldesc=text.ROOM3_3_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_4"),
        "WEST": Exit("WEST", target="ROOM3_2"),
    },
)

ROOM3_4 = Room(
    id="ROOM3_4",
    desc=text.ROOM3_4_DESC,
    ldesc=text.ROOM3_4_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_3"),
        "WEST": Exit("WEST", target="ROOM3_3"),
    },
)


ROOM3_5 = Room(
    id="ROOM3_5",
    desc=text.ROOM3_5_DESC,
    ldesc=text.ROOM3_5_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM2_4"),
        "EAST": Exit("EAST", target="ROOM3_6"),
    },
)

ROOM3_6 = Room(
    id="ROOM3_6",
    desc=text.ROOM3_6_DESC,
    ldesc=text.ROOM3_6_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_5"),
        "EAST": Exit("EAST", target="ROOM3_7"),
        "WEST": Exit("WEST", target="ROOM3_5"),
    },
)

ROOM3_7 = Room(
    id="ROOM3_7",
    desc=text.ROOM3_7_DESC,
    ldesc=text.ROOM3_7_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM3_6"),
        "EAST": Exit("EAST", target="ROOM4_8"),
    },
)

ROOM3_8 = Room(
    id="ROOM3_8",
    desc=text.ROOM3_8_DESC,
    ldesc=text.ROOM3_8_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM2_5"),
        "SOUTH": Exit("SOUTH", target="ROOM3_9"),
    },
)

ROOM3_9 = Room(
    id="ROOM3_9",
    desc=text.ROOM3_9_DESC,
    ldesc=text.ROOM3_9_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_8"),
        "EAST": Exit("EAST", target="ROOM4_10"),
    },
)

ROOM3_10 = Room(
    id="ROOM3_10",
    desc=text.ROOM3_10_DESC,
    ldesc=text.ROOM3_10_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM4_11"),
    },
)


ROOM3_11 = Room(
    id="ROOM3_11",
    desc=text.ROOM3_11_DESC,
    ldesc=text.ROOM3_11_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM4_14"),
        "EAST": Exit("EAST", target="ROOM4_13"),
        "WEST": Exit("WEST", target="ROOM3_12"),
    },
)

ROOM3_12 = Room(
    id="ROOM3_12",
    desc=text.ROOM3_12_DESC,
    ldesc=text.ROOM3_12_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM3_13"),
        "EAST": Exit("EAST", target="ROOM3_11"),
    },
)

ROOM3_13 = Room(
    id="ROOM3_13",
    desc=text.ROOM3_13_DESC,
    ldesc=text.ROOM3_13_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM3_14"),
        "EAST": Exit("EAST", target="ROOM3_12"),
    },
)

ROOM3_14 = Room(
    id="ROOM3_14",
    desc=text.ROOM3_14_DESC,
    ldesc=text.ROOM3_14_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM3_15"),
        "EAST": Exit("EAST", target="ROOM3_13"),
        "SOUTH": Exit("SOUTH", target="END"),
    },
)

ROOM3_15 = Room(
    id="ROOM3_15",
    desc=text.ROOM3_15_DESC,
    ldesc=text.ROOM3_15_LDESC,
    exits={
<<<<<<< HEAD
        "SOUTH": Exit("SOUTH", target="ROOM4_18"),
=======
>>>>>>> e507e4b4441caca2799acec3d07ce20ed19305f9
        "EAST": Exit("EAST", target="ROOM3_14"),
        "NORTH": Exit("NORTH", target="ROOM2_12"),
    },
)

ROOM3_16 = Room(
    id="ROOM3_16",
    desc=text.ROOM3_16_DESC,
    ldesc=text.ROOM3_16_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM2_13"),
        "EAST": Exit("EAST", target="ROOM3_15"),
    },
)

ROOM3_17 = Room(
    id="ROOM3_17",
    desc=text.ROOM3_17_DESC,
    ldesc=text.ROOM3_17_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_18"),
        "WEST": Exit("WEST", target="ROOM4_21"),
    },
)

ROOM3_18 = Room(
    id="ROOM3_18",
    desc=text.ROOM3_18_DESC,
    ldesc=text.ROOM3_18_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_17"),
        "WEST": Exit("WEST", target="ROOM4_22"),
    },
)

ROOM3_19 = Room(
    id="ROOM3_19",
    desc=text.ROOM3_19_DESC,
    ldesc=text.ROOM3_19_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_20"),
        "EAST": Exit("EAST", target="ROOM2_14"),
    },
)

ROOM3_20 = Room(
    id="ROOM3_20",
    desc=text.ROOM3_20_DESC,
    ldesc=text.ROOM3_20_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_21"),
        "SOUTH": Exit("SOUTH", target="ROOM3_19"),
    },
)

ROOM3_21 = Room(
    id="ROOM3_21",
    desc=text.ROOM3_21_DESC,
    ldesc=text.ROOM3_21_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_22"),
        "SOUTH": Exit("SOUTH", target="ROOM3_20"),
    },
)

ROOM3_22 = Room(
    id="ROOM3_22",
    desc=text.ROOM3_22_DESC,
    ldesc=text.ROOM3_22_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_21"),
        "WEST": Exit("WEST", target="ROOM4_27"),
    },
)

ROOM4_1 = Room(
    id="ROOM4_1",
    desc=text.ROOM4_1_DESC,
    ldesc=text.ROOM4_1_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_2"),
        "EAST": Exit("EAST", target="ROOM4_2"),
    },
)

ROOM4_2 = Room(
    id="ROOM4_2",
    desc=text.ROOM4_2_DESC,
    ldesc=text.ROOM4_2_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM4_1"),
        "EAST": Exit("EAST", target="ROOM4_3"),
    },
)

ROOM4_3 = Room(
    id="ROOM4_3",
    desc=text.ROOM4_3_DESC,
    ldesc=text.ROOM4_3_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM4_2"),
        "EAST": Exit("EAST", target="ROOM4_4"),
    },
)

ROOM4_4 = Room(
    id="ROOM4_4",
    desc="ROOM4_4",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Westen.",
    exits={
        "WEST": Exit("WEST", target="ROOM4_3"),
    },
)

ROOM4_5 = Room(
    id="ROOM4_5",
    desc="ROOM4_5",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Osten.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_6"),
        "EAST": Exit("EAST", target="ROOM4_6"),
    },
)

ROOM4_6 = Room(
    id="ROOM4_6",
    desc="ROOM4_6",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Westen und Osten.",
    exits={
        "WEST": Exit("WEST", target="ROOM4_5"),
        "EAST": Exit("EAST", target="ROOM4_7"),
    },
)

ROOM4_7 = Room(
    id="ROOM4_7",
    desc="ROOM4_7",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_8"),
        "WEST": Exit("WEST", target="ROOM4_6"),
    },
)

ROOM4_8 = Room(
    id="ROOM4_8",
    desc="ROOM4_8",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_7"),
        "WEST": Exit("WEST", target="ROOM3_7"),
    },
)

ROOM4_9 = Room(
    id="ROOM4_9",
    desc="ROOM4_9",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Osten.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM4_10"),
        "EAST": Exit("EAST", target="END"),
    },
)

ROOM4_10 = Room(
    id="ROOM4_10",
    desc="ROOM4_10",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_9"),
        "WEST": Exit("WEST", target="ROOM3_9"),
    },
)

ROOM4_11= Room(
    id="ROOM4_11",
    desc="ROOM4_11",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Süden und Westen.",
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM4_12"),
        "WEST": Exit("WEST", target="ROOM3_9"),
    },
)

ROOM4_12 = Room(
    id="ROOM4_12",
    desc="ROOM4_12",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_11"),
        "SOUTH": Exit("SOUTH", target="ROOM4_13"),
    },
)

ROOM4_13= Room(
    id="ROOM4_13",
    desc="ROOM4_13",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_12"),
        "WEST": Exit("WEST", target="ROOM3_11"),
    },
)

ROOM4_14= Room(
    id="ROOM4_14",
    desc="ROOM4_14",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_11"),
        "WEST": Exit("WEST", target="ROOM4_15"),
    },
)

ROOM4_15= Room(
    id="ROOM4_15",
    desc="ROOM4_15",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "EAST": Exit("EAST", target="ROOM4_14"),
        "WEST": Exit("WEST", target="ROOM4_16"),
    },
)

ROOM4_16= Room(
    id="ROOM4_16",
    desc="ROOM4_16",
    ldesc="Du bist in einem Gang Es gibt einen Weg nach Osten und Westen.",
    exits={
        "EAST": Exit("EAST", target="ROOM4_15"),
        "WEST": Exit("WEST", target="ROOM4_17"),
    },
)

ROOM4_17= Room(
    id="ROOM4_17",
    desc="ROOM4_17",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Osten.",
    exits={
        "EAST": Exit("EAST", target="ROOM4_16"),
    },
)

ROOM4_18= Room(
    id="ROOM4_18",
    desc="ROOM4_18",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Westen.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_15"),
        "WEST": Exit("WEST", target="ROOM4_19"),
    },
)

ROOM4_19= Room(
    id="ROOM4_19",
    desc="ROOM4_19",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "EAST": Exit("EAST", target="ROOM4_18"),
        "WEST": Exit("WEST", target="ROOM4_20"),
    },
)

ROOM4_20= Room(
    id="ROOM4_20",
    desc="ROOM4_20",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Osten.",
    exits={
        "EAST": Exit("EAST", target="ROOM4_19"),
    },
)

ROOM4_21= Room(
    id="ROOM4_21",
    desc="ROOM4_21",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Osten und Westen.",
    exits={
        "EAST": Exit("EAST", target="ROOM3_17"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM4_22= Room(
    id="ROOM4_22",
    desc="ROOM4_22",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Norden und Osten.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_23"),
        "EAST": Exit("EAST", target="ROOM3_18"),
    },
)

ROOM4_23= Room(
    id="ROOM4_23",
    desc="ROOM4_23",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_24"),
        "SOUTH": Exit("SOUTH", target="ROOM4_22"),
    },
)

ROOM4_24= Room(
    id="ROOM4_24",
    desc="ROOM4_24",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_25"),
        "SOUTH": Exit("SOUTH", target="ROOM4_23"),
    },
)

ROOM4_25= Room(
    id="ROOM4_25",
    desc="ROOM4_25",
    ldesc="Du bist in einem Gang. Es gibt einen Weg nach Norden und Süden.",
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_26"),
        "SOUTH": Exit("SOUTH", target="ROOM4_24"),
    },
)

ROOM4_26= Room(
    id="ROOM4_26",
    desc="ROOM4_26",
    ldesc="Du bist in einer Kurve. Es gibt einen Weg nach Osten und Süden.",
    exits={
        "EAST": Exit("EAST", target="ROOM3_22"),
        "SOUTH": Exit("SOUTH", target="ROOM4_25"),
    },
)

ROOM4_27= Room(
    id="ROOM4_27",
    desc="ROOM4_27",
    ldesc="Du bist in einer Sackgasse. Es gibt einen Weg nach Osten.",
    exits={
        "EAST": Exit("EAST", target="ROOM3_1"),
    },
)



ROOMS: Dict[str, Room] = {
    r.id: r for r in [MIDDLE, END, ROOM1_1, ROOM1_2, ROOM1_3, ROOM1_4, ROOM1_5, ROOM1_6, ROOM1_7, ROOM1_8, ROOM2_1, ROOM2_2, ROOM2_3, ROOM2_4, ROOM2_5, ROOM2_6, ROOM2_7, ROOM2_8, ROOM2_9, ROOM2_10, ROOM2_11, ROOM2_12, ROOM2_13, ROOM2_14, ROOM2_15, ROOM2_16, ROOM3_1, ROOM3_2, ROOM3_3, ROOM3_4, ROOM3_5, ROOM3_6, ROOM3_7, ROOM3_8, ROOM3_9, ROOM3_10, ROOM3_11, ROOM3_12, ROOM3_13, ROOM3_14, ROOM3_15, ROOM3_16, ROOM3_17, ROOM3_18, ROOM3_19, ROOM3_20, ROOM3_21, ROOM3_22, ROOM4_1, ROOM4_2, ROOM4_3, ROOM4_4, ROOM4_5, ROOM4_6, ROOM4_7, ROOM4_8, ROOM4_9, ROOM4_10, ROOM4_11, ROOM4_12, ROOM4_13, ROOM4_14, ROOM4_15, ROOM4_16, ROOM4_17, ROOM4_18, ROOM4_19, ROOM4_20, ROOM4_21, ROOM4_22, ROOM4_23, ROOM4_24, ROOM4_25, ROOM4_26, ROOM4_27 ]
}