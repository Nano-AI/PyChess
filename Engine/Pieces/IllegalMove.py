def move_check(piece, to_x, to_y):
    temp, prev_x, prev_y = piece.board.get_logical_spot(to_x, to_y), piece.x, piece.y
    piece.board.move(prev_x, prev_y, to_x, to_y, checking=True)
    king = None
    if piece.side == 'w':
        king = piece.board.get_logical_spot()
    else:
        pass
