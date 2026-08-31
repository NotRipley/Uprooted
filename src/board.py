"""
We will map the board as an adjanency matrix that shows connections between clearings.
Each clearing has a suit, building slots and list of neighbours (which will be useful for fast lookup later)
"""
from collections import defaultdict
import json

from .errors import InvalidMapError, IllegalActionError

class Board:
    """
    This is the board state, each clearing has a suit, and building slots. We can also add troops and buildings.
    """
    def __init__(self, board_filepath, summary=False):
        with open(board_filepath) as f:
            data = json.load(f)
        
        self.clearings ={c["id"]: Clearing(c["id"], c["suit"], c["slots"], c.get("ruins", 0), c.get("corner", False)) for c in data["clearings"]}
        self.paths = {tuple(sorted(e)) for e in data["paths"]}
        self.rivers = {tuple(sorted(e)) for e in data["rivers"]}

        self._validate()
    
    def _validate(self):
        for (a, b) in self.paths | self.rivers:
            if a not in self.clearings or b not in self.clearings:
                raise InvalidMapError(f"edge ({a},{b}) references unknown clearing")
            if a == b:
                raise InvalidMapError(f"self-loop on {a}")
    
        for c in self.clearings:
            if not self.neighbours(c) and not self.neighbours(c, "river"):
                raise InvalidMapError(f"clearing {c} is isolated")

    def adjacent(self, a, b, edge_type="land"):
        edges = self.paths if edge_type == "land" else self.rivers

        return tuple(sorted((a,b))) in edges

    def neighbours(self, cid, edge_type="land"):
        edges = self.paths if edge_type == "land" else self.rivers

        # Get a list of all edges including cid
        connected = [(x,y) for (x,y) in edges if cid in (x,y)]
        # Filter out cid
        neighbouring = [x if y == cid else y for (x, y) in connected]

        return neighbouring

    def move_warriors(self, faction, move_from, move_to, num, edge_type="land"):
        if not self.adjacent(move_from, move_to, edge_type):
            raise IllegalActionError(f"{move_from} and {move_to} are not connected by {edge_type}")
            
        self.clearings[move_from].change_warriors(faction, -num)
        self.clearings[move_to].change_warriors(faction, num)

    def __repr__(self):
        lines = []
        for c in self.clearings.values():
            tags = []

            if c.corner:
                tags.append("corner")
            if c.ruins:
                tags.append(f"{c.ruins} ruin(s)")
                
            tags_str = f"[{', '.join(tags)}]" if tags else ""

            lines.append(f"{c.id}: {c.suit} slots={c.building_slots} {tags_str} neighbours={self.neighbours(c.id)}")
        lines.append(f"{len(self.paths)} paths, {len(self.rivers)} rivers")
        return "\n".join(lines)

class Clearing:
    def __init__(self, cid, suit, slots, ruins=0, corner=False):
        self.id = cid
        self.suit = suit

        self.building_slots = slots
        self.ruins = ruins
        self.corner = corner

        self.buildings = [] #[(faction, building_type)]
        self.tokens = defaultdict(int) #{(faction, token_type): count}
        self.warriors = defaultdict(int) #{faction: count}
    
    @property
    def free_slots(self):
        return self.building_slots - self.ruins - len(self.buildings)

    def add_building(self, faction, building_type):
        if self.free_slots <= 0:
            raise IllegalActionError(f"No free slots in clearing {self.id}")
        
        self.buildings.append((faction, building_type))

    def remove_building(self, faction, building_type):
        key = (faction, building_type)
        if key not in self.buildings:
            raise IllegalActionError(f"No {building_type} of {faction} in clearing {self.id}")

        self.buildings.remove(key)

    def add_token(self, faction, token_type):
        self.tokens[(faction, token_type)] += 1

    def remove_token(self, faction, token_type):
        key = (faction, token_type)
        if self.tokens.get(key, 0) <= 0:
            raise IllegalActionError(f"No {token_type} of {faction} in clearing {self.id}")

        self.tokens[key] -= 1
        if self.tokens[key] == 0:
            del self.tokens[key]
    
    def change_warriors(self, faction, num):
        if self.warriors.get(faction, 0) + num < 0:
            raise IllegalActionError(f"Not enough {faction} warriors in {self.id}")
        
        self.warriors[faction] += num

        if self.warriors[faction] == 0:
            del self.warriors[faction]
        
    def current_ruler(self):
        strength = defaultdict(int)

        for faction, count in self.warriors.items():
            strength[faction] += count

        for faction, _building_type in self.buildings:
            strength[faction] += 1

        if not strength:
            return None                     # empty clearing: no ruler

        best = max(strength.values())
        leaders = [f for f, s in strength.items() if s == best]

        if len(leaders) == 1:
            return leaders[0]
        for leader in leaders:
            if leader.win_ties: # if the faction has the win_ties ability
                return leader
        return None # tied so nobody rules

    