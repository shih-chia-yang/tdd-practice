from argparse import ArgumentError
from logging import exception
import random

class GameRound:
    def __init__(self):
        self.__cards=[]
        self.__suits_number={"spades":4,"hearts":2,"diamonds":1,"clubs":0}
        self.__ranks_number={3:0,4:1,5:2,6:3
        ,7:4,8:5,9:6,10:7,"jack":8,
        "queen":9,"king":10,"ace":11,2:12}
        self.create_cards()

    @property
    def cards(self):
        return self.__cards

    def create_cards(self):
        suits=["spades","hearts","diamonds","clubs"]
        ranks=["ace",2,3,4,5,6,7,8,9,10,"jack","queen","king"]
        self.__cards={"{0} of {1}".format(rank,suit): self.__suits_number[suit]+self.__ranks_number[rank] for suit in suits for rank in ranks}
        return self.__cards
    
    def dealing(self,number=1):
        if len(self.cards)==0:
            raise Exception("cards are emtpyed")
        if isinstance(number,int):
            cards=random.choices(list(self.cards.keys()),k=number)
            for card in cards:
                self.cards.pop(card)
            return cards[0]
    
    def compare(card,nextcard):
        pass

    def define_compare_rules(self):

        pass
