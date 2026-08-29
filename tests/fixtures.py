import pytest
from utils.board import Board, Clearing, IllegalActionError

@pytest.fixture
def clearing():
    """A plain 2-slot fox clearing."""
    return Clearing(cid=1, suit="fox", slots=2)

@pytest.fixture
def ruined_clearing():
    """2 slots but 1 taken by a ruin -> only 1 free."""
    return Clearing(cid=2, suit="mouse", slots=2, ruins=1)


@pytest.fixture
def board(tmp_path):
    import json
    data = {
        "map": "test",
        "clearings": [
            {"id": 1, "suit": "fox", "slots": 1},
            {"id": 2, "suit": "mouse", "slots": 1},
            {"id": 3, "suit": "rabbit", "slots": 1},
        ],
        "paths": [[1, 2], [1,3]],
        "rivers": [[2, 3]],
    }
    p = tmp_path / "test_map.json"
    p.write_text(json.dumps(data))
    return Board(str(p))