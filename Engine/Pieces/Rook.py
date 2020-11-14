from Engine.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'r'
        self.start_move = True

    def is_valid_move(self, x, y):
        if x != self.x and y != self.y:  # If the user is going horizontally and vertically
            return False, "You can't move vertically and horizontally at the same time!"

        if self.board.get_logical_spot(x, y).side == self.side:  # Stops from capturing your own piece
            return False, "Capturing own piece"
        if x == self.x and y == self.y:
            return False, "Staying still"
        if x != self.x:  # Moving horizontally
            if x - self.x > 0:  # Moving right
                for i in range(self.x + 1, x):
                    if self.board.board[y][i].type != ' ':
                        return False, f"{self.board.board[y][i].type} at position ({x}, {y}) in the way of the rook " \
                                      f"while going right."
            if x - self.x < 0:  # Moving left
                for i in range(x - self.x):
                    if self.board.board[y][x - i].type != ' ':
                        return False, f"{self.board.board[y][x - i].type} at position ({x}, {y}) in the way of the rook " \
                                      f"while going left."

        elif y != self.y:  # Moving vertically
            # print(y, self.y)
            if y - self.y > 0:  # Moving up
                for i in range(self.y, y - 1):
                    print(self.board.board[i][y].type)
                    if self.board.board[i][y].type != ' ':
                        return False, "Something in the way of the rook while going up."
            if y - self.y < 0:  # Moving down
                for i in range(y, self.y):
                    print(self.board.board[i][y].type)
                    if self.board.board[i][y].type != ' ':
                        return False, "Something in the way of the rook while going down."

        return True, "Success"
