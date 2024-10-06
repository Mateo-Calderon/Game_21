from Player_class import Player # importerar Player klassen
from Dealer_class import Dealer # importerar Dealer klassen
from Score_class import calculate_score # importerar funktionen calculate_score

class Display:
    def __init__(self) -> None:
        self.reveal: bool = False # en boolean värde som anger om hela delarens hand visas

    # metoden som styr vad som visas på konsolen
    def display(self, player: Player, dealer: Dealer):
        # visar spelarens och delarens nuvarande händer och poäng
        print('\nNuvarande kort: ')

        # visar spelarens nuvarande hand och använder calculate_score funktionen för att räkna score för spelaren
        print(f'Spelarens hand: {player.player_hand} score: {calculate_score(player.player_hand)}')

        # om boolean värdet är "True" visas hela handen
        if self.reveal:
            print(f'Delarens hand: {dealer.dealer_hand}, score: {calculate_score(dealer.dealer_hand)}')

        # annars visas bara första kortet
        else:
            print(f'Delarens hand: {dealer.dealer_hand[0]}, [***], score: [***]')

    # metod som sätter boolean värdet till true, kallas till när handen ska visas
    def turn_reveal_true(self):
        self.reveal = True