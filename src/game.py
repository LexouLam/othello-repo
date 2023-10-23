import player
import board
import pawn
import re  # pour le test regex désolée


class Game:
    def __init__(
        self,
        player1=player.Player("Joueur1", pawn.Pawn.BLACK),  # règles noir commence
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
            self.display_scores()
            self.board.draw()
            position = self.input_position(player)
            if not position.valid_position():
                print("wrong input, try again")
                continue
            else:
                list_of_changes = self.board.check_can_play(player.color, position)
                if (
                    list_of_changes
                ):  # the pawn color and position implies some pawn flip
                    self.board.apply_list_of_changes(list_of_changes)
                    self.display_scores()
                    self.board.draw()
                    input_is_wrong = False
                    player = self.change_player(player)
                    self.pawn_counter += 1
                    input_is_wrong = False
                else:
                    print("wrong input, try again")
        pass

    def input_position(self, player: player.Player):
        """
        Traduit la position donnée par le joueur en cours dans un format compréhensible pour le jeu (un objet de classe Position contenant deux valeurs)
        ----
        Input : le jeu (classe Game) incluant son board et les joueurs (classe Player)
        Output : pawn.Position(row, col) avec row = int() et col = int()
        """
        position_input = "rien"
        # "tant que l'input est différent de "[a-Z][digit]" ou "q", faire:
        while re.fullmatch("([a-z][1-8])|(q)", position_input.lower()) == None:
            try:
                position_input = input(
                    f"Enter a position {player.name} (ex : a1) : (q : quit)"
                )
            except ValueError or TypeError:
                print("Input not valid, please try again.")
        # quand l'input est égal à "[a-Z][digit]" ou "q" :
        if position_input == "q":
            print("Goodbye.")
            exit()
        else:
            col = ord(list(position_input.lower())[0]) - ord("a")
            row = int(list(position_input)[1]) - 1
            return pawn.Position(row, col)

    def display_scores(self):
        """
        Donne le score de chaque joueur au moment où.
        ----
        Input : le jeu en cours (avec son tableau).
        Output : une chaîne de caractères (qui doit être affichée avant le board)
        """
        # on va compter le nombre de X et le nb de O sur le board
        nb_black = 0
        nb_white = 0
        nb_empty = 0
        for row in range(8):
            for col in range(8):
                if self.board.array[row][col] == pawn.Pawn.BLACK:
                    nb_black = nb_black + 1
                elif self.board.array[row][col] == pawn.Pawn.WHITE:
                    nb_white = nb_white + 1
                elif self.board.array[row][col] == pawn.Pawn.EMPTY:
                    nb_empty = nb_empty + 1
        print(
            f"Score {self.player1.name} (black) : ",
            nb_black,
            f"Score {self.player2.name} (white) : ",
            nb_white,
            "   |   X : black, O : white",
        )

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
    alexandra = player.Player("Alexandra", pawn.Pawn.BLACK)
    nicolas = player.Player("Nicolas", pawn.Pawn.WHITE)
    game = Game(alexandra, nicolas)
    game.start()
