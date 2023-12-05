# Advent of Code 2023
# Day 4: Scratchcards

import re

file = open("inputs/input_day4", "r")
input = file.readlines()
file.close()

def partOne():

    sumPoints = 0

    for line in input:

        # print(line.split(':')[0])
        # print(line.split(':')[1].split('|'))
        winningNumbers = re.findall(r'\d+', line.split(':')[1].split('|')[0])
        playerNumbers = re.findall(r'\d+', line.split(':')[1].split('|')[1])
        # print(winningNumbers)
        # print(playerNumbers)

        cardPoints = 0
        cardMatches = 0

        for winNum in winningNumbers:
            if winNum in playerNumbers:
                # print("match found: ", winNum)
                cardMatches = cardMatches + 1

        # if cardMatches == 0:
            # print("no matches?")
            # print(cardMatches)
        if cardMatches > 0:
            cardPoints = pow(2, cardMatches - 1)
            # print(cardMatches)
            # print(cardPoints)
        
        sumPoints = sumPoints + cardPoints
        # print("Current total: ", sumPoints)
        # print('\n\n')
        
    print(sumPoints)

# partOne()

def partTwo():

    sumPoints = 0

    # how many copies of each card do i have
    cardCopies = []
    for i in range(len(input)):
        cardCopies.append(0)
    # first card will always have 1 copy
    cardCopies[0] = 1

    testLoop = 0

    for line in input:

        if testLoop > 5:
            break

        cardData = line.split(':')
        cardNumber = int(re.search(r'\d+', cardData[0]).group())
        # print(cardNumber)
        cardMatches = 0

        winningNumbers = re.findall(r'\d+', cardData[1].split('|')[0])
        playerNumbers = re.findall(r'\d+', cardData[1].split('|')[1])

        for winNum in winningNumbers:
            if winNum in playerNumbers:
                cardMatches = cardMatches + 1

        # print(cardMatches)
        for i in range(cardMatches):
            cardCopies[cardNumber + i + 1] += 1
            pass

        testLoop += 1

partTwo()
