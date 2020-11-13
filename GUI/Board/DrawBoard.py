import pygame


def DrawBoard(game_display, size):
    # Our code taken from here
    # https://stackoverflow.com/questions/45945254/make-a-88-chessboard-in-pygame-with-python
    white = (255, 255, 255)
    black = (50, 50, 50)
    width, height = size
    boardLength = 8
    size = height / boardLength / 1.25
    game_display.fill(white)

    cnt = 0

    centers = []

    for i in range(0, boardLength):
        centers.append([])
        for z in range(0, boardLength):
            centers[i].append(
                ((size * z), (size * i))
            )
            if cnt % 2 == 0:
                pygame.draw.rect(game_display, white, [size * z, size * i, size, size])
            else:
                pygame.draw.rect(game_display, black, [size * z, size * i, size, size])

            cnt += 1

        cnt -= 1

    pygame.display.update()
    return centers
