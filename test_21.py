from test_player import Player
from test_dealer import Dealer
from test_display import display
from test_logo import logo
from test_score import calculate_score

def main():
    logo()

    player = Player()
    dealer = Dealer()

    player.player_draws()
    player.player_draws()
    dealer.dealer_draws()
    dealer.dealer_draws()
    while True:
        display(player, dealer)

        if calculate_score(player.player_hand) > 21:
            print('Spelaren har gått över 21. Delaren vinner!')
            return

        choice = input('Vill du ha ett till kort? (J/N): ')

        while choice.lower() not in ['j', 'n']:
            choice = input('Ogiltig inmatning, försök igen: ')
        if choice.lower() == 'j':
            player.player_draws()
        elif choice.lower() == 'n':
            break

    while calculate_score(dealer.dealer_hand) < 17:
        dealer.dealer_draws()
        display(player, dealer)

        if calculate_score(dealer.dealer_hand) > 21:
            print('Delaren gick över 21. Spelaren vinner!')
            return
        
    player_score = calculate_score(player.player_hand)
    dealer_score = calculate_score(dealer.dealer_hand)

    if player_score > dealer_score:
        print('Spelaren fick mindre än Delaren. Delaren vinner!!') # spelaren vinner om de har mer poäng
    elif dealer_score > player_score:
        print('Spelaren fick mindre än Delaren. Delaren vinner!') # delaren vinner om de har mer poäng
    else:
        print("Det är oavgjort. Delaren vinner!") # delaren vinner på en oavgjort

def play_again():
    while True:
        main() # spela en ny omgång
        again = input('Vill du spela igen? (J/N): ')
        if again.lower() not in ['j', 'n']:
            again = input('Ogiltit inmatning. Försök igen (J/N): ') # felinmatnings hantering
        elif again.lower() != 'j':
            print('Tack för att du spelade!') # avslutar spelet om man inte vill spela längren
            break

if __name__ == "__main__":
    play_again()