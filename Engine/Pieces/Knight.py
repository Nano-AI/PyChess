from Engine.Pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'h'
        self.start_move = True

    def is_valid_move(self, x, y):
        slope = (y - self.y) / (x - self.x)
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if abs(slope) != 2 and abs(slope) != 0.5:
            return False, "Not valid move"
        return True, "Success"
