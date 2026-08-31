import pytest
from tests.fixtures import clearing
from src.errors import IllegalActionError

def test_add_token(clearing):
    clearing.add_token("marquise", "wood")
    assert clearing.tokens[("marquise", "wood")] == 1

def test_tokens_stack(clearing):
    clearing.add_token("marquise", "wood")
    clearing.add_token("marquise", "wood")
    assert clearing.tokens[("marquise", "wood")] == 2

def test_tokens_do_not_use_building_slots(clearing):
    clearing.add_token("marquise", "wood")
    clearing.add_token("alliance", "sympathy")
    assert clearing.free_slots == 2          # unchanged

def test_remove_token(clearing):
    clearing.add_token("marquise", "wood")
    clearing.remove_token("marquise", "wood")
    assert ("marquise", "wood") not in clearing.tokens   # cleaned up, no zero entry

def test_remove_absent_token_raises(clearing):
    with pytest.raises(IllegalActionError):
        clearing.remove_token("alliance", "sympathy")