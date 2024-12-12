import time
import random
ranks = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")
deck = [(suit, rank) for suit in suits for rank in ranks]
random.shuffle(deck)
deck1 = deck[:len(deck)//2]
deck2 = deck[len(deck)//2:]
def card_compare(p1_card, p2_card):
    if ranks.index(p1_card[1]) > ranks.index(p2_card[1]):
        return 1
    elif ranks.index(p1_card[1]) < ranks.index(p2_card[1]):
        return 2
    else:
        return 0
def play_round(player1_hand, player2_hand):
    p1_card = player1_hand.pop(0)
    p2_card = player2_hand.pop(0)
    print(f"Player 1 put down {p1_card} and Player 2 put down {p2_card}")
    result = card_compare(p1_card, p2_card)
    if result == 1:
        print("Player 1 wins this round\n")
        player1_hand.append(p1_card)
        player1_hand.append(p2_card)
    elif result == 2:
        print("Player 2 wins this round\n")
        player2_hand.append(p1_card)
        player2_hand.append(p2_card)
    else:
        print("WAR")
        WAR(player1_hand, player2_hand)
def WAR(player1_hand, player2_hand):
    while len(player1_hand) > 4 and len(player2_hand) > 4:
        p1_war_cards = [player1_hand.pop(0) for _ in range(4)]
        p2_war_cards = [player2_hand.pop(0) for _ in range(4)]
        print(f"Player 1 put down {p1_war_cards[:-1]} and show {p1_war_cards[-1]}\n")
        print(f"Player 2 put down {p2_war_cards[:-1]} and show {p2_war_cards[-1]}\n")
        result_WAR = card_compare(p1_war_cards[-1], p2_war_cards[-1])
        if result_WAR == 1:
            print("Player 1 wins war and gets all the cards!\n")
            player1_hand.extend(p1_war_cards + p2_war_cards)
            return
        elif result_WAR == 2:
            print("Player 2 wins war and gets all the cards!\n")
            player2_hand.extend(p1_war_cards + p2_war_cards)
            return
        else:
            print("Another tie, go to war again!\n")
def game_loop(player1_hand, player2_hand):
    while len(player1_hand) > 0 and len(player2_hand) > 0:
        play_round(player1_hand, player2_hand)
        
def play_game(player1_hand, player2_hand):
    game_loop(player1_hand, player2_hand)
    if len(player1_hand) == 0:
        print("Player 2 wins")
    else:
        print("Player 1 wins")
play_game(deck1, deck2)
