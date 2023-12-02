# Advent of Code 2023
# Day 2: Cube Connundrum

import re

file = open("inputs/input_day2.txt", "r")
data = file.readlines()
file.close()

def partOne():

    # the bag of cubes to compare to
    maxRed = 12
    maxGreen = 13
    maxBlue = 14

    # total sum of IDs
    sumID = 0

    for line in data:
        gameValid = True
        gameID = int(re.search(r'\d+', line.split(':')[0]).group())
        # print("game: ", gameID)
        gameData = line.split(':')[1]
        setData = gameData.split(';')
        for set in setData:
            # print("set: ", set)
            colorData = set.split(',')
            for cube in colorData:
                # print(cube)
                cubeColor = re.search(r'red|green|blue', cube).group()
                if (cubeColor == 'red'):
                    cubeNum = int(re.search(r'\d+', cube).group())
                    if (cubeNum > maxRed):
                        gameValid = False
                        # print("game invalid. red: ", cubeNum, " exceeds max red: ", maxRed)
                        break
                if (cubeColor == 'green'):
                    cubeNum = int(re.search(r'\d+', cube).group())
                    if (cubeNum > maxGreen):
                        gameValid = False
                        # print("game invalid. green: ", cubeNum, " exceeds max green: ", maxGreen)
                        break
                if (cubeColor == 'blue'):
                    cubeNum = int(re.search(r'\d+', cube).group())
                    if (cubeNum > maxBlue):
                        gameValid = False
                        # print("game invalid. blue: ", cubeNum, " exceeds max blue: ", maxBlue)
                        break
            if not gameValid:
                # print("break out early")
                break
        if gameValid:
            sumID = sumID + gameID
            # print("this game is valid, the ID has been added to the sum...")
        print("sum of IDs: ", sumID)

def partTwo():
    power = 0

    for line in data:
        gameID = int(re.search(r'\d+', line.split(':')[0]).group())
        # print("game: ", gameID)
        minRed = 0
        minGreen = 0
        minBlue = 0
        gameData = line.split(':')[1]
        setData = gameData.split(';')
        for set in setData:
            # print("set: ", set)
            colorData = set.split(',')
            for cube in colorData:
                # print(cube)
                cubeColor = re.search(r'red|green|blue', cube).group()
                if (cubeColor == 'red'):
                    cubeNum = int(re.search(r'\d+', cube).group())
                    if (cubeNum > minRed):
                        minRed = cubeNum
                        # print("new red minium found: ", minRed)
                if (cubeColor == 'green'):
                    cubeNum = int(re.search(r'\d+', cube).group())
                    if (cubeNum > minGreen):
                        minGreen = cubeNum
                        # print("new green minium found: ", minGreen)
                if (cubeColor == 'blue'):
                    cubeNum = int(re.search(r'\d+', cube).group())
                    if (cubeNum > minBlue):
                        minBlue = cubeNum
                        # print("new blue minium found: ", minBlue)
        # print("min set: ", minRed, minGreen, minBlue)
        print("\n\n")
        power = power + (minRed * minGreen * minBlue)
    print("power: ", power)

partOne()
partTwo()