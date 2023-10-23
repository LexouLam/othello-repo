from enum import Enum


class Pawn(Enum):
    EMPTY = None
    WHITE = 1
    BLACK = 2

    def opponent_color(self):
        if self == Pawn.WHITE:
            return Pawn.BLACK
        elif self == Pawn.BLACK:
            return Pawn.WHITE
        else:
            raise ValueError("None color has no opponent")


class Position:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def __add__(self, other):
        return Position(self.row + other[0], self.col + other[1])

    def __str__(self):
        return f"({self.row}, {self.col})"

    def __eq__(self, other) -> bool:
        return (self.row == other.row) and (self.col == other.col)

    def valid_position(self):
        """
        Checks if the position of the neighbor of self obtained by translation (i,j) is still on the board
        """
        return (self.row < 8) and (self.row >= 0) and (self.col < 8) and (self.col >= 0)


if __name__ == "__main__":
    pion = Pawn.WHITE
    print(pion)
