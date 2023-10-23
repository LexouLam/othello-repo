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
        self.playing_player = self.player1
        self.board = board.Board()
        self.pawn_counter = 0

    def start(self):
        player = self.player1  # player1 has white pawns so he starts
        flag_one_cant_play = False
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
                    position = self.read_input(player)
                    list_of_changes = self.board.check_can_play(player.color, position)
                    if (
                        list_of_changes
                    ):  # the pawn color and position implies some pawn flip
                        self.board.apply_list_of_changes(list_of_changes)
                        player = self.change_player(player)
                        self.pawn_counter += 1
                    else:
                        print("wrong input, try again")
        pass

    def change_player(self, player: player.Player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def pawn_left(self):
        return self.pawn_counter != 60

    def end_of_game(self):
        # compute score
        # prompt winner
        pass

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
                input_is_wrong = False
        return position


if __name__ == "__main__":
    nicolas = player.Player("Nicolas", pawn.Pawn.WHITE)
    alexandra = player.Player("Alexandra", pawn.Pawn.BLACK)
    game = Game(nicolas, alexandra)
    game.start()
