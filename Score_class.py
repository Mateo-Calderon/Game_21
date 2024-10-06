# funkton som räknar ut poäng eller värde av spelarens eller delarens hand
def calculate_score(hand: list) -> int :
    score = 0 # initialiserar handens poäng till 0
    aces = 0 # räknar antal ess i handen, initialiserar den till 0

    for card in hand: # loopar genom varje kort i handen
        if card == 1: # om kortet är ess, värdet 1
            score += 14 # behandlar ess som 14 till och början
            aces += 1 # ökar antal ess-räknare
        else:
            score += card # lägger till värdet av andra kort till poäng

    # om totalpoäng är över 21 och det finns ess i handen
    while score > 21 and aces > 0:
        score -= 13 # justerar ess värdet så att det inte överstiger 21
        aces -= 1 # minskar ess-räknare

    return score # returnerar den totalpoäng