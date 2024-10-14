# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards and discard piles
deck = [(suit,rank) for suit in suits for rank in ranks]
pile1 = 0
pile2 = 0
# Shuffle the deck 

random.shuffle(deck)

# Split the deck into two hands
player1_hand, player2_hand = deck[:26], deck[26:]
def card_comparison(p1_card, p2_card):
    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here
    if ranks.index(p1_card[1]) > ranks.index(p2_card[1]):
        print("P1 BEATS!!! P2")
        return 1
    elif ranks.index(p1_card[1]) < ranks.index(p2_card[1]):
        print("P2 BEATS!!! P2")
        return 2
    return 0
def play_round(player1_hand, player2_hand):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here
    
def war(player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    
def play_game():
    """Main function to run the game."""
    # Your code here
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_card, p2_card = player1_hand.pop(0), player2_hand.pop(0)
        result = card_comparaison(p1_card, p2_card)
        if result == 1:
		pile1 +=2
	elif result == 2:
		pile2 += 2
	elif not(result):
		war(player1_hand, player2_hand)
				
# Call the main function to start the game
play_game()

