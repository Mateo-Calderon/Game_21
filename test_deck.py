import random

class Deck:
    def __init__(self) -> None:
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
        random.shuffle(self.cards)

    def one_card(self):
        return self.cards.pop()