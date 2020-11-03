class IllegalMove(Exception):
    """Raised when the move can't be played by the piece"""
    pass


class MovingEmptyBox(Exception):
    """Raised when the program is trying to move an empty box"""
    pass
