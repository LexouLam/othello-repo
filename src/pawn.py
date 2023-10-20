from enum import Enum


class Pawn(Enum):
    EMPTY = None
    WHITE = 1
    BLACK = 2


class Position:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def __add__(self, other):
        return Position(self.row + other[0], self.col + other[1])

    def __str__(self):
        return f"({self.row}, {self.col})"

    def valid_position(self):
        """
        Checks if the position of the neighbor of self obtained by translation (i,j) is still on the board
        """
        return (self.row < 8) and (self.row >= 0) and (self.col < 8) and (self.col >= 0)


pion = Pawn.WHITE
print(pion)
