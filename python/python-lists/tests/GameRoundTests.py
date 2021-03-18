import sys,io
sys.path.append('../src')
from json.tool import main
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
    def test_get_card_number_from_cards(self):
        self.assertEqual(57,self.gameRound.get_card_number("ace of hearts"))

    def test_compare_one_cards_should_be_return_bool(self):
        diff1=self.gameRound.compare("7 of spades","ace of hearts")
        self.assertEqual(True,diff1)
        diff2=self.gameRound.compare("2 of clubs","ace of hearts")
        self.assertEqual(False,diff2)
    
    def test_compare_two_cards_should_be_return_bool(self):
        diff=self.gameRound.compare(["7 of spades","7 of clubs"],["7 of hearts","7 of diamonds"])
        self.assertEqual(False,diff)
    


if __name__=="__main__":
    main()