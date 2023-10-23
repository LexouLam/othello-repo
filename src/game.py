import player
import board
import pawn


class Game:
    def __init__(
        self,
        player1=player.Player("Joueur1", pawn.Pawn.BLACK),
        player2=player.Player("Joueur2", pawn.Pawn.WHITE),
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = board.Board()
        self.pawn_counter = 0

    def start(self):
        player = self.player1  # player1 has white pawns so he starts
        flag_one_cant_play = False  # True if one player can't play, so that we will end the game if the second player cannot play either
        while True:
            if not self.pawn_left():  # all pawns are used so end of games
                return self.end_of_game()
            else:
                if not player.player_can_play(self.board):
                    if flag_one_cant_play:
                        return self.end_of_game()
                    else:
                        player = self.change_player(player)
                        flag_one_cant_play = True
                    continue
                else:  # player can play
                    flag_one_cant_play = False
                    self.read_input(player)
                    player = self.change_player(player)

        pass

    def change_player(self, player: player.Player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def pawn_left(self):
        return self.pawn_counter != 60

    def end_of_game(self):
        for i, j, color in self.board:
            if color == pawn.Pawn.WHITE:
                self.player2.score += 1
            elif color == pawn.Pawn.BLACK:
                self.player1.score += 1
            else:
                continue
        # prompt scores
        self.prompt_scores()

    def prompt_scores(self):
        if self.player1.score > self.player2.score:
            print(f"Player {self.player1.name} has won with {self.player1.score} black")
            print(
                f"Player {self.player2.name} has lost with {self.player2.score} white"
            )
        elif self.player1.score == self.player2.score:
            print("Equal scores of the two players with {self.player1.score} each")
        else:
            print(f"Player {self.player2.name} has won with {self.player2.score} white")
            print(
                f"Player {self.player1.name} has lost with {self.player1.score} black"
            )

    def read_input(self, player):
        input_is_wrong = True
        while input_is_wrong:
            self.board.draw()
            row, col = map(int, input(f"Enter row and col ({player.color}):  ").split())
            position = pawn.Position(row, col)
            if not position.valid_position():
                print("wrong input, try again")
                continue
            else:
                list_of_changes = self.board.check_can_play(player.color, position)
                if (
                    list_of_changes
                ):  # the pawn color and position implies some pawn flip
                    self.board.apply_list_of_changes(list_of_changes)
                    player = self.change_player(player)
                    self.pawn_counter += 1
                    input_is_wrong = False
                else:
                    print("wrong input, try again")
        return


if __name__ == "__main__":
    alexandra = player.Player("Alexandra", pawn.Pawn.BLACK)
    nicolas = player.Player("Nicolas", pawn.Pawn.WHITE)
    game = Game(alexandra, nicolas)
    game.start()
