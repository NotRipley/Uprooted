from utils.board import Board

def setup_board(board_filepath, summary=False):
    board = Board(board_filepath)

    # --- human-summary ---
    if summary:
        for c in board.clearings.values():
            tags = []

            if c.corner:
                tags.append("corner")
            if c.ruins:
                tags.append(f"{c.ruins} ruin(s)")
            
            tags_str = f"[{', '.join(tags)}]" if tags else ""

            print(f"{c.id}: {c.suit} slots={c.building_slots} {tags_str} neighbours={board.neighbours(c.id)}")
        print(f"{len(board.paths)} paths, {len(board.rivers)} rivers")
    # --- check everything setup ---
    assert len(board.clearings) == 12, f"expected 12 clearings got {len(board.clearings)}"
    
    suits = [c.suit for c in board.clearings.values()]
    for suit in ("fox", "mouse", "rabbit"):
        assert suits.count(suit) == 4, f"expected 4 {suit} clearings got {len(suit.count(suit))}"

    corners = [c for c in board.clearings.values() if c.corner]
    assert len(corners) == 4, f"expected 4 corners got {len(corners)}"

    for (a, b) in board.paths | board.rivers:
        assert a in board.clearings and b in board.clearings, f"edge ({a},{b}) references unknown clearing"
        assert a != b, f"self-loop on {a}"
    
    for c in board.clearings:
        assert board.neighbours(c), f"clearing {c} is isolated"
    

    print("All checks passed")
    return board

if __name__ == "__main__":
    setup_board("input_data/Autumn_board.json", summary=True)