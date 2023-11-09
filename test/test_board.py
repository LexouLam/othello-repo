import unittest

import sys
import os

module_directory = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(module_directory)

from board import Board
from pawn import Pawn, Position


class Test_Board(unittest.TestCase):
    def test_board(self):
        board = Board()
        pawn = Pawn.BLACK
        position = Position(3, 5)
        output = board.check_can_play(pawn, position)
        expected_output = [(Pawn.BLACK, Position(3, 5), (0, -1), Position(3, 3))]
        self.assertTrue(expected_output == output)


if __name__ == "__main__":
    unittest.main()
