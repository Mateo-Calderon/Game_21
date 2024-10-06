from Deck_class import Deck # importerar klassen Deck

# klass för spelaren
class Player:
    def __init__(self) -> None:
        self.player_hand = [] # en lista som innehåller delarens kort

    def player_draws(self): # metoden lägger till ett kort till spelarens hand
        deck = Deck() # skapar en instans av klassen Deck, som hanterar kortleken
        self.player_hand.append(deck.one_card()) # drar ett kort från kortleken till spelarens hand
