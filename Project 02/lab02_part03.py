"""
    Class: EE 381 - Section 13
    Project 02 - Binomial Coefficient _Part 03
"""
import numpy as np
import random

#Function
"""
    Find the probability that the player win the lottery
        (player choose 4 numbers from a sequence of 1 through 20 and
            these numbers have to match with 4 random balls are drawn)

    Input: N (The number of experiments)
    Output: The probability
"""
def winLotteryGame(N):
    count = 0 #count the number of experiments that meet the requirement
    S = range(1, 21) # create a sample space - a sequence of numbers from 1 to 20
    for i in range(0, N): #for each experiment
        # the player picks 4 numbers from 1 to 20
        numbers = random.sample(S, 4)
        # 4 balls are drawn at random from a box containing 20 balls numbered 1 through 20
        balls = random.sample(S, 4)

        numbers.sort()
        balls.sort()

        # if get 4 matches => the player win the lottery game => increase count
        if (numbers[0] == balls[0] and numbers[1] == balls[1] and numbers[2] == balls[2] and numbers[3] == balls[3]):
            count += 1
        #print(numbers)
        #print(balls)
        #print(count)
            
    print("The probability that the player win the lottery is:", count/N)

#Main
if __name__ == "__main__":
    winLotteryGame(10000000)
