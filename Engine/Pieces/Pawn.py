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
        if self.board.get_logical_spot(x, y).type == ' ' and x != self.x:
            return False, "Moving to narnia"
        if abs(self.x - x) > 1 or abs(self.y - y) > 2:
            return False, "Moving to narnia"
        if abs(self.y - y) > 1 and not self.start_move:
            return False, "Moving to narnia"

        if abs(self.y - y) > 1 and abs(self.x - x) > 0:
            return False, "Moving to narnia"

        ud = 1 if self.side == 'w' else -1
        if abs(y - self.y) == 2 and self.board.get_logical_spot(self.x, self.y + ud).type != ' ':
            return False, "Trying to move 2 spaces up when there's a pieces above it."
        return True, "Success"

    def get_guarding_spots(self):
        spots = []
        y = 1 if self.side == 'w' else -1

        if 0 <= self.y + y <= 8:
            if 0 <= self.x + 1 <= 8:
                spots.append((self.x + 1, self.y + y))

            if 0 <= self.x - 1 <= 8:
                spots.append((self.x - 1, self.y + y))

        return spots
