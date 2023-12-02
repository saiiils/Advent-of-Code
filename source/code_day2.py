# Advent of Code 2023
# Day 2: Cube Connundrum

import re

file = open("inputs/input_day2.txt", "r")
data = file.readlines()
file.close()

# the bag of cubes to compare to
maxRed = 12
maxGreen = 13
maxBlue = 14

# total sum of IDs
sumID = 0

# part one
for line in data:
    gameValid = True
    gameID = int(re.search(r'\d+', line.split(':')[0]).group())
    print("Game: ", gameID)
    gameData = line.split(':')[1]
    setData = gameData.split(';')
    for set in setData:
        print("Set: ", set)
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
    print(sumID)