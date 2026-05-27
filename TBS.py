from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Set


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
    blocked_msg: Optional[str] = None

    def allowed(self, state: "GameState") -> bool:
        return self.condition.check(state) if self.condition else True
    
@dataclass
class Item:
    flag_name: str          # z.B. "ITEM_KEY"
    name: str               # "Key"
    item_desc: str          # Text beim Finden
    item_reaktion: str      # Text beim Geben
    used_flag: Optional[str] = None  # z.B. "KEY_USED"
    solves: list[str] = field(default_factory=list)
    
    def display_name(self) -> str:
        return self.name

@dataclass
class Room:
    id: str
    desc: str
    ldesc: Optional[str] = None
    exits: Dict[str, Exit] = field(default_factory=dict)
    action: Optional[Callable[["GameState", "Room", str], None]] = None
    flags: Set[str] = field(default_factory=set)
    item: Optional[Item] = None
    # item_flag: Optional[str] = None
    # item_text: Optional[str] = None
    # used_flag: Optional[str] = None

    def describe(self) -> str:
        return self.desc
    
    def look(self) -> Optional[str]:
       return self.ldesc

    def try_move(self, state: "GameState", direction: str) -> Optional[str]:
        ex = self.exits.get(direction.upper())
        if not ex:
            return None

        #condition (e.g. IF WON-FLAG / IF KITCHEN-WINDOW IS OPEN)
        if not ex.allowed(state):
            return None
        
        return ex.target
    
    def find_item(self, state: "GameState") -> Optional[str]:
        # Hat dieser Raum überhaupt ein Item?
        if not self.item:
            return None
        
        item = self.item

        # Wurde das Item bereits verbraucht / abgegeben?
        if item.used_flag and item.used_flag in state.flags:
            return None

        # Hat der Spieler das Item schon?
        if item.flag_name in state.flags:
            return None

        # Item wird jetzt gefunden
        state.flags.add(item.flag_name)
        return item.item_desc
    

    def exit_blocked_message(self, state: "GameState") -> Optional[str]:
        blocked_exits = ""

        for exit in self.exits.values():
            if not exit.allowed(state) and exit.blocked_msg:
                blocked_exits += f"{exit.blocked_msg}\n"

        return blocked_exits if blocked_exits else None
    
    def exit_blocked_flag(self, state: "GameState") -> Optional[str]:
        blocker_flag = ""
        for ex in self.exits.values():
            if (not ex.allowed(state)) and ex.blocked_msg:
                if isinstance(ex.condition, FlagCondition):
                    blocker_flag = ex.condition.flag
        return blocker_flag if blocker_flag else None


    @staticmethod
    def end_action(state: "GameState", room: "Room", cmd: str) -> None:
        state.flags.add("WON-FLAG")
        state.game_over = True
      
@dataclass
class GameState:
    flags: Set[str] = field(default_factory=set)
    game_over: bool = False 