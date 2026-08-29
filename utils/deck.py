"""
We model the deck as a list of cards.
Each card has a suit, cost, VP reward, item reward and description.
"""
def InvalidCardError(Exception):
    "Raise error if the card is not valid"
    pass
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

def cards_from_json(card_json):
    """
    :param card_json: a .json file containing the information for an entire deck of cards.
    :return: a list of Card objects.
    """
    pass