from test_deck import Deck

class Player:
    def __init__(self) -> None:
        self.player_hand = []

    def player_draws(self):
        deck = Deck()
        self.player_hand.append(deck.one_card())


