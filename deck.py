from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ['Diamonds','Spades','Hearts','Clubs']:
            for value in range(1, 14):
                if value == 1:
                    value = "Ace"
                elif value == 11:
                    value = "Jack"
                elif value == 12:
                    value = "Queen"
                elif value == 13:
                    value = "King"
                self.cards.append(Card(suit, value))