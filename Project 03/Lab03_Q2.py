"""
    Class: EE 381 - Section 13
    Project 03 - Uniform Distribution _Part 02
"""

import numpy as np
import random
from scipy.stats import uniform

"""
    Three points #1, #2, and #3 are selected at random from
    the circumference of a circle. Write Python code to 
    find the probability that the three points lie on the
    same semicircle.
"""


def findThreePoints():

    threePoints = np.random.uniform(0, 360, size = 3)
    threePoints.sort()

    return threePoints

def semiCircleTest(N):

    count = 0

    for i in range(0, N):

        threePoints = findThreePoints()
        temp1 = threePoints[2] - threePoints[0]
        if (temp1 <= 180):
            count += 1
        else:
            temp2 = threePoints[1] - threePoints[0]
            if (temp2 < 180):
                if (360 - temp1 + temp2 < 180):
                    count += 1
            else:
                if (360 - temp2 <= 180):
                    count += 1

    print("The probability that three random points lie on a semi-circle is", count / N)


semiCircleTest(1000000)
