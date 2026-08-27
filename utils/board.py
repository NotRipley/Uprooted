"""
We will map the board as an adjanency matrix that shows connections between clearings.
Each clearing has a suit, building slots and list of neighbours (which will be useful for fast lookup later)
"""
from collections import defaultdict
import json

class IllegalActionError(Exception):
    "Error class so it's easy to debug an illegal action"
    pass

class Board:
    """
    This is the board state, each clearing has a suit, and building slots. We can also add troops and buildings.
    """
    def __init__(self, board_filepath):
        with open(board_filepath) as f:
            data = json.load(f)
        
        self.clearings ={c["id"]: Clearing(c["id"], c["suit"], c["slots"], c.get("ruins", 0), c.get("corner", False)) for c in data["clearings"]}
        self.paths = {tuple(sorted(e)) for e in data["paths"]}
        self.rivers = {tuple(sorted(e)) for e in data["rivers"]}
    
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
            raise IllegalActionError(f"{src} and {dst} are not connected by {edge_type}")
            
        self.clearings[move_from].change_warriors(faction, -num)
        self.clearings[move_to].change_warriors(faction, num)


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
    
    def change_warriors(self, faction, num):
        if self.warriors[faction] + num < 0:
            raise IllegalActionError(f"Not enough {faction} warriors in {self.id}")
        
        self.warriors[faction] += num

        if self.warriors[faction] == 0:
            del self.warriors[faction]