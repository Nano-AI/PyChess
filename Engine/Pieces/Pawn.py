from Engine.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'p'
        self.start_move = True

    def is_valid_move(self, x, y):
        if y - self.y < 0 and self.side == 'w':  # Checks if move is backwards or same spot
            return False, "Moving backwards or going in the same spot"
        if y - self.y > 0 and self.side == 'b':
            return False, "Moving backwards or going in same spot"
        if y - self.y >= 3:  # Checks if move is over 2 boxes up
            return False, "Moving more than 2 boxes up"
        if not self.start_move and y - self.y >= 2:  # Checks if the move is above 2 boxes if the start move is false
            return False, "Not start move and moving 2 boxes up"
        if self.x == x and self.board.get_logical_spot(x, y).type != ' ':  # Checks if move will crash
            return False, "Move will crash into another piece"             # into another piece
        if self.x != x and self.y == y:  # Stops pawn from moving directly right and left
            print(self.x, self.y, x, y)
            return False, "Pawn is moving directly left or right"
        if self.x - x > 1 or self.x - x < -1:
            if self.y == y:
                return False, "Moving more than 1 spot diagonally"
        if self.x - x == 1 or self.x - x == -1:
            if y - self.y > 1:
                return False, "Forgot what this does"
            if self.board.get_logical_spot(x, y).type == ' ':
                return False, "Trying to capture an empty spot"
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Trying to capture your own piece"
        self.start_move = False
        return True, "Success"


"""
Things to fix:
Pawn can go directly right and left - Fixed I think
Pawn can move diagonally without capturing a piece - Fixed I think
"""
