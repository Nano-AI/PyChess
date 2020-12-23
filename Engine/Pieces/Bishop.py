from Engine.Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, board, side: chr, x: int, y: int):
        super().__init__(board, side, x, y)
        self.type = 'b'

    def is_valid_move(self, x, y):
        if self.board.get_logical_spot(x, y).side == self.side:
            return False, "Capturing own piece"
        if x - self.x == 0:
            return False, "Moving vertically"
        if y - self.y == 0:
            return False, "Moving horizontally"
        if abs((y - self.y) / (x - self.x)) != 1:  # Getting slope of movement
            return False, "Not moving diagonally"

        dy = (y - self.y)
        dx = (x - self.x)

        rl = 1 if dx > 0 else -1

        if dy > 0:  # Moving up
            for i in range(1, abs(dx)):
                if self.board.get_logical_spot(self.x + (i * rl), self.y + i).type != ' ':
                    return False, "Object blocking path"

        if dy < 0:  # Moving down
            for i in range(1, abs(dy)):
                if self.board.get_logical_spot(self.x + (i * rl), self.y + -i).type != ' ':
                    return False, "Object blocking path"
        return True, "Success"

    def get_guarding_spots(self):
        spots = []

        spots_till_right = len(self.board.board[0]) - self.x - 1
        spots_till_left = len(self.board.board[0]) - spots_till_right - 1

        spots_till_up = len(self.board.board) - self.y - 1
        spots_till_down = len(self.board.board) - spots_till_up - 1

        # print(spots_till_right, spots_till_left, spots_till_up, spots_till_down)

        for x in range(0, len(self.board.board)):
            spots.append([])
            for y in range(0, len(self.board.board[x])):
                spots[x].append(0)

        small_top_right = (spots_till_right if spots_till_right < spots_till_up else spots_till_up)
        small_top_left = (spots_till_left if spots_till_left < spots_till_up else spots_till_up)
        small_down_right = (spots_till_right if spots_till_right < spots_till_down else spots_till_down)
        small_down_left = (spots_till_left if spots_till_left < spots_till_down else spots_till_left)

        # print(spots_till_right, spots_till_left, spots_till_up, spots_till_down)

        # This fills spots it's guarding for top right
        if small_top_right != 0:
            for i in range(1, small_top_right + 1):
                """The if statement in the for range selects the smaller value, because you don't want to be scanning
                if it's out of bounds"""
                spots[self.y + i][self.x + i] = 1
                if self.board.board[self.x + i][self.y + i].type != ' ':
                    break

        # This fills spots it's guarding for top left
        if small_top_left != 0:
            for i in range(1, small_top_left + 1):
                spots[self.y + i][self.x - i] = 1
                if self.board.board[self.x + i][self.y - i].type != ' ':
                    break

        # This fills spots it's guarding for the bottom right
        if small_down_right != 0:
            for i in range(1, small_down_right + 1):
                spots[self.y - i][self.x + i] = 1
                if self.board.board[self.x - i][self.y + i].type != ' ':
                    break

        # This fills spots it's guarding from the bottom left
        if small_down_left != 0:
            for i in range(1, small_down_left + 1):
                spots[self.y - i][self.x - i] = 1
                if self.board.board[self.x - i][self.y - i].type != ' ':
                    print(self.y - i, self.x - i)
                    break

        # print('-----------')
        # for arr in [ele for ele in reversed(spots)]:
        #     print(arr)

        return [ele for ele in reversed(spots)]
