import random

class Deck:
    def __init__(self) -> None:
        # skapar ett kortlek som innehåller 52 kort
        # 1 reprensenterar ess som har värdet 1 eller 14
        self.cards: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
        random.shuffle(self.cards) # blandar kortleken slumpmässigt

    def one_card(self) -> int: # metoden returnerar ett heltal från kortleken
        # tar bort och returnerar det sista kortet från listan
        return self.cards.pop()