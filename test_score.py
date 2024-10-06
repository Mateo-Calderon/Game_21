def calculate_score(hand):
    score = 0
    aces = 0
    for card in hand:
        if card == 1:
            score += 13
            aces += 1
        else:
            score += card
        
    while score > 21 and aces:
        score -= 13
        aces -= 1

    return score