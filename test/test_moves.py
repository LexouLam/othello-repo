# "some tests"

# https://realpython.com/python-testing/#writing-your-first-test
# Lastly, if your source code is not in the directory root and contained in a subdirectory,
# for example in a folder called src/, you can tell unittest where to execute the tests so that
# it can import the modules correctly with the -t flag:

# python -m unittest discover -s test -t src

import unittest
import os
from src.pawn import Position


class Test_Pawn(unittest.TestCase):
    def test_valid_position(self):
        position = Position(8, 8)
        output = position.valid_position()
        self.assertFalse(output)
        position = Position(7, 7)
        output = position.valid_position()
        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
