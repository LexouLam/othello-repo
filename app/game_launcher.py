import sys
import os

module_directory = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(module_directory)

import game
import player  # obligé d'importer chaque module sinon ça ne marche pas (à cause du path)
import board
import pawn
import re


def input_start_game():
    """
    Demande de lancement du jeu.
    ----
    input : réponse à "veux-tu jouer?"
    output : "start_decision" = string qui vaut "y"
    """
    entree_valide = False
    start_decision = "rien"
    while start_decision.lower() not in ["y", "q"]:
        while entree_valide == False:
            try:
                # code
                start_decision = input("Start game ? (Y/N)\nq : quit\n")
            except ValueError or TypeError:
                # any exception
                print("Input not valid, please try again.")
            else:
                # code to execute when no errors
                entree_valide = start_decision.lower() in ["y", "q"]
    if start_decision.lower() == "q":
        print("Goodbye.")
        exit()
    else:
        return start_decision.lower()


def input_carac_players(start_decision):
    """
    Donne les caractéristiques des joueurs : noms et couleur.
    ----
    Input : demandé via input.
    Output : deux objets player1 et player2 de la classe "Player"
    """
    if start_decision == "y":
        player_1_nom = input("Name 1:\n(q : quit)")
        if player_1_nom.lower() == "q":
            print("Goodbye.")
            exit()
        else:
            player_1_couleur = "rien"
            while player_1_couleur.lower() not in ["white", "black", "q"]:
                player_1_couleur = input("Color : (white / black)\n(q : quit)")
            if player_1_couleur.lower() == "q":
                print("Goodbye.")
                exit()
            else:
                player_2_nom = input("Name 2:\n(q : quit)")
                if player_2_nom.lower() == "q":
                    print("Goodbye.")
                    exit()
                else:
                    if player_1_couleur.lower() == "white":
                        player_1_couleur = pawn.Pawn.WHITE
                        player_2_couleur = pawn.Pawn.BLACK
                    else:
                        player_1_couleur = pawn.Pawn.BLACK
                        player_2_couleur = pawn.Pawn.WHITE
        player1 = player.Player(player_1_nom, player_1_couleur)
        player2 = player.Player(player_2_nom, player_2_couleur)
        return player1, player2
    else:
        print("There is a problem. I am crashing.")
        exit()


def game_launch(player1: player.Player, player2: player.Player):
    """
    Lancement de la partie, le joueur qui a les noirs sera le premier à jouer donc donné dans le premier argument.
    ----
    Input : player1 et player2, deux objets de la classe Player
    Output : une partie game_test
    """
    if player1.color == pawn.Pawn.BLACK:
        game_test = game.Game(player1, player2)
    else:
        game_test = game.Game(player2, player1)
    return game_test


if __name__ == "__main__":
    start_decision = input_start_game()
    players = input_carac_players(start_decision)
    game_test = game_launch(players[0], players[1])
    game.Game.start(game_test)
