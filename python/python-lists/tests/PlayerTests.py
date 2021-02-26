import sys,io
sys.path.append('../src')
from unittest import TestCase,mock
from Player import Player

class PlayerTests(TestCase):

    def setUp(self):
        self.player=Player()
        return super().setUp()

    def test_hand_cards(self):
        self.assertEqual(0,len(self.player.hand_cards))

    def test_take_card_then_hand_cards_increase(self):
        self.player.take_card("2 of spades")
        self.assertEqual(1,len(self.player.hand_cards))
    
    def test_play_card_then_hand_cards_decrease(self):
        self.player.take_card("ace of spades")
        origin_cards=len(self.player.hand_cards)
        self.player.play_card()
        self.assertEqual(len(self.player.hand_cards),origin_cards-1)

    def test_sort_card_then_hand_cards_sort_by_sum(self):
        self.player.take_card("3 of clubs")
        self.player.take_card("10 of clubs")
        self.player.take_card("ace of spades")
        self.player.take_card("2 of spades")
        self.player.take_card("4 of diamonds")
        self.player.take_card("5 of hearts")
        self.player.sort_card()
        self.assertListEqual(["2 of spades","ace of spades","10 of clubs","5 of hearts","4 of diamonds","3 of clubs"],self.player.hand_cards)

    def test_pass_card_then_block_should_be_true(self):
        self.player.pass_card()
        self.assertTrue(self.player.block)