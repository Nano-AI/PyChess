from Engine.Pieces.Bishop import *
from Engine.Pieces.Rook import *


class Queen(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'q'

    def is_valid_move(self, x, y):
        self.get_guarding_spots()
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if self.x != x and self.y != y and abs((y - self.y) / (x - self.x)) != 1:
            return False, "Illegal move"

        if self.x != x and self.y != y and abs((y - self.y) / (x - self.x)) == 1:
            valid, reason = Bishop(self.board, self.side, self.x, self.y).is_valid_move(x, y)
            if not valid:
                return valid, reason

        if self.x == x or self.y == y:
            valid, reason = Rook(self.board, self.side, self.x, self.y).is_valid_move(x, y)
            if not valid:
                return valid, reason

        return True, "Success"

    def get_guarding_spots(self):
        return None
