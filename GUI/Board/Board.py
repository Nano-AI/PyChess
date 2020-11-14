import pygame
from GUI.Board.DrawBoard import *
from Engine.Board import *


class BoardGUI:
    def __init__(self):
        self.image_path = "Pieces/"
        self.default_piece_image = self.image_path + 'White/Pawn.png'

        pygame.init()
        self.screen_info = pygame.display.Info()
        self.size = (self.width, self.height) = (int(self.screen_info.current_w * 1), int(self.screen_info.current_h * 1))

        self.screen = pygame.display.set_mode((int(self.height / 1.25), int(self.height / 1.25)))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Chess - Nano-AI")

    def run(self):
        self.board = Board()

        centers = DrawBoard(self.screen, self.size)

        piece_images, piece_rectangles = self.map_board(self.screen, self.board, centers)
        running = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    # for row in piece_rectangles:
                    for i in range(len(piece_rectangles)):
                        # for image in row:
                        for j in range(len(piece_rectangles[i])):
                            if piece_rectangles[i][j] is not None and piece_rectangles[i][j].collidepoint(x, y):
                                print(i, j)

                if not running:
                    pygame.quit()
                    quit()
            self.clock.tick(60)

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
                        raise e
                    piece.set_alpha(0)

                piece = pygame.transform.scale(piece, (int(self.height / 8 / 1.25), int(self.height / 8 / 1.25)))
                piece_rect = piece.get_rect()
                piece_rect.x, piece_rect.y = centers[x][y]
                rectangles[x].append(piece_rect)
                game_display.blit(piece, centers[x][y])
                pieces_images[x].append(piece)
        pygame.display.update()
        return pieces_images, rectangles

    def get_image(self, piece: str):
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
            return self.image_path + side_p + 'Pawn.png'
        return None
        # return image_path + 'White/Pawn.png'
