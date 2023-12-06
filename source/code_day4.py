# Advent of Code 2023
# Day 4: Scratchcards

import re

file = open("inputs/input_day4", "r")
data = file.readlines()
file.close()

def partOne():

    sumPoints = 0

    for line in data:

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
                cardMatches += 1

        # if cardMatches == 0:
            # print("no matches?")
            # print(cardMatches)
        if cardMatches > 0:
            cardPoints = pow(2, cardMatches - 1)
            # print(cardMatches)
            # print(cardPoints)
        
        sumPoints += cardPoints
        # print("Current total: ", sumPoints)
        # print('\n\n')
        
    print(sumPoints)

# partOne()

def partTwo():

    # how many copies of each card do i have
    maxCards = len(data)
    cardCopies = [1] * maxCards
    # cardCopies[0] = 1

    for index, line in enumerate(data):

        # if index > 10: break

        cardData = line.split(':')
        cardNumber = int(re.search(r'\d+', cardData[0]).group())

        winningNumbers = re.findall(r'\d+', cardData[1].split('|')[0])
        playerNumbers = re.findall(r'\d+', cardData[1].split('|')[1])

        cardMatches = 0

        for winNum in winningNumbers:
            if winNum in playerNumbers:
                cardMatches += 1

        # for number of copies for current card
        for i in range(cardCopies[index]):
            if cardMatches > 0:
                for matches in range(cardMatches):
                    if (cardNumber + matches < maxCards):
                        # print("adding one to card ", cardNumber + matches + 1, " ... ", matches + 1, " of ", cardMatches)
                        cardCopies[cardNumber + matches] += 1
                    else:
                        # print("card overflow", cardNumber)
                        # input("Press enter to contiue...")
                        break
            else:
                # print("no matches")
                # input("Press enter to contiue...")
                break

        # print(
        #     "Card: ", cardNumber,
        #     "Copies: ", cardCopies[index],
        #     "Matches: ", cardMatches
        #     )
        # print(cardCopies)
        # print('\n')

        # input("Press enter to continue...")

    sumPoints = 0

    for index, line in enumerate(data):

        cardData = line.split(':')
        cardNumber = int(re.search(r'\d+', cardData[0]).group())

        winningNumbers = re.findall(r'\d+', cardData[1].split('|')[0])
        playerNumbers = re.findall(r'\d+', cardData[1].split('|')[1])

        cardTotal = 0
        cardMatches = 0
        cardPoints = 0

        for winNum in winningNumbers:
            if winNum in playerNumbers:
                cardMatches += 1

        if cardMatches > 0:
            cardPoints = pow(2, cardMatches - 1)

        cardTotal = cardPoints * cardCopies[index]

        # for i in range(cardCopies[index]):
        #     # print(cardCopies[index])
        #     cardTotal += cardPoints

        print(
            "Card: ", cardNumber,
            " Copies: ", cardCopies[index],
            " Matches: ", cardMatches,
            " Points: ", cardPoints,
            " Total: ", cardTotal
            )
        # print(cardCopies)
        # print('\n\n')
        
        sumPoints += cardTotal
        
    print(sumPoints)

partTwo()