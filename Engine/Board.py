from typing import List

from Engine.Errors import *
from Engine.Pieces.Empty import *
from Engine.Pieces.Pawn import *
from Engine.Pieces.Rook import *
from Engine.Pieces.Bishop import *
from Engine.Pieces.Knight import *
from Engine.Pieces.Queen import *


def get_side(item: str):
    if item.islower():
        return 'w'
    return 'b'


class Board:
    def __init__(self):
        """
        ----- BOARD KEY -----
        -- White Key --
        r - Black Rook
        h - Black Knight
        b - Black Bishop
        q - Black Queen
        k - Black King
        p - Black Pawn

        -- Black Key --
        R - White Rook
        H - White Knight
        B - White Bishop
        Q - White Queen
        K - Black King
        P - Black Pawn

        -- Misc --
        . - Empty Spot
          - Empty spot
        """
        self.board_setup = [
            ['R', 'H', 'B', 'Q', 'K', 'B', 'H', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'h', 'b', 'q', 'k', 'b', 'h', 'r']
        ]
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
        valid = False
        reason = ""
        try:
            valid, reason = self.get_logical_spot(x, y).is_valid_move(x1, y1)
        except Exception as e:
            raise Exception(e)
        if self.get_logical_spot(x, y).type == ' ':
            raise MovingEmptyBox(f"An empty box is trying to be moved at ({x}, {y}).")
        if self.get_logical_spot(x1, y1).type == 'k':
            raise Exception("King is trying to be captured")
        if not valid:
            piece = self.get_logical_spot(x, y)
            raise IllegalMove(f"{piece.type} at ({piece.x}, {piece.y}) is trying to move to ({x1}, {y1})."
                              f" It is currently at ({x}, {y})\nReason: {reason}")
        self.change_logical_spot(x1, y1, self.get_logical_spot(x, y))
        self.change_logical_spot(x, y, Empty(self, x, y))
        if self.get_logical_spot(x1, y1).type == 'p':
            self.get_logical_spot(x1, y1).start_move = False
        self.get_logical_spot(x1, y1).x = x1
        self.get_logical_spot(x1, y1).y = y1

    def change_logical_spot(self, x: int, y: int, value: Piece):
        self.board[len(self.board[x]) - y - 1][x] = value

    def setup_board(self):
        board = []
        for y in range(len(self.board_setup)):
            total = []
            for x in range(len(self.board_setup[y])):
                total.append(
                    self.get_piece(
                        self.board_setup[y][x], get_side(self.board_setup[y][x]), self.convert_to_logical(x, y)
                    )
                )
            board.append(total)
        return board

    def convert_to_logical(self, x, y):
        return x, len(self.board_setup) - y - 1

    def get_piece(self, s, side, pos):
        x, y = pos
        if s.lower() == 'p':
            return Pawn(self, side, x, y)
        if s.lower() == 'r':
            return Rook(self, side, x, y)
        if s.lower() == 'b':
            return Bishop(self, side, x, y)
        if s.lower() == 'h':
            return Knight(self, side, x, y)
        if s.lower() == 'q':
            return Queen(self, side, x, y)
        return Empty(self, x, y)
