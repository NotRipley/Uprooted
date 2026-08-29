import pytest
from tests.fixtures import clearing, ruined_clearing
from utils.board import IllegalActionError

def test_add_building(clearing):
    clearing.add_building("marquise", "sawmill")
    assert ("marquise", "sawmill") in clearing.buildings
    assert clearing.free_slots == 1

def test_fill_all_slots(clearing):
    clearing.add_building("marquise", "sawmill")
    clearing.add_building("marquise", "workshop")
    assert clearing.free_slots == 0

def test_build_in_full_clearing_raises(clearing):
    clearing.add_building("marquise", "sawmill")
    clearing.add_building("marquise", "workshop")
    with pytest.raises(IllegalActionError):
        clearing.add_building("eyrie", "roost")

def test_ruin_occupies_slot(ruined_clearing):
    assert ruined_clearing.free_slots == 1
    ruined_clearing.add_building("eyrie", "roost")
    with pytest.raises(IllegalActionError):
        ruined_clearing.add_building("marquise", "sawmill")

def test_remove_building(clearing):
    clearing.add_building("marquise", "sawmill")
    clearing.remove_building("marquise", "sawmill")
    assert clearing.buildings == []
    assert clearing.free_slots == 2

def test_remove_absent_building_raises(clearing):
    with pytest.raises(IllegalActionError):
        clearing.remove_building("marquise", "sawmill")

def test_remove_building_only_removes_one_copy(clearing):
    clearing.add_building("eyrie", "roost")   # hypothetical double, e.g. 3-slot later
    clearing.add_building("eyrie", "roost")
    clearing.remove_building("eyrie", "roost")
    assert clearing.buildings.count(("eyrie", "roost")) == 1