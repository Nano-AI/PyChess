from typing import List


class Piece:
    def __init__(self, board, side: chr, x: int, y: int):
        self.x = x
        self.y = y
        self.side = side
        self.board = board
        self.type = ''

    def is_valid_move(self, x, y) -> (bool, str):
        """
        This function checks if the spot (x, y) is valid for the piece to move to. If get_guarding_spots returns None,
        it will use this to check for checks/checkmates
        """
        pass

    def get_guarding_spots(self) -> List[tuple]:
        """
        This function gets the spots the piece is guarding, which is used to check for checks/checkmates if it doesn't
        return None. Check king or pawn file for example
        """
        pass
