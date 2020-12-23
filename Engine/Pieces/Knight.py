from Engine.Pieces.Piece import Piece


class Knight(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'h'

    def is_valid_move(self, x, y):
        dy = y - self.y
        dx = x - self.x
        try:
            slope = (y - self.y) / (x - self.x)
        except ZeroDivisionError:
            return False, "Vertical movement"
        except Exception as e:
            raise e
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if abs(dy) > 2 or abs(dx) > 2:
            return False, "The move was too far"
        if abs(slope) != 2 and abs(slope) != 0.5:
            return False, "Not valid move"
        return True, "Success"

    def get_guarding_spots(self):
        spots = []

        for x in range(0, len(self.board.board)):
            spots.append([])
            for y in range(0, len(self.board.board[x])):
                spots[x].append(0)

        """
        . . . . . . .
        . . x . x . .
        . x . . . x .
        . . . k . . .
        . x . . . x .
        . . x . x . .
        . . . . . . .
        """

        move_spots = [(1, 2), (-1, 2), (1, -2), (-1, -2)]
        x, y = self.y, self.x
        for sx, sy in move_spots:
            spots[x + sx][y + sy] = 1
            spots[x + sy][y + sx] = 1

        # print('-----------')
        # for arr in [ele for ele in reversed(spots)]:
        #     print(arr)

        return [ele for ele in reversed(spots)]

