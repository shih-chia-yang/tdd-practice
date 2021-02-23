from unittest import TestCase
import sys
sys.path.append('../src')
from rock_paper_scissor import Game

class GameTests(TestCase):
    @property
    def determine_Winner_param_List(self):
        return [["It's a Draw", 0, 0,],
            ["Winner is player1", 1, 0],
            ["Winner is player2", 0, 1]]

    def test_init(self):
        game=Game()
        self.assertIsNotNone(game.participant)
        self.assertIsNotNone(game.secondParticipant)
        self.assertFalse(game.endGame)


    def testdetermineWinner(self):
        game=Game()
        for params in self.determine_Winner_param_List:
            game.participant.points=params[1]
            game.secondParticipant.points=params[2]
            game.determineWinner()
            self.assertEqual(params[0],game.resultString)