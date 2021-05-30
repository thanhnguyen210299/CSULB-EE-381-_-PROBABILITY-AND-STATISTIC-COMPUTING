"""
    Class: EE 381 - Section 13
    Project 01 - Random Number Experiments _Part 03
"""
import numpy as np

#Function
"""
    Find the probability of getting 35 heads when tossing 100 coins

    Input: N (The number of experiments), numberOfCoins = 100, numberOfHeads = 35
    Output: The probability
"""
def tossTheCoins(N, numberOfCoins, numberOfHeads):
    count = 0 # count the number of experiments which have 35 heads
    for i in range(0, N): #for each experience
        #create an array that contains the results after tossing 100 coins
        sideOfCoins = np.random.randint(0, 2, numberOfCoins) #0 is tail and 1 is head
        #count the number of heads
        heads = sum(sideOfCoins)

        #if the number of heads equals to 35 => increase count
        if (heads == numberOfHeads):
            count += 1

    print('The probability of getting', numberOfHeads, 'heads when tossing', numberOfCoins, 'coins is: ', count / N)

#Main
if __name__ == "__main__":
    tossTheCoins(100000, 100, 35)
