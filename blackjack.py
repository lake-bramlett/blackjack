import random
from deck import Deck

def play_blackjack():
    deck = Deck()
        game_cards = random.shuffle(deck.cards)
        for card in deck.cards:
            print(str(card.value) + " of " + str(card.suit))


def run_blackjack():
    answer = raw_input('Do you want to play Blackjack? ')
    answer = answer.lower()
    if answer == 'yes' or answer == 'y':
        play_blackjack()
    elif answer == 'no' or answer == 'n':
        print('Okay! See you later!')
    else: 
       print('I\'m sorry, I didn\'t quite undertand you.')
       run_blackjack()
       
run_blackjack()
