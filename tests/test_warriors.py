import pytest
from utils.board import Clearing, IllegalActionError

@pytest.fixture
def clearing():
    """A plain 2-slot fox clearing."""
    return Clearing(cid=1, suit="fox", slots=2)

def test_add_warriors(clearing):
    clearing.change_warriors("marquise", 3)
    assert clearing.warriors["marquise"] == 3

def test_remove_warriors(clearing):
    clearing.change_warriors("marquise", 3)
    clearing.change_warriors("marquise", -2)
    assert clearing.warriors["marquise"] == 1

def test_remove_too_many_warriors_raises(clearing):
    clearing.change_warriors("marquise", 2)
    with pytest.raises(IllegalActionError):
        clearing.change_warriors("marquise", -3)

def test_remove_warriors_from_empty_clearing_raises(clearing):
    with pytest.raises(IllegalActionError):
        clearing.change_warriors("eyrie", -1)

def test_warriors_reach_zero_cleans_up(clearing):
    clearing.change_warriors("marquise", 2)
    clearing.change_warriors("marquise", -2)
    assert "marquise" not in clearing.warriors   # no ghost zero-entries

def test_multiple_factions_tracked_independently(clearing):
    clearing.change_warriors("marquise", 2)
    clearing.change_warriors("eyrie", 4)
    assert clearing.warriors == {"marquise": 2, "eyrie": 4}