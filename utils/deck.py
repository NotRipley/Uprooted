"""
We model the deck as a list of cards.
Each card has a suit, cost, VP reward, item reward and description.
"""
import json

# --- classes ---
class Card:
    def __init__(self, suit, cost, VP, item, desc):
        """
        Assign parameter values to Card instance.
        :param suit: "mouse"/"rabbit"/"fox"/"bird" | str
        :param cost: format (number_suit) e.g. "2_fox" | str
        :param VP: number of victory points | int
        :param item: "boot"/"bag"/"crossbow"/"hammer"/"sword"/"tea"/"coin" | str
        :param desc: text on the card | str
        """
        # bouncer checks for stupid inputs
        self.bouncer(suit, cost, VP, item, desc)

        # if past the bouncer we make the card
        self.suit = suit
        self.cost = cost
        self.VP = VP
        self.item = item
        self.desc = desc

    def bouncer(self, suit, cost, VP, item, desc):
        """Input validation."""
        suits = ["bird", "fox", "mouse", "rabbit"]
        if suit not in suits:
            raise InvalidCardError(f"Expected suit to be {", ".join(suits)} but got {suit}")
            
        if not (
            isinstance(suit, str) and
            isinstance(cost, str) and
            isinstance(VP, int) and
            isinstance(item, str) and
            isinstance(desc, str)
        ):
            raise TypeError(
                f"Expected (str, str, int, str, str), got"
                f"({type(suit)}, {type(cost)}, {type(VP)}, {type(item)}, {type(desc)}."
            )

class Deck:
    def __init__(self, cards):
        self.cards = cards



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
    card_list = []
    for suit in deck_config["cards"]:
        for cost_suit in deck_config["cards"][suit]:
            for card_config in deck_config["cards"][suit][cost_suit]:
                card = Card(card_config["cost_quant"], card_config["vp"], card_config["item"], card_config["desc"])
                card_list.append(card)

    # --- give list to Deck instance ---
    return Deck(card_list)

def InvalidCardError(Exception):
    "Raise error if the card is not valid"
    pass