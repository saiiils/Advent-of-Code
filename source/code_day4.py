# Advent of Code 2023
# Day 4: Scratchcards

import re

file = open("inputs/input_day4", "r")
input = file.readlines()
file.close()

def partOne():

    sumPoints = 0

    for line in input:

        print(line.split(':')[0])
        # print(line.split(':')[1].split('|'))
        winningNumbers = re.findall(r'\d+', line.split(':')[1].split('|')[0])
        playerNumbers = re.findall(r'\d+', line.split(':')[1].split('|')[1])
        # print(winningNumbers)
        # print(playerNumbers)

        cardPoints = 0
        cardMatches = 0

        for winNum in winningNumbers:
            if winNum in playerNumbers:
                print("match found: ", winNum)
                cardMatches = cardMatches + 1

        if cardMatches == 0:
            print("no matches?")
            print(cardMatches)
        if cardMatches > 0:
            cardPoints = pow(2, cardMatches - 1)
            print(cardMatches)
            print(cardPoints)
        
        sumPoints = sumPoints + cardPoints
        print("Current total: ", sumPoints)
        print('\n\n')
        
    print(sumPoints)

partOne()