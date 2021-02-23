from unittest import TestCase
import sys
sys.path.append('../src')
from rock_paper_scissor import Participant
from rock_paper_scissor import GameRound

class GameRoundTests(TestCase):
    def setUp(self) -> None:
        p1=Participant('p1')
        p2=Participant('p2')
        self.gameRound=GameRound(p1,p2)

    def test_compareChoices(self):
        result=self.gameRound.compareChoices();
        self.assertEqual(result,"p2")
    def test_awardPoints(self):
        self.assertDictEqual({"p1":1,"p2":2},self.gameRound.awardPoints())
