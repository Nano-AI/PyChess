from Engine.Board import *
from GUI.Board.DrawBoard import *
import pygame


class BoardGUI:
    def __init__(self):
        self.board = Board()
        self.image_path = "Pieces/"
        self.default_piece_image = self.image_path + 'White/Pawn.png'

        pygame.init()
        self.screen_info = pygame.display.Info()
        self.size = (self.width, self.height) = (
            int(self.screen_info.current_w * 1), int(self.screen_info.current_h * 1))

        self.screen = pygame.display.set_mode((int(self.height / 1.25), int(self.height / 1.25)))
        self.clock = pygame.time.Clock()

        self.selected = None
        self.moving_to = None

        self.piece_images, self.piece_rectangles = None, None
        self.centers = DrawBoard(self.screen, self.size)
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
                            if self.piece_rectangles[i][j] is not None and self.piece_rectangles[i][j].collidepoint(x, y):
                                if self.selected is None and self.board.board[i][j].type != ' ':
                                    self.selected = (i, j)
                                elif self.selected is not None and self.moving_to is None:
                                    self.moving_to = (i, j)
                                    if self.selected != self.moving_to:
                                        x, y = self.convert_to_logical(self.selected)
                                        x1, y1 = self.convert_to_logical(self.moving_to)
                                        try:
                                            self.board.move(x, y, x1, y1)
                                            self.update_board()
                                            # self.screen.blit(self.piece_images[i][j], self.moving_to)
                                        except Exception as e:
                                            print("Sorry, but the move you played is illegal.\n", e)
                                    self.selected = None
                                    self.moving_to = None
                                elif self.selected is None and self.moving_to is not None:
                                    raise Exception("Selected is somehow none while the moving spot is not.")
                                elif self.selected is not None and self.moving_to is not None:
                                    self.selected = None
                                    self.moving_to = None
                                # else:
                                #     raise Exception("Somehow the selected and moving spot is not working?")

                if not running:
                    pygame.quit()
                    quit()
                pygame.display.update()
            self.clock.tick(60)

    def update_board(self):
        DrawBoard(self.screen, self.size)
        for x in range(len(self.piece_images)):
            for y in range(len(self.piece_images[x])):
                self.piece_images[x][y].set_alpha(0)
                piece_image_path = self.get_image(self.board.board[x][y])
                piece = None
                if piece_image_path is not None:
                    try:
                        piece = pygame.image.load(piece_image_path)
                    except FileNotFoundError:
                        print(f"Image path not found: {piece_image_path}")
                    except Exception as e:
                        raise e
                else:
                    try:
                        piece = pygame.image.load(self.default_piece_image)
                    except FileNotFoundError:
                        print(f"Image path not found: {piece_image_path}")
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
                        piece = pygame.image.load(piece_image_path)
                    except FileNotFoundError:
                        print(f"Image path not found: {piece_image_path}")
                    except Exception as e:
                        raise e
                else:
                    try:
                        piece = pygame.image.load(self.default_piece_image)
                    except FileNotFoundError:
                        print(f"Image path not found: {piece_image_path}")
                    except Exception as e:
                        raise Exception(e)
                    piece.set_alpha(0)

                piece = pygame.transform.scale(piece, (int(self.height / 8 / 1.25), int(self.height / 8 / 1.25)))
                piece_rect = piece.get_rect()
                piece_rect.x, piece_rect.y = centers[x][y]
                rectangles[x].append(piece_rect)
                game_display.blit(piece, centers[x][y])
                pieces_images[x].append(piece)
        return pieces_images, rectangles

    def get_image(self, piece):
        side_p = ''
        if isinstance(piece, str):
            if piece.islower():
                side_p += 'White/'
            else:
                side_p += 'Black/'
            if piece.lower() == 'p':
                return self.image_path + side_p + 'Pawn.png'
            if piece.lower() == 'r':
                return self.image_path + side_p + 'Rook.png'
            return None
        if isinstance(piece, Piece):
            if piece.side == 'w':
                side_p = 'White/'
            else:
                side_p += 'Black/'
            if piece.type == 'p':
                return self.image_path + side_p + 'Pawn.png'
            if piece.type == 'r':
                return self.image_path + side_p + 'Rook.png'
            return None

    def convert_to_logical(self, x_y: tuple):
        x, y = x_y
        return y, len(self.board.board_setup[0]) - x - 1
