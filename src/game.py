import player
import board
import pawn


class Game:
    def __init__(
        self,
        player1=player.Player("Joueur1", pawn.Pawn.BLACK),  # règles noir commence
        player2=player.Player("Joueur2", pawn.Pawn.WHITE),
    ) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = board.Board()
        self.tour_counter = 0

    def start(self):
        player = self.player1
        while self.game_can_continue():
            if not player.player_can_play(self.board):
                player = self.change_player(player)
            input_is_wrong = True
            while input_is_wrong:
                self.board.draw()
                #####
                position = self.input_position(player)
                #####
                if not position.valid_position():
                    print("wrong input, try again")
                    continue
                list_of_changes = self.board.check_can_play(player.color, position)
                if list_of_changes:
                    self.board.apply_list_of_changes(list_of_changes)
                    self.board.draw()
                    input_is_wrong = False
                    player = self.change_player(player)
                else:
                    print("wrong input, try again")

        pass

    def input_position(self, player: player.Player):
        position_input = input(f"Enter a position {player.name} (ex : a1) : (q : quit)")
        if position_input == "q":
            print("Goodbye.")
            exit()
        else:
            col = ord(list(position_input.lower())[0]) - ord("a")
            row = int(list(position_input)[1]) - 1
            return pawn.Position(row, col)

    def game_can_continue(self) -> bool:
        return (
            self.player1.player_can_play(self.board)
            or self.player2.player_can_play(self.board)
        ) and self.tour_counter < 60

    def change_player(self, player: player.Player):
        if player == self.player1:
            player = self.player2
        else:
            player = self.player1
        return player


if __name__ == "__main__":
    nicolas = player.Player("Nicolas", pawn.Pawn.WHITE)
    alexandra = player.Player("Alexandra", pawn.Pawn.BLACK)
    game = Game(nicolas, alexandra)
    # for i, j, element in game.board:
    #     print(i, j, element)
    game.start()
