from Engine.Pieces.Piece import Piece

"""
After done making the piece, go to Engine/Board.py and go to the get_piece() function, and add your piece there.
Then, go to Board/Board.py and go to the get_image() function and add you image there.
"""


class Template(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = ' '  # ENTER THE TYPE HERE

    def is_valid_move(self, x, y):
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        return True, "Success"

    def get_guarding_spots(self):
        spots = []
        for x in range(0, len(self.board.board)):
            spots.append([])
            for y in range(0, len(self.board.board[x])):
                spots[x].append(0)

        return [ele for ele in reversed(spots)]
