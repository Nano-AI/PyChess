from Engine.Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'p'
        self.start_move = True

    def is_valid_move(self, x, y):
        # print(f"---\nCurrent values: ({self.x}, {self.y})\nGoing to: ({x}, {y})\nstart_move: {self.start_move}")
        if y - self.y < 0:  # Checks if move is backwards or same spot
            return False
        if y - self.y >= 3:  # Checks if move is over 2 boxes up
            return False
        if not self.start_move and y - self.y >= 2:  # Checks if the move is above 2 boxes if the start move is false
            return False
        if self.x == x and self.board.get_logical_spot(x, y).type != ' ':
            return False
        if self.x - x > 1 or self.x - x < -1:
            return False
        if self.x - x == 1 or self.x - x == -1:
            if y - self.y > 1:
                return False
        if self.x - x == 1 or self.x - x == -1:
            pass
        return True
