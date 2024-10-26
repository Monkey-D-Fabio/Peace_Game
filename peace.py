# Import necessary modules
import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")

# Create a deck of cards and discard piles
deck = [(suit,rank) for suit in suits for rank in ranks]
pile1 = []
pile2 = []
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
        return 1
    elif ranks.index(p1_card[1]) < ranks.index(p2_card[1]):
        return 2
    return 0
def play_round(result, p1_card, p2_card, pile1, pile2):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here
    print(f"P1 played {p1_card}")
    print(f"P2 played {p2_card}")
    if result == 1:
    	print("P1 BEATS!!! P2")
    	pile1.append(p1_card)
    	pile1.append(p2_card)
    elif result == 2:
    	print("P2 BEATS!!! P1")
    	pile2.append(p1_card)
    	pile2.append(p2_card)
    else:
    	print("WAAAAAAARRRRR")
    	#pile2.append(p1_card)
    	#pile2.append(p2_card)
    	war(p1_card, p2_card, player1_hand, player2_hand)
def war(p1_card, p2_card, player1_hand, player2_hand):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    war_extra_cards = []
    while ranks.index(p1_card[1]) == ranks.index(p2_card[1]):
        cards1_left = 4
        cards2_left = 4
        if len(player1_hand) < 4:
    	    cards1_left = 4 - len(player1_hand)
    	    war_extra_cards += player1_hand
    	    player1_hand = pile1
    	    random.shuffle(player1_hand)
        if len(player2_hand) < 4:
    	    cards2_left = 4 - len(player2_hand)
    	    war_extra_cards += player2_hand
    	    player2_hand = pile2
    	    random.shuffle(player2_hand)
        print(war_extra_cards)
        for i in range(cards1_left):
            if i + 1 == cards1_left:
                p1_card = player1_hand.pop(0)
                war_extra_cards.append(p1_card)
                
            else:
                print(player1_hand)
                war_extra_cards.append(player1_hand.pop(0))
        for i in range(cards2_left):
            if i + 1 == cards2_left:
                p2_card = player2_hand.pop(0)
                war_extra_cards.append(p2_card)
                
            else:
                print(player2_hand)
                war_extra_cards.append(player2_hand.pop(0))
    result= card_comparison(p1_card, p2_card)
    play_round(result, p1_card, p2_card, pile1, pile2)
    
            
        
def play_game(player1_hand, player2_hand, pile1, pile2):
    """Main function to run the game."""
    # Your code here
    while len(player1_hand) > 0 and len(player2_hand) > 0:
        p1_card, p2_card = player1_hand.pop(0), player2_hand.pop(0)
        result = card_comparison(p1_card, p2_card)
        play_round(result, p1_card, p2_card, pile1, pile2)
        if len(player1_hand) == 0 or len(player2_hand) == 0:
    	    player1_hand = pile1
    	    pile1 = []
    	    random.shuffle(player1_hand)
    	    player2_hand = pile2
    	    pile2 = []
    	    random.shuffle(player2_hand)
    	    print("Reshuffled")
    if not(player1_hand):
        print("P2's victory")
    else:
        print("P1's victory")
		
# Call the main function to start the game
play_game(player1_hand, player2_hand, pile1, pile2) 
