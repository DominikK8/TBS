# Labyrinth Rooms

from TBS import FlagCondition, Room, Exit
from typing import Dict
from Items import ALL_ITEMS
import text

END = Room(
    id="END",
    desc="Ein Ausgang!",
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
    item=ALL_ITEMS["KEY"]
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
    item=ALL_ITEMS["AIDA"]
)

ROOM3_1 = Room(
    id="ROOM3_1",
    desc=text.ROOM3_1_DESC,
    ldesc=text.ROOM3_1_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_2"),
        "WEST": Exit("WEST", target="ROOM4_26"),
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
    item=ALL_ITEMS["DOCUMENT"]
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
        "SOUTH": Exit("SOUTH", target="ROOM4_13"),
        "EAST": Exit("EAST", target="ROOM4_12"),
        "WEST": Exit("WEST", target="ROOM3_12"),
    },
    item=ALL_ITEMS["DOOR"]
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
        "SOUTH": Exit("SOUTH", target="ROOM4_16"),
    },
)

ROOM3_15 = Room(
    id="ROOM3_15",
    desc=text.ROOM3_15_DESC,
    ldesc=text.ROOM3_15_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM3_16"),
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
        "WEST": Exit("WEST", target="ROOM4_20"),
    },
)

ROOM3_18 = Room(
    id="ROOM3_18",
    desc=text.ROOM3_18_DESC,
    ldesc=text.ROOM3_18_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_17"),
        "WEST": Exit("WEST", target="ROOM4_21"),
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
        "WEST": Exit("WEST", target="ROOM4_25"),
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
    desc=text.ROOM4_4_DESC,
    ldesc=text.ROOM4_4_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM4_3"),
    },
)

ROOM4_5 = Room(
    id="ROOM4_5",
    desc=text.ROOM4_5_DESC,
    ldesc=text.ROOM4_5_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM3_6"),
        "EAST": Exit("EAST", target="ROOM4_6"),
    },
)

ROOM4_6 = Room(
    id="ROOM4_6",
    desc=text.ROOM4_6_DESC,
    ldesc=text.ROOM4_6_LDESC,
    exits={
        "WEST": Exit("WEST", target="ROOM4_5"),
        "EAST": Exit("EAST", target="ROOM4_7"),
    },
)

ROOM4_7 = Room(
    id="ROOM4_7",
    desc=text.ROOM4_7_DESC,
    ldesc=text.ROOM4_7_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM4_8"),
        "WEST": Exit("WEST", target="ROOM4_6"),
    },
)

ROOM4_8 = Room(
    id="ROOM4_8",
    desc=text.ROOM4_8_DESC,
    ldesc=text.ROOM4_8_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_7"),
        "WEST": Exit("WEST", target="ROOM3_7"),
        "SOUTH": Exit("SOUTH", target="ROOM4_9")
    },
)

ROOM4_9 = Room(
    id="ROOM4_9",
    desc=text.ROOM4_9_DESC,
    ldesc=text.ROOM4_9_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM4_10"),
        "EAST": Exit("EAST", target="END",
                     condition= FlagCondition("BLOCK_REDBUG"), 
                     blocked_msg=text.REDBUCK_BLOCKED_MSG,
                     blocked_msg_general=text.REDBUCK_BLOCKED_MSG_GENERAL),
        "NORTH": Exit("NORTH", target="ROOM4_8"),
    },
)

ROOM4_10 = Room(
    id="ROOM4_10",
    desc=text.ROOM4_10_DESC,
    ldesc=text.ROOM4_10_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_9"),
        "WEST": Exit("WEST", target="ROOM3_9"),
    },
)

ROOM4_11= Room(
    id="ROOM4_11",
    desc=text.ROOM4_11_DESC,
    ldesc=text.ROOM4_11_LDESC,
    exits={
        "SOUTH": Exit("SOUTH", target="ROOM4_12"),
        "WEST": Exit("WEST", target="ROOM3_10"),
    },
)

ROOM4_12 = Room(
    id="ROOM4_12",
    desc=text.ROOM4_12_DESC,
    ldesc=text.ROOM4_12_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_11"),
        "WEST": Exit("WEST", target="ROOM3_11"),
    },
)

ROOM4_13= Room(
    id="ROOM4_13",
    desc=text.ROOM4_13_DESC,
    ldesc=text.ROOM4_13_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_11"),
        "WEST": Exit("WEST", target="ROOM4_14"),
    },
)

ROOM4_14= Room(
    id="ROOM4_14",
    desc=text.ROOM4_14_DESC,
    ldesc=text.ROOM4_14_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM4_13"),
        "WEST": Exit("WEST", target="ROOM4_15"),
    },
)

ROOM4_15= Room(
    id="ROOM4_15",
    desc=text.ROOM4_15_DESC,
    ldesc=text.ROOM4_15_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM4_14"),
    },
)

ROOM4_16= Room(
    id="ROOM4_16",
    desc=text.ROOM4_16_DESC,
    ldesc=text.ROOM4_16_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM3_14"),
        "WEST": Exit("WEST", target="ROOM4_17"),
    },
)

ROOM4_17= Room(
    id="ROOM4_17",
    desc=text.ROOM4_17_DESC,
    ldesc=text.ROOM4_17_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM4_16"),
        "WEST": Exit("WEST", target="ROOM4_18"),
    },
)

ROOM4_18= Room(
    id="ROOM4_18",
    desc=text.ROOM4_18_DESC,
    ldesc=text.ROOM4_18_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM4_17"),
        "WEST": Exit("WEST", target="ROOM4_19"),
    },
)

ROOM4_19= Room(
    id="ROOM4_19",
    desc=text.ROOM4_19_DESC,
    ldesc=text.ROOM4_19_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM4_18"),
    },
)

ROOM4_20= Room(
    id="ROOM4_20",
    desc=text.ROOM4_20_DESC,
    ldesc=text.ROOM4_20_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_17"),
        "WEST": Exit("WEST", target="END"),
    },
)

ROOM4_21= Room(
    id="ROOM4_21",
    desc=text.ROOM4_21_DESC,
    ldesc=text.ROOM4_21_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_18"),
        "NORTH": Exit("NORTH", target="ROOM4_22"),
    },
)

ROOM4_22= Room(
    id="ROOM4_22",
    desc=text.ROOM4_22_DESC,
    ldesc=text.ROOM4_22_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_23"),
        "SOUTH": Exit("SOUTH", target="ROOM4_21"),
    },
)

ROOM4_23= Room(
    id="ROOM4_23",
    desc=text.ROOM4_23_DESC,
    ldesc=text.ROOM4_23_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_24"),
        "SOUTH": Exit("SOUTH", target="ROOM4_22"),
    },
)

ROOM4_24= Room(
    id="ROOM4_24",
    desc=text.ROOM4_24_DESC,
    ldesc=text.ROOM4_24_LDESC,
    exits={
        "NORTH": Exit("NORTH", target="ROOM4_25"),
        "SOUTH": Exit("SOUTH", target="ROOM4_23"),
    },
)

ROOM4_25= Room(
    id="ROOM4_25",
    desc=text.ROOM4_25_DESC,
    ldesc=text.ROOM4_25_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_22"),
        "SOUTH": Exit("SOUTH", target="ROOM4_24"),
    },
)

ROOM4_26= Room(
    id="ROOM4_26",
    desc=text.ROOM4_26_DESC,
    ldesc=text.ROOM4_26_LDESC,
    exits={
        "EAST": Exit("EAST", target="ROOM3_1"),
    },
    item=ALL_ITEMS["MATCHBOX"]
)

ROOMS: Dict[str, Room] = {
    r.id: r for r in [MIDDLE, END, 
                      ROOM1_1, ROOM1_2, ROOM1_3, ROOM1_4, ROOM1_5, ROOM1_6, ROOM1_7, ROOM1_8, 
                      ROOM2_1, ROOM2_2, ROOM2_3, ROOM2_4, ROOM2_5, ROOM2_6, ROOM2_7, ROOM2_8, ROOM2_9, ROOM2_10, ROOM2_11, ROOM2_12, ROOM2_13, ROOM2_14, ROOM2_15, ROOM2_16, 
                      ROOM3_1, ROOM3_2, ROOM3_3, ROOM3_4, ROOM3_5, ROOM3_6, ROOM3_7, ROOM3_8, ROOM3_9, ROOM3_10, ROOM3_11, ROOM3_12, ROOM3_13, ROOM3_14, ROOM3_15, ROOM3_16, ROOM3_17, ROOM3_18, ROOM3_19, ROOM3_20, ROOM3_21, ROOM3_22, 
                      ROOM4_1, ROOM4_2, ROOM4_3, ROOM4_4, ROOM4_5, ROOM4_6, ROOM4_7, ROOM4_8, ROOM4_9, ROOM4_10, ROOM4_11, ROOM4_12, ROOM4_13, ROOM4_14, ROOM4_15, ROOM4_16, ROOM4_17, ROOM4_18, ROOM4_19, ROOM4_20, ROOM4_21, ROOM4_22, ROOM4_23, ROOM4_24, ROOM4_25, ROOM4_26 ]
}