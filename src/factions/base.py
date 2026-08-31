from enum import Enum 

class FactionID(Enum):
    MARQUISE = "marquise"
    EYRIE = "eyrie"
    HAMSTER = "hamster"  

    @property
    def win_ties(self):
        return self in (FactionID.EYRIE,)

class Faction():
    id: FactionID
    win_ties = False
    warrior_cap = 10

    def __init__(self):
        self.warrior_supply = self.warrior_cap.
        self.hand = []
        self.vp = 0