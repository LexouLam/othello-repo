import pawn


class Board:
    def __init__(self) -> None:
        self.array = [[pawn.Pawn.EMPTY for _ in range(8)] for _ in range(8)]
        self.array[3][3] = pawn.Pawn.WHITE
        self.array[3][4] = pawn.Pawn.BLACK
        self.array[4][3] = pawn.Pawn.BLACK
        self.array[4][4] = pawn.Pawn.WHITE

    def is_move_valid(self, position: pawn.Position):
        return True

    def __add__(self, color, position):
        self.array[position.row][position.col] = color
        return self

    def __getitem__(self, index: tuple):
        i, j = index
        return self.array[i][j]

    def __getitem__(self, position: pawn.Position):
        i, j = position.row, position.col
        return self.array[i][j]

    def check_neighbors(self, color, position: pawn.Position):
        """
        if the player wants to place a pawn color at given position, checks if it is possible
        """
        if color == pawn.Pawn.WHITE:
            opponent_color = pawn.Pawn.BLACK
        elif color == pawn.Pawn.BLACK:
            opponent_color = pawn.Pawn.WHITE
        else:
            raise ValueError("invalid color")
        good_neighbors = []
        for index in {
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        }:
            attempted_position = position + index
            print(index, self[attempted_position] == opponent_color)
            if (
                attempted_position.valid_position()
                and self[attempted_position] == opponent_color
            ):
                print("HEllo")
                good_neighbors.append(attempted_position)

        return color, good_neighbors

    def draw(self):
        print(self.array)


if __name__ == "__main__":
    board = Board()
    # board.draw()
    # print(board.array[0][0])
    print(board.check_neighbors(pawn.Pawn.BLACK, pawn.Position(3, 2)))
