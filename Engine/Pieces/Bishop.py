from Engine.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'b'
        self.start_move = True

    def is_valid_move(self, x, y):
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if x - self.x == 0:
            return False, "Moving vertically"
        if y - self.y == 0:
            return False, "Moving horizontally"
        if abs((y - self.y) / (x - self.x)) != 1:  # Getting slope of movement
            return False, "Not moving diagonally"

        dy = (y - self.y)
        dx = (x - self.x)

        ud = 1 if dy > 0 else -1
        rl = 1 if dx > 0 else -1

        if dy > 0:  # Moving up
            for i in range(1, abs(dx)):
                if self.board.get_logical_spot(self.x + (i * rl), self.y + i).type != ' ':
                    return False, "Object blocking path"

        if dy < 0:  # Moving down
            for i in range(1, abs(dy)):
                if self.board.get_logical_spot(self.x + i, self.y + (i * ud)).type != ' ':
                    return False, "Object blocking path"

        return True, "Success"
