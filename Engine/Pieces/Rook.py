from Engine.Pieces.Piece import Piece


class Rook(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'r'
        self.start_move = True

    def is_valid_move(self, x, y):
        if x != self.x and y != self.y:  # If the user is going horizontally and vertically
            return False, "You can't move vertically and horizontally at the same time!"

        if self.road_block(x, y):
            return False

        return True

    def road_block(self, x, y):
        """Checks if there is a piece between the place where the user wants to go and where they currently are"""
        if x != self.x:  # Moving horizontally
            pass

        elif y != self.y:  # Moving vertically
            pass
