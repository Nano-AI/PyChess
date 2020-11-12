from Engine.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'r'
        self.start_move = True

    def is_valid_move(self, x, y):
        if x - self.x != 0 and y - self.y != 0:
            return False
        if x != 0:
            if x - self.x < 0:
                for i in range(x, x - self.x):
                    print(self.board.get_logical_spot(i, self.y).type)
            elif x - self.x > 0:
                pass
            else:
                raise Exception(f"I don't know how, but x is something other than 0. Value: {x}")
        elif y != 0:
            for x in range(x):
                pass
