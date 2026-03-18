import unittest
from unittest.mock import patch
import random

from blackjack import (
    create_deck,
    deal_card,
    deal_initial_cards,
    calculate_total,
    reveal_dealer_hand,
    dealer_turn,
    check_game_end,
    determine_winner
)

class TestBlackjackGame(unittest.TestCase):

    def test_create_deck(self):
        deck = create_deck()
        self.assertEqual(len(deck), 52)
        self.assertEqual(deck.count(10), 4)  # Only four 10s (not counting face cards)
        self.assertEqual(deck.count('J'), 4)
        self.assertEqual(deck.count('A'), 4)

    def test_deal_card(self):
        deck = [2, 3, 4]
        hand = []
        deal_card(hand, deck)
        self.assertEqual(len(hand), 1)
        self.assertEqual(len(deck), 2)
        self.assertNotIn(hand[0], deck)

    def test_deal_initial_cards(self):
        deck = create_deck()
        player_hand = []
        dealer_hand = []
        deal_initial_cards(deck, player_hand, dealer_hand)
        self.assertEqual(len(player_hand), 2)
        self.assertEqual(len(dealer_hand), 2)
        self.assertEqual(len(deck), 48)

    def test_calculate_total_no_aces(self):
        self.assertEqual(calculate_total([10, 'Q']), 20)

    def test_calculate_total_with_aces(self):
        self.assertEqual(calculate_total(['A', 9]), 20)
        self.assertEqual(calculate_total(['A', 'A', 8]), 20)
        self.assertEqual(calculate_total(['A', 10, 'A']), 12)

    def test_reveal_dealer_hand(self):
        self.assertEqual(reveal_dealer_hand([4, 'K']), '4 and X')
        self.assertEqual(reveal_dealer_hand([4, 'K', 2]), '4, K, 2')

    def test_dealer_turn_hits_until_17(self):
        deck = [2, 2, 3, 5, 6, 10, 10]  # Controlled deck
        dealer_hand = [2, 3]
        dealer_turn(deck, dealer_hand)
        self.assertGreaterEqual(calculate_total(dealer_hand), 17)

    def test_check_game_end_conditions(self):
        self.assertEqual(check_game_end(21, 18), "Blackjack! You win!")
        self.assertEqual(check_game_end(18, 21), "Blackjack! Dealer wins!")
        self.assertEqual(check_game_end(22, 18), "You bust! Dealer wins!")
        self.assertEqual(check_game_end(18, 22), "Dealer bust! You win!")
        self.assertIsNone(check_game_end(18, 19))  # No end yet

    def test_determine_winner_logic(self):
        self.assertEqual(determine_winner(19, 20), "Dealer wins!")
        self.assertEqual(determine_winner(20, 19), "You win!")
        self.assertEqual(determine_winner(18, 18), "It's a tie!")

if __name__ == '__main__':
    unittest.main()
