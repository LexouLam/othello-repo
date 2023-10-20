import pawn
import board


class Player:
    def __init__(self, name, color) -> None:
        self.name = name
        self.can_play = True

    def save(self):
        # create joueur_name.txt and add your score
        return

    def can_play(self, board: board.Board):
        for i, j, pion in self.board:
            if pion == pawn.Pawn.EMPTY:
                if board.check_neighbors_and_apply:
                    return
