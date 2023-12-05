# Advent of Code 2023
# Day 3: Gear Ratios
#
# The engine schematic (your puzzle input) consists of a visual representation of the engine.
# There are lots of numbers and symbols you don't really understand, but apparently any number
# adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
# (Periods (.) do not count as a symbol.) Of course, the actual engine schematic is much larger.
#
# What is the sum of all of the part numbers in the engine schematic?

import re
from itertools import product

file = open("inputs/input_day3", "r")
input = file.readlines()
file.close()

engineSchematic = [line for line in input if line]

# strange, but start with y
yMax = len(engineSchematic)     # y length of the schematic, aka number of lines in engine schematic
xMax = len(engineSchematic[0])  # x length of the schematic, aka number of elemnts in a line of the engine schematic

def partOne():

    sumPartNums = 0

    # for each line
    for lineIndex, line in enumerate(engineSchematic):

        for numMatch in re.finditer(r'\d+', line):

            # if lineIndex > 1: break
            # get coordinates of all adjacent cells. +2 on right because range is exclusive on right
            partNum = int(numMatch.group())
            yAdj = list(range(lineIndex - 1, lineIndex + 2))
            xAdj = list(range(numMatch.start() - 1, numMatch.end() + 1))
            numStart = numMatch.start()
            numEnd = numMatch.end() - 1

            # cartesian product of adjacent coordinates
            adjCoords = list(product(yAdj, xAdj))

            # get characters of all the adjacent coordinates.
            adjChars = [
                engineSchematic[y][x]
                for y, x in adjCoords
                if y in range(0, yMax) and x in range(0, xMax - 1)
                and (y != lineIndex or x not in range(numStart, numEnd + 1))
            ]

            # check if adjacent characters are not digit or dot
            if any(c for c in adjChars if c not in ".0123456789"):
                sumPartNums = sumPartNums + partNum

            print(partNum)
            print(yAdj)
            print(xAdj)
            print(adjChars)
            print(sumPartNums)
            print('\n\n')

    print("Total: ", sumPartNums)

partOne()
    
def partTwo():

    sumGearRatios = 0

    # go thru each line and char in engineSchematic
    for lineIndex, line in enumerate(engineSchematic):

        # find each gear (aka star)
        for gear in re.finditer(r'\*', engineSchematic[lineIndex]):

            # parts list for each gear
            adjParts = []

            # search adjacent lines
            for adjLineIndex in [-1, 0, 1]:

                # check to make sure we don't go out of bounds
                if (lineIndex + adjLineIndex) in range(0, yMax):
                    for partNum in re.finditer(r'\d+', engineSchematic[lineIndex + adjLineIndex]):
                        # checks if the part is adjacent to the gear
                        if gear.start() in range(partNum.start() - 1, partNum.end() + 1):
                            adjParts.append(int(partNum.group()))
            
            # if exactly two parts are found, add to gear ratio sum
            if len(adjParts) == 2:
                sumGearRatios = sumGearRatios + (adjParts[0] * adjParts[1])
    
    print(sumGearRatios)

partTwo()