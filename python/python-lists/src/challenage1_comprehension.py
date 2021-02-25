# import __init__
# import main_module
import random
from GameRound import GameRound 

class Game:
    def __init__(self) :
        self.selected_card=list
        game_round=GameRound()
        # GameRound.create_cards()
        self.all_cards=game_round.cards
        pass

    def start(self):
        any_number=''
        while isinstance(any_number,int)==False:
            any_number=input('any number any card :')
            if any_number.isnumeric():
                any_number =int(any_number)
                self.selected_cards=random.choices(self.all_cards,k=any_number)
            else:
                print('please enter a number ,not string or others')
        self.extract()
    def extract(self):
        for selected_card in self.selected_cards:
            self.all_cards.remove(selected_card)


