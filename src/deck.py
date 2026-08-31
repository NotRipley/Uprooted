"""
We model the deck as a list of cards.
Each card has a suit, cost, vp reward, item reward and description.
"""
import json
from errors import InvalidCardError

# --- classes ---
class Card:
    def __init__(self, suit, cost, vp, item, desc):
        """
        Assign parameter values to Card instance.
        :param suit: "mouse"/"rabbit"/"fox"/"bird" | str
        :param cost: format (number_suit) e.g. "2_fox" | str
        :param vp: number of victory points | int
        :param item: "boot"/"bag"/"crossbow"/"hammer"/"sword"/"tea"/"coin" | str
        :param desc: text on the card | str
        """
        # bouncer checks for stupid inputs
        self.bouncer(suit, cost, vp, item, desc)

        # if past the bouncer we make the card
        self.suit = suit
        self.cost = cost
        self.vp = vp
        self.item = item
        self.desc = desc
        # idx -1 to represent not set yet
        ## What do you mean by the comment above?
        self.idx = -1 

    def bouncer(self, suit, cost, vp, item, desc):
        """Input validation."""
        #Check suit is valid
        suits = ["bird", "fox", "mouse", "rabbit"]
        if suit not in suits:
            raise InvalidCardError(f"Expected suit to be {", ".join(suits)} but got {suit}")
            
        if not (
            isinstance(suit, str) and
            isinstance(cost, str) and
            isinstance(vp, int) and
            isinstance(item, str) and
            isinstance(desc, str)
        ):
            raise TypeError(
                f"Expected (str, str, int, str, str), got"
                f"({type(suit)}, {type(cost)}, {type(vp)}, {type(item)}, {type(desc)}."
            )

class Deck:
    def __init__(self, cards_list):
        self.cards = cards_list
        self.bouncer()

    def load(self, filepath):
        "Load the deck from a json object"
        pass
    
    def draw(self, n):
        "Draw n cards from the deck. Remove the cards drawn from the deck and return them (to be added to hand etc.)"
        pass

    def bouncer(self):
        """Check the cards have been inherited correctly."""
        pass



# --- unbound functions ---

def deck_reader(deck_filepath): # This should be sm like Deck.load(filepath) to initialise the deck
    """
    Read in deck JSON and return a Deck object with its cards.
    :param deck_filepath: filepath of a .json file containing the information for an entire deck of cards.
    :return: a Deck object.
    """
    # --- open json and read out inputs ---
    with open(deck_filepath, "r") as f:
        deck_config = json.load(f)

    # --- validate json ---

    # --- make list of card objects ---
    cards_list = []
    cards_config = deck_config["cards"]
    for i, card in enumerate(cards_config):
        item = Card(**card)
        item.idx = i # what is this idx for? doesn't seem to be used anywhere?
        cards_list.append(item)

    # --- give list to Deck instance ---
    return Deck(cards_list)

