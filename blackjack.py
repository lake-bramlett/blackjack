import random
from deck import Deck
from threading import Timer


def bust_check(total):
    if total > 21:
        print('Bust!')
                
def calculate_total(cards):
    total = 0
    for card in cards:
        if card.value == 'A':
            total += 11
        elif card.value == 'J' or card.value == 'Q' or card.value == 'K':
            total += 10
        else: 
            total += card.value
    return total


def play_blackjack():
    deck = Deck()
    random.shuffle(deck.cards)
    cards_in_play = deck.cards
    player_cards = []
    player_total: 0
    dealer_cards = []
    dealer_total: 0
    turn = 'player'

    # initial deal    
    for x in [player_cards, dealer_cards]:
        for y in range(2):
            x.append(cards_in_play.pop(0))
    # player turn
    while turn == 'player':
        print('Your hand:')
        for card in player_cards:
            card.display()
        choice = input('Hit or hold? ')
        choice = choice.lower()
        if choice == 'hit':
            cards_in_play[0].display()
            player_cards.append(cards_in_play.pop(0))
            player_total = calculate_total(player_cards)
            bust_check(player_total)
        elif choice == 'hold':
            turn = 'dealer'
        else:
            print('Not a valid selection')

    if turn == 'dealer':
        print('dealer time...')
   

def run_blackjack():
    answer = input('Do you want to play Blackjack? ')
    answer = answer.lower()
    if answer == 'yes' or answer == 'y':
        print('let\'s play!')
        game = Timer(2.0, play_blackjack)
        game.start()
    elif answer == 'no' or answer == 'n':
        print('Okay! See you later!')
    else: 
       print('I\'m sorry, I didn\'t quite undertand you.')
       run_blackjack()
       
run_blackjack()
