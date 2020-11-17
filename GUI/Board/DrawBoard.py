import pygame


def DrawBoard(game_display, size, selected):
    # Our code taken from here
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

            cnt += 1

        cnt -= 1

    return centers
