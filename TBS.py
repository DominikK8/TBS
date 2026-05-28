from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Dict, Optional, Set, Union, Tuple

# Basisklasse mit Verweis auf spätere Definition
class Condition:
    def check(self, state: "GameState") -> bool:
        raise NotImplementedError
# Erweiterung Condition für Exits
@dataclass(frozen=True)
class FlagCondition(Condition):
    flag: str
    # Prüfung, ob FlagCondition in GameState
    def check(self, state: "GameState") -> bool:
        return self.flag in state.flags
# Exit
@dataclass
class Exit:
    # Richtungen
    direction: str
    # Ziel -> Wohin führt die Richtung
    target: Optional[str] = None
    # Welche Bedingungen gibt es, dass man die Richtung gehen kann (Welche Flagge muss im GameState vorhanden sein?)
    condition: Optional[Condition] = None
    # Spezifische und allgemeine Block Nachrichten
    blocked_msg: Optional[str] = None
    blocked_msg_general: Optional[str] = None
    # condition check wird als methode der Klasse aufgerufen
    def allowed(self, state: "GameState") -> bool:
        return self.condition.check(state) if self.condition else True
# Items    
@dataclass
class Item:
    # Interner Name der Flagge
    flag_name: str
    # Ausgabename
    name: str
    # Beschreibung beim finden
    item_desc: str
    # Reaktion bei Abgabe
    item_reaktion: str
    # zusätzlich Flagge markiert diese als benutzt, sie kann dann nicht wiederverwendet werden
    used_flag: Optional[str] = None
    # Flaggen bzw. Conditions, die durch das Item gelöst werden
    solves: list[str] = field(default_factory=list)
    
    def display_name(self) -> str:
        return self.name
# Hauptklasse Räume
@dataclass
class Room:
    # Interne ID
    id: str
    # Ausgabename
    desc: str
    # Beschreibung
    ldesc: Optional[str] = None
    # Mögliche Ausgänge
    exits: Dict[str, Exit] = field(default_factory=dict)
    # Mögliche Aktionen
    action: Optional[Callable[["GameState", "Room", str], None]] = None
    # Flaggen die der Raum auslöst (in GameStat schreibt)
    flags: Set[str] = field(default_factory=set)
    # Items im Raum
    item: Optional[Item] = None

    def describe(self) -> str:
        return self.desc
    
    def look(self) -> Optional[str]:
       return self.ldesc
    # Hauptmethode Bewegung
    def try_move(self, state: "GameState", direction: str) -> Tuple[Union[str, Exit, None], str]:
        ex = self.exits.get(direction.upper())
        # Ist kein Exit definiert -> Wand
        if not ex:
            return None, "NO_EXIT"
        # Ist der Exit definiert aber hat eine FlagCondition
        if not ex.allowed(state):
            return ex, "BLOCKED"
        # Exit vorhanden und passierbar
        return ex.target, "OK"
    # Item finden
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
    
    # Ausgabe der Blockade Message, falls vorhanden
    def exit_blocked_message(self, state: "GameState") -> Optional[str]:
        blocked_exits_msg = ""
        # Falls mehrere Blockaden vorhanden wird Liste erstellt (für evtl. Erweiterungen)
        for exit in self.exits.values():
            if not exit.allowed(state) and exit.blocked_msg:
                blocked_exits_msg += f"{exit.blocked_msg}\n"

        return blocked_exits_msg if blocked_exits_msg else None
    
    # Auslesen der Flaggen eines Exits, ebenfalls als Liste für spätere Erweiterungen
    def exit_blocked_flag(self, state: "GameState") -> Optional[str]:
        blocker_flag = ""
        for ex in self.exits.values():
            if (not ex.allowed(state)) and ex.blocked_msg:
                if isinstance(ex.condition, FlagCondition):
                    blocker_flag = ex.condition.flag
        return blocker_flag if blocker_flag else None
    
    # setzen der Spielende Kriterien (zur Zeit, wenn ein END Raum betreten wird)
    @staticmethod
    def end_action(state: "GameState", room: "Room", cmd: str) -> None:
        state.flags.add("WON-FLAG")
        state.game_over = True

# Beinhaltet alle Flaggen und den Game_Over boolean      
@dataclass
class GameState:
    flags: Set[str] = field(default_factory=set)
    game_over: bool = False 