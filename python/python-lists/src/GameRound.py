from calendar import c
from functools import reduce
import random

class GameRound:
    def __init__(self):
        self.__cards=[]
        self.__suits_number={"spades":4,"hearts":2,"diamonds":1,"clubs":0}
        self.__ranks_number={3:0,4:5,5:10,6:15
        ,7:20,8:25,9:30,10:35,"jack":40,
        "queen":45,"king":50,"ace":55,2:60}
        self.create_cards()

    @property
    def cards(self):
        return self.__cards

    def create_cards(self):
        suits=["spades","hearts","diamonds","clubs"]
        ranks=["ace",2,3,4,5,6,7,8,9,10,"jack","queen","king"]
        self.__cards={f'{rank} of {suit}': self.__suits_number[suit]+self.__ranks_number[rank] for suit in suits for rank in ranks}
        return self.__cards
    
    @staticmethod
    def get_card_number(card):
        gameround= GameRound()
        gameround.create_cards()
        return gameround.cards[card]
    
    def dealing(self,number=1):
        if len(self.cards)==0:
            raise Exception("cards are emtpyed")
        if isinstance(number,int):
            cards=random.choices(list(self.cards.keys()),k=number)
            for card in cards:
                self.cards.pop(card)
            return cards[0]
    
    def compare(self,card,nextcard):
        if isinstance(card,list) and isinstance(nextcard,list):
            first_sum=sum([self.__cards[card] for card in card])
            next_sum=sum([self.__cards[card] for card in nextcard])
            return (first_sum-next_sum)<0

        if isinstance(card,str) and isinstance(nextcard,str):
            difference=self.__cards[card] - self.__cards[nextcard]
        return difference<0

    def define_compare_rules(self):
        pass


# print(GameRound.get_card_number("ace of hearts"))