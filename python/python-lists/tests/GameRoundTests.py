from logging import exception
from argparse import ArgumentError
import sys,io
sys.path.append('../src')
from unittest import TestCase,mock
from GameRound import GameRound

class PorkerTests(TestCase):
    def setUp(self):
        self.gameRound=GameRound()
        self.gameRound.create_cards()
        return super().setUp()

    def test_create_cards_then_return_52_cards(self):
        self.assertEqual(52,len(self.gameRound.cards))

    def test_dealing_then_cards_should_be_decrease(self):
        total_cards_count=len(self.gameRound.cards)
        card=self.gameRound.dealing()
        after_dealing_total_cards_count=len(self.gameRound.cards)
        self.assertRegex(card,"(([2-9]|10|jack|queen|king|ace).of.(hearts|diamonds|spades|clubs))")
        self.assertEqual(total_cards_count-1,after_dealing_total_cards_count)
    
    def test_dealing_after_empty_cards_then_shoule_be_dealing_end(self):
        with self.assertRaises(Exception):
            i=0
            total=len(self.gameRound.cards)+1
            while i<total:
                self.gameRound.dealing()
                i+=1
    def define_compare_rules_should_be_return_dict(self):
        pass
