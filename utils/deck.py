"""
We model the deck as a list of cards.
Each card has a suit, cost, vp reward, item reward and description.
"""
import json

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

    def bouncer(self, suit, cost, vp, item, desc):
        """Input validation."""
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

    def bouncer(self):
        """Check the cards have been inherited correctly."""
        pass



# --- unbound functions ---

def deck_reader(deck_filepath):
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
    for card in cards_config:
        cards_list.append(Card(**card))

    # --- give list to Deck instance ---
    return Deck(cards_list)

def InvalidCardError(Exception):
    "Raise error if the card is not valid"
    pass