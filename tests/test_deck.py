import pytest
from src.errors import IllegalActionError # obvs need to add that it

def draw_without_reshuffle(full_deck):
    n_cards = len(full_deck.draw_pile)
    full_deck.draw(10)
    assert(len(full_deck.discard_pile) == 10)
    assert(len(full_deck.draw_pile) == n_cards - 10)


def test_draw_with_reshuffle(one_left_deck):
    first_card = one_left_deck.draw_pile[0]
    pass

def test_bad_input_raises():
    pass

def test_print_nicely():
    pass


