import pygame


def DrawBoard(game_display, size, selected, turn, illegal_move="", moves=None):
    # Our chess draw board code taken from here
    # https://stackoverflow.com/questions/45945254/make-a-88-chessboard-in-pygame-with-python

    white = (255, 255, 255)
    black = (50, 50, 50)
    selected_c = (120, 120, 120)
    width, height = size
    boardLength = 8
    size = height / boardLength / 1.25
    game_display.fill(white)

    cnt = 0

    if selected is not None:
        sx, sy = selected
    else:
        sx, sy = None, None

    centers = []
    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for i in range(0, boardLength):
        centers.append([])
        for z in range(0, boardLength):
            centers[i].append(
                ((size * z), (size * i))
            )
            if sx is not None and sy is not None and z == sy and i == sx:
                pygame.draw.rect(game_display, selected_c, [size * z, size * i, size, size])
            elif cnt % 2 == 0:
                pygame.draw.rect(game_display, white, [size * z, size * i, size, size])
            else:
                pygame.draw.rect(game_display, black, [size * z, size * i, size, size])

            if moves is not None and (i, z) in moves:
                # pygame.draw.rect(game_display, (170, 162, 59), [size * z, size * i, size, size])
                cx, cy = centers[i][z]
                # pygame.draw.circle(surface, (100, 162, 10, 150), (cx + (size / 2), cy + (size / 2)), size / 10)
                pygame.draw.rect(surface, (120, 162, 10, 70), [size * z, size * i, size, size])

            cnt += 1

        cnt -= 1

    turn_font = pygame.font.SysFont(pygame.font.get_default_font(), int(width / 35))
    move_font = pygame.font.SysFont(pygame.font.get_default_font(), int(width / 40))

    if turn == 'w':
        turn_text = "White"
    elif turn == 'b':
        turn_text = "Black"
    else:
        raise Exception("Turn is not black or white")
    turn = turn_font.render(f"{turn_text}'s Turn", True, black, white)
    turn_box = turn.get_rect()
    move = turn_font.render(illegal_move, True, black, white)
    move_box = move.get_rect()

    # turn_box.center = (width * boardLength, 0)
    turn_x, turn_y = turn_box.size
    move_x, move_y = move_box.size
    turn_box.center = ((boardLength * size) + (turn_x / 2) + (size / 5), (turn_y / 2) + (size / 5))
    move_box.center = ((boardLength * size) + (move_x / 2) + (size / 5), (move_y / 2) + (size / 5))

    game_display.blit(surface, (0, 0))
    game_display.blit(turn, turn_box)
    game_display.blit(move, move_box)

    return centers
