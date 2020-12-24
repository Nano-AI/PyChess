from Engine.Pieces.Piece import Piece
from copy import copy


class King(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.checked = False
        self.guarding_spots = []
        self.available_moves = []
        self.type = 'k'
        self.around = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1)]

    def is_valid_move(self, x, y):
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if abs(x - self.x) > 1 or abs(y - self.y) > 1:
            return False, "Moving too far"

        can_go, piece = self.guarded(x, y)

        if can_go:
            return False, f"{piece.type} can go there!"

        return True, "Success"

    def guarded(self, x, y):
        """This function checks if a piece is guarding the spot passed in, if it is, then it's going to return True
        and the piece, other wise it is going to return False and None"""
        guarded = False
        for row in self.board.board:
            for piece in row:
                if piece.type == ' ' or piece.side == self.side:
                    continue

                guarding = piece.get_guarding_spots()

                if guarding is None:
                    guarded, _ = piece.is_valid_move(x, y)
                else:
                    for spot in guarding:
                        if spot == (x, y):
                            guarded = True

                if guarded:
                    return True, piece
        return False, None

    def get_guarding_spots(self):
        spots = []
        spots_around = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for sx, sy in spots_around:
            if 0 <= self.x + sx <= 8 and 0 <= self.y + sy <= 8:  # to make sure that cords don't go out of bounds
                spots.append((self.x + sx, self.y + sy))

        return spots
