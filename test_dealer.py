from test_deck import Deck

class Dealer:
    def __init__(self) -> None:
        self.dealer_hand = []

    def dealer_draws(self):
        deck = Deck()
        self.dealer_hand.append(deck.one_card())