from Engine.Pieces.Piece import Piece


class Empty(Piece):
    def __init__(self, board, x: int, y: int):
        super().__init__(board, None, x, y)
        self.type = ' '
