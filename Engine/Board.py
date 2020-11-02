from typing import List
from Engine.Pieces.ImportAll import *


class Board:
    def __init__(self):
        self.board: List[List[Piece]] = self.setup_board()

    def print_board(self):
        for row in self.board:
            string = ""
            for piece in row:
                if piece.side == 'b':
                    string += piece.type.upper()
                elif piece.type == ' ':
                    string += '.'
                else:
                    string += piece.type
            print(string)

    def get_board(self):
        return self.board

    def get_spot(self, x, y):
        return self.board[int(y)][int(x)]

    def get_logical_spot(self, x, y) -> Piece:
        return self.board[len(self.board[int(x)]) - int(y) - 1][int(x)]

    def move(self, x, y, x1, y1):
        if not self.get_logical_spot(x, y).is_valid_move(x1, y1):
            return False
        self.change_logical_spot(x1, y1, self.get_logical_spot(x, y))
        self.change_logical_spot(x, y, Empty(self, x, y))
        if self.get_logical_spot(x1, y1).type == 'p':
            self.get_logical_spot(x1, y1).start_move = False
        self.get_logical_spot(x1, y1).x = x1
        self.get_logical_spot(x1, y1).y = y1

    def change_logical_spot(self, x: int, y: int, value: Piece):
        self.board[len(self.board[x]) - y - 1][x] = value

    def setup_board(self):
        board = [[], [], [], [], [], [], [], []]
        bottom = [
            'r', 'h', 'b', 'q', 'k', 'b', 'h', 'r'
        ]
        for x in range(len(board)):
            if x == 1:
                for y in range(len(board)):
                    board[x].append(Pawn(self, 'b', y, 7 - x))

            elif x == 6:
            # elif x == 5:
                for y in range(len(board)):
                    board[x].append(Pawn(self, 'w', y, 7 - x))

            else:
                for y in range(len(board)):
                    board[x].append(Empty(self, y, 7 - x))

        return board
