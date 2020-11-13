import pygame
from GUI.Board.DrawBoard import DrawBoard
from Engine.Board import *
from Engine.Pieces.Piece import Piece
import os

image_path = "Pieces/"

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (int(screen_info.current_w * 1), int(screen_info.current_h * 1))

screen = pygame.display.set_mode((int(height / 1.25), int(height / 1.25)))


def main():
    global screen
    board = Board()

    centers = DrawBoard(screen, size)

    map_board(screen, board, centers)

    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
        clock.tick(60)


def map_board(game_display, board, centers):
    pieces_images = []
    for x in range(len(board.board_setup)):
        pieces_images.append([])
        for y in range(len(board.board_setup[x])):
            piece_image_path = get_image(board.board_setup[x][y])
            piece = None
            if piece_image_path is not None:
                try:
                    piece = pygame.image.load(piece_image_path)
                except FileNotFoundError:
                    print(f"Image path not found: {piece_image_path}")
                except Exception as e:
                    raise e
                piece = pygame.transform.scale(piece, (int(height / 8 / 1.25), int(height / 8 / 1.25)))
                game_display.blit(piece, centers[x][y])
            pieces_images[x].append(piece)

            # piece = pygame.image.load(get_image(board.get_spot(x, y))).convert_alpha()
            # piece.get_rect()
            # pieces_images[x].append(piece)

    pygame.display.update()


def get_image(piece: str):
    global image_path
    # return 'Pieces/White/Pawn.png'
    """
    Pieces/Black/Pawn.png
    Pieces/White/Pawn.png
    Pieces/Black/Pawn.png
    """
    side_p = ''

    if piece.islower():
        side_p += 'White/'
    else:
        side_p += 'Black/'
    if piece.lower() == 'p':
        return image_path + side_p + 'Pawn.png'
    return None


clock = pygame.time.Clock()

main()
