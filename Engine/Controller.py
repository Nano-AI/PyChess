from Engine.Board import Board
from Engine.Errors import *


class Controller:
    def __init__(self):
        board = Board()
        # board.move(0, 1, 1, 3)
        # board.move(7, 1, 6, 3)
        # board.print_board()
        while True:
            board.print_board()
            spot = input("Enter piece to select: ").split(" ")
            move_spot = input("Enter spot to move: ").split(" ")
            try:
                board.move(int(spot[0]), int(spot[1]), int(move_spot[0]), int(move_spot[1]))
            except IllegalMove:
                print("You entered an illegal move!")
            except MovingEmptyBox:
                print("You're trying to move an empty box.")
        # board.move(0, 5, 0, 6)
        # print(board.get_logical_spot(0, 3).start_move)
