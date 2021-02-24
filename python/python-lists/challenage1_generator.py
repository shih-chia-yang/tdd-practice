import sys
sys.path.append('../../python')
from main_module import create_divider
create_divider("使用generator建立",1,"*")
create_divider("建立52張牌撲克，從牌組隨機抽取5張，列出剩下牌組數量與抽取的撲克牌",1,"*")

import random
suits=["hearts","spades","clubs","diamonds"]
ranks=["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]

cards_generator=([rank,suit] for suit in suits for rank in ranks )
cards =list(cards_generator)
print(f'there are {len(cards)} cards in the deck')
print('dealing...')
player_count=""
while isinstance(player_count,int)==False:
    player_count=input('any number any card :')
    if player_count.isnumeric():
        player_count =int(player_count)
    else:
        print('please enter a number ,not string or others')
selected_cards=random.choices(cards,k=int(player_count))
for selected_card in selected_cards:
    cards.remove(selected_card)
print(f'there are {len(cards)} cards in the deck')
print('player has the following cards in their hand: ')
print(selected_cards)