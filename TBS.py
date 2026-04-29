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