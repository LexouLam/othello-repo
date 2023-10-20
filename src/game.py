import player
import board
import pawn


class Game:
    def __init__(
        self,
        player1=player.Player("Joueur1", pawn.Pawn.WHITE),
        player2=player.Player("Joueur2", pawn.Pawn.BLACK),
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = board.Board()
        self.tour_counter = 0

    def start(self):
        # while (
        #     self.player1.can_play or self.player2.can_play
        # ) and self.tour_counter < 60:
        #     while True:
        #         row, col = input("Give me your coordinates :").split()
        #         pass
        pass

    def game_can_continue(self) -> bool:
        return (
            self.player1.player_can_play(self.board)
            or self.player2.player_can_play(self.board)
        ) and self.tour_counter < 60


if __name__ == "__main__":
    nicolas = player.Player("Nicolas", pawn.Pawn.WHITE)
    alexandra = player.Player("Alexandra", pawn.Pawn.BLACK)
    game = Game(nicolas, alexandra)
    # for i, j, element in game.board:
    #     print(i, j, element)
    print(game.game_can_continue())
