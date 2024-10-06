from Deck_class import Deck # importerar klassen Deck

class Dealer:
    def __init__(self) -> None:
        self.dealer_hand: list = [] # en lista som innehåller delarens kort

    def dealer_draws(self) -> None: # metoden lägger till ett kort till delarens hand
        deck = Deck() # skapar en instans av klassen Deck, som hanterar kortleken
        self.dealer_hand.append(deck.one_card()) # drar ett kort till delarens hand med metoden one_card från klassen Deck