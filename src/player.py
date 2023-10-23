import pawn
import board


class Player:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        self.can_play = True
        self.score = 0

    def save(self):
        # create joueur_name.txt and add your score
        return

    def player_can_play(self, board: board.Board) -> bool:
        self.can_play = False
        for i, j, pion in board:
            if pion == pawn.Pawn.EMPTY:
                if board.check_can_play(self.color, pawn.Position(i, j)):
                    self.can_play = True
        return self.can_play
