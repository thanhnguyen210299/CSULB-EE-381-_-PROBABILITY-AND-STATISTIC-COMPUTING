"""
    Class: EE 381 - Section 13
    Project 01 - Random Number Experiments _Part 02
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#Function
"""
    Simulate the roll of six sides of an unfair die follow the required probabilities

    Input:
        p = [0.1, 0.15, 0.3, 0.25, 0.05, 0.15] (The required probabilities for each side)
        N (The number of Experiments)
    Output: None
"""
def rollAnUnfairDie(p, N):
    #Randomize result for each experiment
    result = []
    sides = len(p) # the number of sides of the die
    cs = np.cumsum(p) # the cumulative sum of the elements along a given axis
    cp = np.append(0, cs) # cp = [0 0.1 0.25 0.55 0.8 0.85 1]

    for i in range(0, N): #for each experience
        # generate the random number between 0 and 1
        r = np.random.rand()
        # check which range r is falling in [0, 0.1), or [0.1, 0.25),...
        for j in range(0, sides):
            if (r >= cp[j] and r < cp[j+1]):
                # get the number on the right (the bigger one)
                temp = j + 1
        # add the result into the list
        result.append(temp)
    
    #Stem plot graphing
    b = range(1, max(result) + 2)
    sb = np.size(b)
    h, bin_edges = np.histogram(result, bins = b)
    b1 = bin_edges[0: sb - 1]
    plt.close('all')
    
    #Generate plot
    #First figure
    fig1 = plt.figure(1)
    plt.stem(b1, h)
    plt.title('Stem plot - An unfair six-sided die')
    plt.xlabel('Side of a dice')
    plt.ylabel('Number of occurrences')
    fig1.show()
    fig1.savefig('Lab01-2_UnfairSixSidedDice.jpg')
    
    #Second figure
    fig2 = plt.figure(2)
    p = h / N
    plt.stem(b1, p)
    plt.title('Stem plot - An unfair six-sided die: Probability mass function')
    plt.xlabel('Side of a dice')
    plt.ylabel('Probability')
    fig2.show()
    fig2.savefig('Lab01-1_PMF of UnfairSixSidedDice.jpg')
    

#Main
if __name__ == "__main__":
    rollAnUnfairDie([0.1, 0.15, 0.3, 0.25, 0.05, 0.15], 10000)
