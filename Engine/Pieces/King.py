from Engine.Pieces.Piece import Piece

"""
After done making the piece, go to Engine/Board.py and go to the get_piece() function, and add your piece there.
Then, go to Board/Board.py and go to the get_image() function and add you image there.
"""


class King(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.guarding_spots = []
        self.available_moves = []
        self.type = 'k'
        self.around = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1)]

    def is_valid_move(self, x, y):
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if abs(x - self.x) > 1 or abs(y - self.y) > 1:
            return False, "Moving too far"

        spots = []
        # print(len(self.board.board) - 1)
        # print(len(self.board.board[0]) - 1)
        for row in self.board.board:
            for piece in row:
                if piece.type != ' ' and piece.side != self.side:
                    try:
                        piece.get_guarding_spots()
                        # spots.append()
                    except Exception as e:
                        print(piece.x, piece.y, piece.type)
                        # print(e)
        #     for x1 in range(0, len(self.board.board) - 1):
        #         print(x1)
        #         for y1 in range(0, len(self.board.board[x1]) - 1):
        #             print(y1)
        #             if self.board.board[x1][y1].type != ' ' and self.board.board[x1][y1].side != self.side:
        #                 spots.append(self.board.board[x1][y1].get_guarding_spots())

        # print("asdfasdf")
        # for grids in spots:
        #     for grid in grids:
        #         print('---')
        #         for row in grid:
        #             print(row)

        return True, "Success"

    def get_guarding_spots(self):
        """
        . . .
        . k .
        . . .
        """
        spots = []
        spots_around = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for x in range(0, len(self.board.board)):
            spots.append([])
            for y in range(0, len(self.board.board[x])):
                spots[x].append(0)

        for sx, sy in spots_around:
            spots[self.y + sy][self.x + sx] = 1
        # print('-----------')
        # for arr in [ele for ele in reversed(spots)]:
        #     print(arr)
        return [ele for ele in reversed(spots)]
