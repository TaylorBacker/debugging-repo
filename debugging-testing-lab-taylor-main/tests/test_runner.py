# To run tests, navigate to the top-level directory of
# the codebase and run:
#    python -m unittest
import unittest
import unittest.mock as mock
from dicegame.runner import GameRunner


class TestRunner(unittest.TestCase):

    def test_winCount(self):
        """checks a valid win count"""
        valid_wins = list(range(0, 6))
        for i in range(100):
            d = GameRunner()
            self.assertIn(d.wins, valid_wins)

    def test_lossCount(self):
        """checks a valid loss count"""
        valid_losses = list(range(0, 6))
        for i in range(100):
            d = GameRunner()
            self.assertIn(d.loses, valid_losses)

    def test_roundCount(self):
        ''' checks round count always above 1'''
        valid_rounds = list(range(1,1000))
        for i in range(100):
            d = GameRunner()
            self.assertIn(d.round, valid_rounds)

if __name__ == "__main__":
    unittest.main()

        