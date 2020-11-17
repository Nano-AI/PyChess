from Engine.Pieces.Piece import Piece


class Queen(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'q'

    def is_valid_move(self, x, y):
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if self.x != x and self.y != y and abs((y - self.y) / (x - self.x)) != 1:
            return False, "Illegal move"

        if self.x != x and self.y != y and abs((y - self.y) / (x - self.x)) == 1:
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

        else:
            if x == self.x:  # Moving up/down
                dy = 1 if self.y < y else -1
                i = self.y + dy
                while i != y:
                    print(i)
                    if self.board.get_logical_spot(self.x, i).type != ' ':
                        return False, "Object blocking way"
                    i += dy

            elif y == self.y:  # Moving right/left
                dx = 1 if self.x < x else -1
                print(dx)
                i = self.x + dx
                print(i)
                while i != x:
                    print(i)
                    if self.board.get_logical_spot(i, self.y).type != ' ':
                        return False, "Object blocking way"
                    i += dx

            else:
                return False, "Moving dumb way"

            return True, "Success"

        return True, "Success"
