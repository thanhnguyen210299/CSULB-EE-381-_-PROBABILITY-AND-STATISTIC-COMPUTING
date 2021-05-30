"""
    Class: EE 381 - Section 13
    Project 02 - Binomial Coefficient _Part 02
"""
import numpy as np
import random

#Function
"""
    Find the probability
        of getting a group of students that has an equal number of boys and girls

    Input: N (The number of experiments), n (the number of students equal 4*n)
    Output: The probability
"""
def getEqualBoyGirl(N, n):
    result = 0 #count the number of experiments that meet the requirement
    for i in range(0, N): #for each experiment
        S = range(1, 4*n+1) # create a sequence of numbers from 1 to 4*n
        #create a list of random items of length 2*n from the given string
        #choose 2*n student from a 4*n-student class
        choices = random.sample(S, 2*n) 
        count = 0 # a counter to get the number of boys
        for k in choices:
            if (k <= 2*n): # boy is marked with the number from 1 to 2*n
                count += 1

        # if the group contains an equal number of boys and girls
        # => the number of boys equal n
        if (count == n):
            result += 1
    print("With n =", n, ", the probability that the group contains an equal number of boys and girls is:", result/N)

#Main
if __name__ == "__main__":
    getEqualBoyGirl(100000, 10)
    getEqualBoyGirl(100000, 50)
