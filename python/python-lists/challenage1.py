import random
suits=["hearts","spades","clubs","diamonds"]
ranks=["2","3","4","5","6","7","8","9","10","jack","queen","kind","ace"]
cards=[]
for suit in suits:
    for rank in ranks:
        cards.append(f'{rank} of {suit}')

print(f'there are {len(cards)} cards in the deck')
print('dealing...')
player_count=5
selected_cards=random.choices(cards,k=player_count)
for selected_card in selected_cards:
    cards.remove(selected_card)
print(f'there are {len(cards)} cards in the deck')
print('player has the following cards in their hand: ')
print(selected_cards)
