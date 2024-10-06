from test_player import Player
from test_dealer import Dealer
from test_score import calculate_score

def display(player: Player, dealer: Dealer):
    reveal_dealer = False
    if calculate_score(dealer.dealer_hand) > 17:
        reveal_dealer = True

    print('\nNuvarande kort: ')
    print(f'{player.player_hand} score: {calculate_score(player.player_hand)}')
    if reveal_dealer:
        print(f'{dealer.dealer_hand}, score: {calculate_score(dealer.dealer_hand)}')
    else:
        print(f'{dealer.dealer_hand[0]}, [***], score: [***]')