"""
    Class: EE 381 - Section 13
    Project 02 - Binomial Coefficient _Part 01
"""

import random

"""
    A certain population consists of N=1000 people. 500 of them support party A; 300 of them
    support party B; and 200 support party C. A group of 4 people is chosen at random from the
    population. What is the probability that all persons in the group support of party A, party B,
    and party C.
"""


def findFourPeopleParty():

    fourPeople = random.sample(range(1, 1001), 4)
    fourPeopleParty = []

    for position in range(len(fourPeople)):
        if 1 <= fourPeople[position] <= 500:
            fourPeopleParty.append('A')
        elif 501 <= fourPeople[position] <= 800:
            fourPeopleParty.append('B')
        elif 801 <= fourPeople[position] <= 1000:
            fourPeopleParty.append('C')

    return fourPeopleParty


def allPersonsInGroup(N):

    countA = 0
    countB = 0
    countC = 0

    for i in range(0, N):

        fourPeopleParty = findFourPeopleParty()

        if fourPeopleParty[0] == 'A' and fourPeopleParty[1] == 'A' and fourPeopleParty[2] == 'A' and fourPeopleParty[3] == 'A':
            countA += 1
        elif fourPeopleParty[0] == 'B' and fourPeopleParty[1] == 'B' and fourPeopleParty[2] == 'B' and fourPeopleParty[3] == 'B':
            countB += 1
        elif fourPeopleParty[0] == 'C' and fourPeopleParty[1] == 'C' and fourPeopleParty[2] == 'C' and fourPeopleParty[3] == 'C':
            countC += 1

    print("The probability that all persons in the group support part A is ", countA / N)
    print("The probability that all persons in the group support part B is ", countB / N)
    print("The probability that all persons in the group support part C is ", countC / N)


allPersonsInGroup(10000000)
