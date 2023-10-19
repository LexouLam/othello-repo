from enum import Enum


class Pawn(Enum):
    EMPTY = None
    WHITE = 1
    BLACK = 2


class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
