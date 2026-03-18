# Creators
Alfie Harrison - BSc Financial Mathematics
Ben Griffiths-Johnson - BSc Financial Mathematics
Max Aira - BSc Financial Mathematics
Sean Howell - BSc Financial Mathematics


# Blackjack

Below you will find the tutorial and how to section, as well as clear explanations and references to our Blackjack project

## Tutorial

In this tutorial we will see how our Blackjack project was coded, showing our thought processes with detailed explanations of each section of code

To play a game of Blackjack, you need a deck of cards. Therefore, the appropriate library/s must be imported.

import random

def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10]*4 + ['J', 'Q', 'K', 'A']*4

Essentially, we have defined our deck and what it consists of, and imported random, which is the library used later in the code to allow the randomness of the cards dealt.

Next, the cards are dealt and the hands are calculated by the following code

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

The hands are dealt, and the code has to be written in a particular way to ensure the correct calculation of the players' hand. As displayed, if the player/dealer holds an ace, and the calculation of both cards is greater than 21, the ace is calculated as a 1. On the other hand, it is calculated as 11 if the ace plus the other random card sums to 21 or less. 

Once the player has received both cards, one of the dealers cards are displayed to the player, which helps the player to make a decision on his hand. This small section of code represents this.

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

If the players' hand = 21, the player does not enter the game as they attain a hand called 'Blackjack' which wins/draws the game immediately depending on the dealers' cards. However, if the players' hand is less than 21, the player enters the game and is given a choice to stand (keep remaining cards,) or hit(draw another card.)

The dealers hand is calculated by the following code

def dealer_turn(deck, dealer_hand):
        while calculate_total(dealer_hand) <= 16:
            deal_card(dealer_hand, deck)

After this, the end of the game is calculated, comparing the players hand to the dealers hand

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

Each individual outcome is presented in the code, as well as the writing the player receives depending on the outcome. For example, if they draw cards greater than 21, they will receive "You bust! Dealer wins!"


## How to guides

### How to create a deck of cards

import random

def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10]*4 + ['J', 'Q', 'K', 'A']*4

### How to create a function that deals the cards

def deal_card(hand, deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

 def deal_initial_cards(deck, player_hand, dealer_hand):
        for _ in range(2):
            deal_card(player_hand, deck)
            deal_card(dealer_hand, deck)

### How to create a function that calculates the total of the cards dealt

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
### How to reveal the dealers hand

def reveal_dealer_hand(hand):
        return f"{hand[0]} and X" if len(hand) == 2 else ', '.join(map(str, hand))

### How to add the players and dealers turn into the game
    
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

### How to check for the end of the game
    
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

### How to determine the results of the game

def determine_winner(player_total, dealer_total):
        if 21 - dealer_total < 21 - player_total:
            return "Dealer wins!"
        elif 21 - dealer_total > 21 - player_total:
            return "You win!"
        else:
            return "It's a tie!"

### How to display the results of the game

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

### How to repeat the game

 if __name__ == "__main__":
        while True:
            run_game()
            again = input("Play again? (y/n): ").lower()
            if again != 'y':
                break

## Explanation

### Creating a deck of cards

A deck of cards is needed to play Blackjack. In addition, this deck has to be random. 

import random

def create_deck():
    return [2, 3, 4, 5, 6, 7, 8, 9, 10]*4 + ['J', 'Q', 'K', 'A']*4

The corresponding creates a deck of cards which returns a random card.

### Dealing cards

To play Blackjack, cards must be dealt by the dealer to the player and himself.

def deal_card(hand, deck):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)
    
    def deal_initial_cards(deck, player_hand, dealer_hand):
        for _ in range(2):
            deal_card(player_hand, deck)
            deal_card(dealer_hand, deck)

This enables us to deal cards randomly to ensure the game is fair.

### Calculating the players and dealers hand

Both hands must be calculated to continue the game of Blackjack.

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
    

It is important that the aces are calculated correctly, ensuring that the ace is calculated as '1' or '11' depending on the sum of both cards combined.

### Revealing the dealers hand

One of the dealers' cards is revealed. In Blackjack, this shows the player one of the dealers card, and is used to make a decision on whether they should stick with their current hand or hit and collect another card

def reveal_dealer_hand(hand):
        return f"{hand[0]} and X" if len(hand) == 2 else ', '.join(map(str, hand))

### Can the player play?

The player can play the game if they do not present 21.

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

The player has to make a choice whether to hit or stand depending on the cards they are dealt. If they hit, they risk busting, but if they stand, they risk the dealer beating them with a higher summation of cards. It is also important to state that the dealer automatically does not play if they are dealt cards which sum to 16 or greater.

### The Results

The results are shown after the player decides to hit or stand

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

Each result is dependent on the cards dealt in a specific game


## Reference

### List of Functionality

The following functions are written using the 'random' library

- 'deal_card(hand, deck)'
- 'deal_card(player_hand, deck)'
- 'deal_card(dealer_hand, deck)'
  
In addition, we used the unittest.mock library to test the code

### Bibliography

- https://en.wikipedia.org/wiki/Blackjack
- We used this site to get a general overview of the games rules 
- https://inventwithpython.com/bigbookpython/project4.html
- we used this site to get an idea of writing the game
- https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
- We used this site to implement f-strings into the code 
