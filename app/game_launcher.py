import sys
import os

module_directory = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(module_directory)

import game
import player  # obligé d'importer chaque module sinon ça ne marche pas (à cause du path)
import board
import pawn
import re

if __name__ == "__main__":
    entree_valide = False
    start_decision = "rien"
    while start_decision not in ["Y", "q"]:
        while entree_valide == False:
            try:
                # code
                start_decision = input("Start game ? (Y/N)\nq : quit\n")
            except ValueError or TypeError:
                # any exception
                print("Input not valid, please try again.")
            else:
                # code to execute when no errors
                entree_valide = start_decision in [
                    "Y",
                    "q",
                ]
    while start_decision != "q":
        player_1_nom = input("Name 1:\n(q : quit)")
        if player_1_nom == "q":
            print("Goodbye.")
            exit()
        else:
            player_1_couleur = "rien"
            while player_1_couleur not in ["white", "black", "q"]:
                player_1_couleur = input("Color : (white / black)\n(q : quit)")
            if player_1_couleur == "q":
                print("Goodbye.")
                exit()
            else:
                player_2_nom = input("Name 2:\n(q : quit)")
                if player_2_nom == "q":
                    print("Goodbye.")
                    exit()
                else:
                    if player_1_couleur == "white":
                        player_1_couleur = pawn.Pawn.WHITE
                        player_2_couleur = pawn.Pawn.BLACK
                    else:
                        player_2_couleur = pawn.Pawn.WHITE

                    player1 = player.Player(player_1_nom, player_1_couleur)
                    player2 = player.Player(player_2_nom, player_2_couleur)
                    # ci-dessous : dans la fonction game.Game.start() le premier joueur nommé est celui qui commence
                    if player_1_couleur == pawn.Pawn.BLACK:
                        game_test = game.Game(player1, player2)
                    else:
                        game_test = game.Game(player2, player1)
                    game.Game.start(game_test)
    print("Goodbye.")
    exit()
