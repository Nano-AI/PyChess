from Engine.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'p'
        self.start_move = True

    def is_valid_move(self, x, y):
        print(f"---\nCurrent values: ({self.x}, {self.y})\nGoing to: ({x}, {y})")
        if y - self.y < 0:
            return False
        if not self.start_move and y - self.y == 1:
            return False
        return True
