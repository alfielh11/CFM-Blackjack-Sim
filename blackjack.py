import random

def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10] * 4 + ['J', 'Q', 'K', 'A'] * 4

def deal_card(hand, deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

def deal_initial_cards(deck, player_hand, dealer_hand):
    for _ in range(2):
        deal_card(player_hand, deck)
        deal_card(dealer_hand, deck)

def calculate_total(hand):
    total = 0
    ace_count = 0

    for card in hand:
        if isinstance(card, int):
            total += card
        elif card in ['J', 'Q', 'K']:
            total += 10
        else:  # Ace
            total += 11
            ace_count += 1

    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total

def reveal_dealer_hand(hand):
    return f"{hand[0]} and X" if len(hand) == 2 else ', '.join(map(str, hand))

def player_turn(deck, player_hand):
    while True:
        print(f"\nYour hand: {player_hand}, total: {calculate_total(player_hand)}")
        move = input("1: Stand\n2: Hit\n")
        if move == '1':
            break
        elif move == '2':
            deal_card(player_hand, deck)
            if calculate_total(player_hand) >= 21:
                break
        else:
            print("Invalid input. Please enter 1 or 2.")

def dealer_turn(deck, dealer_hand):
    while calculate_total(dealer_hand) <= 16:
        deal_card(dealer_hand, deck)

def check_game_end(player_total, dealer_total):
    if player_total == 21:
        return "Blackjack! You win!"
    elif dealer_total == 21:
        return "Blackjack! Dealer wins!"
    elif player_total > 21:
        return "You bust! Dealer wins!"
    elif dealer_total > 21:
        return "Dealer bust! You win!"
    return None

def determine_winner(player_total, dealer_total):
    if 21 - dealer_total < 21 - player_total:
        return "Dealer wins!"
    elif 21 - dealer_total > 21 - player_total:
        return "You win!"
    else:
        return "It's a tie!"

def run_game():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    deal_initial_cards(deck, player_hand, dealer_hand)

    while True:
        print(f"\nDealer has {reveal_dealer_hand(dealer_hand)}")
        player_turn(deck, player_hand)
        dealer_turn(deck, dealer_hand)

        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)

        print(f"\nFinal Hands:")
        print(f"You: {player_hand}, total: {player_total}")
        print(f"Dealer: {dealer_hand}, total: {dealer_total}")

        end_result = check_game_end(player_total, dealer_total)
        if end_result:
            print(end_result)
        else:
            print(determine_winner(player_total, dealer_total))
        break

if __name__ == "__main__":
    while True:
        run_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break
