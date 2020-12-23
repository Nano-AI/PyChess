from Engine.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'r'
        self.start_move = True

    def is_valid_move(self, x, y):
        if self.side == self.board.get_logical_spot(x, y).side:
            return False, "Trying to capture own piece."

        if x == self.x and y == self.y:
            return False, "Trying to move diagonally"

        if x == self.x:  # Moving up/down
            dy = 1 if self.y < y else -1
            i = self.y + dy
            while i != y:
                if self.board.get_logical_spot(self.x, i).type != ' ':
                    return False, "Object blocking way"
                i += dy

        elif y == self.y:  # Moving right/left
            dx = 1 if self.x < x else -1
            i = self.x + dx
            while i != x:
                if self.board.get_logical_spot(i, self.y).type != ' ':
                    return False, "Object blocking way"
                i += dx

        else:
            return False, "Moving dumb way"

        return True, "Success"

    def get_guarding_spots(self):
        return None
