import sys
import os

module_directory = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(module_directory)

import game
import player  # obligé d'importer chaque module sinon ça ne marche pas (à cause du path)
import board
import pawn

# try: except: pour input

start = False
while start == False:
    start_decision = input("Commencer partie ? (Y/N)\nq pour quitter\n")
    if start_decision == "Y":
        start = True
    # elif start_decision == "q":
    #     break
    else:
        start = False
player_1_nom = input("Nom :")
player_1_couleur = "rien"
while player_1_couleur not in ["blanc", "noir"]:
    player_1_couleur = input("Couleur : (blanc / noir)")
player_2_nom = input("Nom :")
if player_1_couleur == "blanc":
    player_2_couleur = "noir"
else:
    player_2_couleur = "noir"

player1 = player.Player(player_1_nom, player_1_couleur)
player2 = player.Player(player_2_nom, player_2_couleur)

game_test = game.Game(player1, player2)
