from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ['♥','♦','♣','♠']:
            for value in range(1, 14):
                if value == 1:
                    value = "A"
                elif value == 11:
                    value = "J"
                elif value == 12:
                    value = "Q"
                elif value == 13:
                    value = "K"
                self.cards.append(Card(suit, value))