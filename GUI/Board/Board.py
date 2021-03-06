from Engine.Board import *
from GUI.Board.DrawBoard import *
import pygame
import os
from Engine.Errors import *
from Engine.Pieces.King import King
import pickle


class BoardGUI:
    def __init__(self):
        self.board = Board()
        self.image_path = "GUI/Pieces/"
        self.default_piece_image = self.image_path + 'White/Pawn.png'

        pygame.init()
        self.screen_info = pygame.display.Info()
        self.size = (self.width, self.height) = (
            int(self.screen_info.current_w * 1), int(self.screen_info.current_h * 1))

        self.screen = pygame.display.set_mode((int(self.height / 1.25) + int(self.height / 4), int(self.height / 1.25)))
        self.clock = pygame.time.Clock()

        self.selected = None
        self.moving_to = None

        self.turn = 'w'

        self.piece_images, self.piece_rectangles = None, None
        self.centers = DrawBoard(self.screen, self.size, self.selected, self.turn)

        self.protected_spots = []

        self.white_checked = False
        self.black_checked = False

        self.black_x_y = None
        self.white_x_y = None

        pygame.display.set_caption("Chess - Nano-AI")

    def run(self):
        self.piece_images, self.piece_rectangles = self.map_board(self.screen, self.board, self.centers)
        running = True
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    for i in range(len(self.piece_rectangles)):
                        for j in range(len(self.piece_rectangles[i])):
                            if self.piece_rectangles[i][j] is not None and self.piece_rectangles[i][j].collidepoint(x,
                                                                                                                    y):
                                if self.selected is None and self.board.board[i][j].type != ' ' and \
                                        self.board.board[i][j].side == self.turn:
                                    self.selected = (i, j)
                                elif self.selected is not None and self.moving_to is None:
                                    self.moving_to = (i, j)
                                    if self.selected != self.moving_to:
                                        x, y = self.convert_to_logical(self.selected)
                                        x1, y1 = self.convert_to_logical(self.moving_to)
                                        try:
                                            """This is where the piece gets moved when a player clicks on it and 
                                            selects a spot"""
                                            # self.board.move(x, y, x1, y1)
                                            print(self.black_checked, self.white_checked)
                                            if self.black_checked or self.white_checked:
                                                can, error = self.check_move(x, y, x1, y1)
                                                if can:
                                                    self.move(x, y, x1, y1)
                                                else:
                                                    raise IllegalMove(error)

                                            elif self.turn == 'b' and not self.black_checked:
                                                self.move(x, y, x1, y1)

                                            elif self.turn == 'w' and not self.white_checked:
                                                self.move(x, y, x1, y1)
                                        except IllegalMove as e:
                                            print("Sorry, but the move you played is illegal.\n", e)
                                        except Exception as e:
                                            raise e
                                    self.selected = None
                                    self.moving_to = None
                                elif self.selected is None and self.moving_to is not None:
                                    raise Exception("Selected is somehow none while the moving spot is not.")
                                elif self.selected is not None and self.moving_to is not None:
                                    self.selected = None
                                    self.moving_to = None
                    self.update_board()

                if not running:
                    pygame.quit()
                    quit()
                pygame.display.update()
            self.clock.tick(120)

    def update_board(self):
        if self.selected is not None:
            sx, sy = self.selected
            # possible_moves = self.board.get_logical_spot(sx, sy).get_possible_spots()
            spot = self.board.board[sx][sy]
            possible_moves = []
            for i in range(0, 8):
                for j in range(0, 8):
                    ii, ij = self.convert_to_logical((i, j))
                    try:
                        if spot.type != ' ':
                            valid, reason = spot.is_valid_move(ii, ij)
                            if valid:
                                possible_moves.append((i, j))

                        """This is where I check if the king has been checked"""
                        if self.board.get_logical_spot(ii, ij).type == 'k':
                            king = self.board.get_logical_spot(ii, ij)
                            checked, _ = king.is_checked()
                            if king.side == 'w':
                                self.white_checked = checked
                                self.white_x_y = self.convert_to_logical((ii, ij))
                            elif king.side == 'b':
                                self.black_checked = checked
                                self.black_x_y = self.convert_to_logical((ii, ij))

                    except Exception as e:
                        raise e
            DrawBoard(self.screen, self.size, self.selected, self.turn, moves=possible_moves)
        else:
            DrawBoard(self.screen, self.size, self.selected, self.turn)
        for x in range(len(self.piece_images)):
            for y in range(len(self.piece_images[x])):
                self.piece_images[x][y].set_alpha(0)
                piece_image_path = self.get_image(self.board.board[x][y])
                piece = None
                if piece_image_path is not None:
                    try:
                        piece = pygame.image.load(piece_image_path)
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Image path not found (update board): {piece_image_path}")
                    except Exception as e:
                        raise e
                else:
                    try:
                        piece = pygame.image.load(self.default_piece_image)
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Image path not found (update board): {piece_image_path}")
                    except Exception as e:
                        raise e
                    piece.set_alpha(0)
                piece = pygame.transform.scale(piece, (int(self.height / 8 / 1.25), int(self.height / 8 / 1.25)))
                self.screen.blit(piece, self.centers[x][y])

    def map_board(self, game_display, board, centers):
        pieces_images = []
        rectangles = []
        for x in range(len(board.board_setup)):
            pieces_images.append([])
            rectangles.append([])
            for y in range(len(board.board_setup[x])):
                piece_image_path = self.get_image(board.board_setup[x][y])
                piece = None
                if piece_image_path is not None:
                    try:
                        path = os.path.abspath(piece_image_path)
                        piece = pygame.image.load(path)
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Image path not found (map_board): {path}")
                    except Exception as e:
                        raise e
                else:
                    try:
                        path = os.path.abspath(self.default_piece_image)
                        piece = pygame.image.load(path)
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Image path not found (map_board): {path}")
                    except Exception as e:
                        raise e
                    piece.set_alpha(0)

                piece = pygame.transform.scale(piece, (int(self.height / 8 / 1.25), int(self.height / 8 / 1.25)))
                piece_rect = piece.get_rect()
                piece_rect.x, piece_rect.y = centers[x][y]
                rectangles[x].append(piece_rect)
                game_display.blit(piece, centers[x][y])
                pieces_images[x].append(piece)
        return pieces_images, rectangles

    def get_image(self, piece):
        piece_name = ""
        if isinstance(piece, str):
            piece_name = piece.lower()
        if isinstance(piece, Piece):
            piece_name = piece.type
        pieces = {
            'p': 'Pawn.png',
            'r': 'Rook.png',
            'b': 'Bishop.png',
            'h': 'Knight.png',
            'q': 'Queen.png',
            'k': 'King.png'
        }
        try:
            return self.get_image_path(piece) + pieces[piece_name]
        except KeyError:
            pass

    def get_image_path(self, piece):
        side_p = ""
        if isinstance(piece, str):
            if piece.islower():
                side_p += 'White/'
            else:
                side_p += 'Black/'
        if isinstance(piece, Piece):
            if piece.side == 'w':
                side_p = 'White/'
            else:
                side_p += 'Black/'
        return self.image_path + side_p

    def convert_to_logical(self, x_y: tuple):
        x, y = x_y
        # return x, len(self.board.board_setup[0]) - y - 1
        return y, len(self.board.board_setup[0]) - x - 1

    def check_move(self, x: int, y: int, to_x: int, to_y: int):
        can, error = self.board.get_logical_spot(x, y).is_valid_move(to_x, to_y)
        if not can:
            return False, error
        if self.board.get_logical_spot(x, y).type == 'w':
            kx, ky = self.white_x_y
        else:
            kx, ky = self.black_x_y
        piece = self.board.get_logical_spot(kx, ky)
        if piece.type != 'k' and not piece.move_piece_check(x, y):
            DrawBoard(self.screen, self.size, self.selected, self.turn, illegal_move=f"The {piece.side} king is in check!")

        return True, None
        # self.board.move()

    def move(self, x: int, y: int, x1: int, y1: int):
        self.board.move(x, y, x1, y1)
        self.turn = 'b' if self.turn == 'w' else 'w'
        self.update_board()
