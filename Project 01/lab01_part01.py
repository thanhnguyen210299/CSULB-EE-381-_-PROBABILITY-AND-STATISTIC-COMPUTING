"""
    Class: EE 381 - Section 13
    Project 01 - Random Number Experiments _Part 01
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#Function
"""
    Number of rolls that needs to get a sum of 7 appears when rolling 2 dice

    Input: N (The number of Experiments)
    Output: None
"""
def sumOf2Dice(N):
    result = []
    for i in range(0, N): #for each experiment
        count = 0
        total = 0
        while (total != 7): #roll the 2 dice until get the sum of 7
            count += 1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
        result.append(count - 1) #count - 1 because don't include the total of 7
    #Stem plot graphing
    b = range(0, 40)
    sb = np.size(b)
    h1, bin_edges = np.histogram(result, bins = b)
    b1 = bin_edges[0: sb - 1]
    plt.close('all')
    print(h1[0])
    
    #Generate plot
    #First figure
    fig1 = plt.figure(1)
    plt.stem(b1, h1)
    plt.title('Stem plot - Sum of two dice equal to 7')
    plt.xlabel('Number of rolls')
    plt.ylabel('Number of occurrences')
    fig1.show()
    fig1.savefig('Lab01-1_Sum7OfTwoDice.jpg')
    
    #Second figure
    fig2 = plt.figure(2)
    p1 = h1 / N
    print(p1[0])
    plt.stem(b1, p1)
    plt.title('Stem plot - Sum of two dice equal to 7: Probability mass function')
    plt.xlabel('Number of rolls')
    plt.ylabel('Probability')
    fig2.show()
    fig2.savefig('Lab01-1_PMF of Sum7OfTwoDice.jpg')

#Main
if __name__ == "__main__":
    sumOf2Dice(1000000)
