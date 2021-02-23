
from unittest import TestCase
import sys
sys.path.append('../src')
from rock_paper_scissor import Participant

class TestExerciseMethods(TestCase):
    def test_participant_choice_symbol(self):
        participant = Participant('stone')
        symbol=['rock','paper','scissor']
        participant.choose()
        self.assertTrue(participant.choose_symbol in symbol)
