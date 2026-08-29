import pytest
from tests.fixtures import board
from utils.board import IllegalActionError

def test_move_warriors_to_adjacent_clearing(board):
    board.clearings[1].change_warriors("marquise", 3)
    board.move_warriors("marquise", 1, 2, 2)
    assert board.clearings[1].warriors["marquise"] == 1
    assert board.clearings[2].warriors["marquise"] == 2

def test_move_warriors_to_non_adjacent_clearing(board):
    board.clearings[2].change_warriors("marquise", 3)
    with pytest.raises(IllegalActionError):
        board.move_warriors("marquise", 2, 3, 2)
    assert board.clearings[2].warriors["marquise"] == 3

def test_move_warriors_with_river(board):
    board.clearings[2].change_warriors("riverfolk", 3)
    with pytest.raises(IllegalActionError):
        board.move_warriors("riverfolk", 2, 3, 2) # not connected by land
    board.move_warriors("riverfolk", 2, 3, 2, edge_type="river") # connected by river
    assert board.clearings[2].warriors["riverfolk"] == 1
    assert board.clearings[3].warriors["riverfolk"] == 2
