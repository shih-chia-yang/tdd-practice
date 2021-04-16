import __init__
import main_module
from challenage1_comprehension import Game

main_module.create_divider("建立52張牌撲克，從牌組隨機抽取5張，列出剩下牌組數量與抽取的撲克牌",1,"*")
main_module.create_divider("使用comprehension建立",1,"*")

game =Game()
print(f'there are {len(game.all_cards)} cards in the deck')
print('dealing...')
game.start()
print(f'there are {len(game.all_cards)} cards in the deck')
print('player has the following cards in their hand: ')
print(game.selected_cards)