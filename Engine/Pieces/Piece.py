class Piece:
    def __init__(self, board, side: chr, x: int, y: int):
        self.x = x
        self.y = y
        self.side = side
        self.board = board
        self.type = ''

    def is_valid_move(self, x, y):
        pass
