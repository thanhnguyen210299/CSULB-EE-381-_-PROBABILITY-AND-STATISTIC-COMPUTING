"""
    Class: EE 381 - Section 13
    Project 01 - Random Number Experiments _Part 04
"""
import random

"""
    Problem: 
    Determine the probability of “4 of a kind” in a 6-card poker draw.
    
    
    Background: 
    A deck of cards contains 52 cards. They are divided into four suits: 
    spades, diamonds, clubs and hearts. Each suit has 13 cards: ace through 10, 
    and three picture cards: Jack, Queen, and King.
    
    A '4 of a kind' or a 'quad' is a hand that contains four cards of one rank, 
    such as 9♣ 9♠ 9♦ 9♥ ('four of a kind, nines').
    
    
    Solution:
"""

DeckOfCards = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
               '2♦', '3♦', '4♦', '5♦', '6♦','7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
               '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥','Q♥', 'K♥', 'A♥',
               '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']

def fourOfAKind(N):
    count = 0
    for i in range(0, N):
        MyDraw = random.sample(DeckOfCards, 6)
        MyDraw.sort()

        if (MyDraw[0][0] == MyDraw[3][0]) or (MyDraw[2][0] == MyDraw[5][0]) or (MyDraw[1][0] == MyDraw[4][0]):
            count += 1

    print("The probability of getting a 4 of a kind when in a 6-card poker draw is ", count/N)

fourOfAKind(10000000)
