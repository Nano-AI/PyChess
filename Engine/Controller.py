from Engine.Board import Board


class Controller:
    def __init__(self):
        board = Board()
        board.move(0, 1, 0, 3)
        # board.move(1, 1, 1, 3)
        board.move(0, 3, 0, 5)
        # print(board.get_logical_spot(0, 3).start_move)
        board.print_board()
