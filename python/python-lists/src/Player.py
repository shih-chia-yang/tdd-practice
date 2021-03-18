from audioop import reverse
from typing import OrderedDict

from psutil import pid_exists
from GameRound import GameRound

class Player:
    def __init__(self):
        self.hand_cards=[]
        self.block=False
        pass

    def take_card(self,card):
        if isinstance(card,str):
            self.hand_cards.append(card)
    def sort_card(self):
        number_list={card:GameRound.get_card_number(card) for card in self.hand_cards}
        rank_list={k:number_list[k] for k in sorted(number_list, key=number_list.get, reverse=True)}
        self.hand_cards=list(rank_list.keys())
            
    def play_card(self):
        if self.hand_cards:
            self.hand_cards.pop(0)
    def pass_card(self):
        if self.block==True:
            self.block=False
        else:
            self.block=True

player=Player()
player.take_card("3 of clubs")
player.take_card("10 of clubs")
player.take_card("ace of spades")
player.take_card("2 of spades")
player.take_card("4 of diamonds")
player.take_card("5 of hearts")
player.sort_card()