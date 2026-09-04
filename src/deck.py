"""
We model the deck as a list of cards.
Each card has a suit, cost, vp reward, item reward and description.
"""
import json
import numpy as np
from src.errors import InvalidCardError
import random

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
        # --- input validation ---
        self.check(suit, cost, vp, item, desc)

        # --- attributes ---
        self.suit = suit
        self.cost = cost
        self.vp = vp
        self.item = item
        self.desc = desc

    def __repr__(self): # Very good
        """Print cards nicely"""
        return (
            f"\n __________________ \n"
            f"{self.suit} card \n"
            f" costing {self.cost} \n"
            f" worth {self.vp} \n"
            f" gives {self.item} \n"
            f" {self.desc} \n"
            f"__________________ \n")


    def check(self, suit, cost, vp, item, desc):
        """Input validation."""
        # --- suit ---
        suits = ["bird", "fox", "mouse", "rabbit"]
        if suit not in suits:
            raise InvalidCardError(f"Expected suit to be {", ".join(suits)} but got {suit}")
        # --- cost ---
        



class Deck:
    def __init__(self, filepath):
        self.load(filepath)
        self.bouncer()

    def load(self, filepath):
        "Load the deck from a json object"
        # --- open json and read out inputs ---
        with open(filepath, "r") as f:
            deck_config = json.load(f)

        # --- validate json ---

        # --- make list of card objects ---
        cards_list = []
        cards_config = deck_config["cards"]
        for i, card in enumerate(cards_config): # What is the purpose of i?
            item = Card(**card)
            cards_list.append(item)

        # --- attach card list ---
        self.cards = cards_list # what is self.cards for?
        self.draw_pile = self.cards 
        self.discard_pile = []

    
    def draw(self, n):
        """Draw n cards from the deck. Remove the cards drawn from the deck and return them (to be added to hand etc.)
        Acts kind of like a highlight so to discard cards we can draw them and then place them."""
        # --- check enough cards to draw and if not, reshuffle ---
        # a point here: it should draw as many as it can, then reshuffle when it hits zero
        if n > len(self.draw_pile):
            # --- draw down to empty, store, reshuffle ---
            extra = self.draw_pile
            n -= len(self.draw_pile) # suggest you use extra instead of self.draw_pile here
            print("not enough cards to draw => reshuffling \n") # try and include a flag for print statements,
            # when running things you want to stay away from verbose output as the default because it pollutes your terminal
            # and adds a lot of unnecessary text
            self.reshuffle()
        else:
            extra = []
        # --- draw, remove and return ---
        cards_to_draw = random.sample(self.draw_pile, n)
        cards_to_draw.extend(extra)
        self.draw_pile.remove(cards_to_draw)
        return cards_to_draw



    def reshuffle(self):
        """move discard pile to draw pile"""
        self.draw_pile.extend(self.discard_pile)
        self.discard_pile = []

    def bouncer(self):
        """Check the cards have been inherited correctly."""
        # This should be checks like: deck has at least 1 card etc.
        pass



# --- unbound functions ---





