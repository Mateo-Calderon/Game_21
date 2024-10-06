from Player_class import Player # importerar klassen Player
from Dealer_class import Dealer # importerar klassen Dealer
from Display_class import Display # importerar klassen Display
from Logo_clas import logo # importerar funktionen logo
from Score_class import calculate_score # importerar funktionen calculate_score

# main funktionen
def main() -> None:
    logo()# visar logan för spelet

    player = Player() # skapar en instansvaribel för klassen Player
    dealer = Dealer() # skapar en instansvaribel för klassen Dealer
    display = Display() # skapar en instansvariabel för klassen display

    player.player_draws() # metod för spelaren att dra ett kort
    player.player_draws() # metod för spelaren att dra ett kort
    dealer.dealer_draws() # metod för delaren att dra ett kort

    # spelarens tur
    while True:
        # visar spelarens och delarens kort och score(gömmer dealerns andra kort och score i början)
        display.display(player, dealer) 

        if calculate_score(player.player_hand) > 21: # om spelarens hand går över 21
            print('Spelaren har gått över 21. Delaren vinner!') # skriver ut meddelande om man går över 21
            return # Avslutar spelet om spelarens poäng är över 21

        choice: str = input('Vill du ha ett till kort? (J/N): ') # Input från användaren, returnerar en sträng
        
        # while loop som felhanterar ogiltigt inmatningar
        while choice.lower() not in ['j', 'n']: 
            choice = input('Ogiltig inmatning, försök igen: ')

        if choice.lower() == 'j': # om spelaren vill ha ett till kort
            player.player_draws() # drar ett till kort
        elif choice.lower() == 'n': # om spelaren svarar nej
            break # avslutar loopen

    # Delarens tur: drar kort tills summan är minst 17
    while calculate_score(dealer.dealer_hand) < 17: # kallar calculate_score funktionen som räknar score från delarens hand
        dealer.dealer_draws() # drar ett kort åt delaren
        display.turn_reveal_true() # kallar funktionen som visar delarens hand
        display.display(player, dealer) # visar aktuellt spel händer

        # håller koll om delaren gick över 21
        if calculate_score(dealer.dealer_hand) > 21: 
            print('Delaren gick över 21. Spelaren vinner!') # skriver att spelarens har vunnit
            return # avslutar spelet
     
    # beräknar slut poäng för spelaren och delaren
    player_score: int = calculate_score(player.player_hand) 
    dealer_score: int = calculate_score(dealer.dealer_hand)

    # jämför poäng mellan spelaren och delaren
    if player_score > dealer_score:
        print('Spelaren fick mer än Delaren. Spelaren vinner!!') # spelaren vinner om de har mer poäng
    elif dealer_score > player_score:
        print('Spelaren fick mindre än Delaren. Delaren vinner!') # delaren vinner om de har mer poäng
    else:
        print("Det är oavgjort. Delaren vinner!") # delaren vinner på en oavgjort

def play_again():
    while True:
        main() # spelar en ny omgång
        again: str = input('Vill du spela igen? (J/N): ')

        # hanterar felinmatning
        if again.lower() not in ['j', 'n']:
            again = input('Ogiltit inmatning. Försök igen (J/N): ')

        # om spelaren inte vill spela igen avslutar spelet
        elif again.lower() != 'j':
            print('Tack för att du spelade!') # tackmeddelande
            break # avslutar spelet

 # kör spelet om skriptet körs direkt
if __name__ == "__main__":
    play_again() # startar spelet