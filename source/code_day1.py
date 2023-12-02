# Advent of Code 2023
# Day 1: Trebuchet?!

import re

file = open("inputs/input_day1.txt", "r")
data = file.readlines()
file.close()

firstDigit = 0
lastDigit = 0
sumVals = 0

# if first char is digit, store it, else check for substring, continue

def digitCombiner(tens, ones):
    calibVal = (tens * 10) + ones
    # print(calibVal)
    return calibVal

def textToNum(text):
    if text == "one":
        return 1
    elif text == "two":
        return 2
    elif text == "three":
        return 3
    elif text == "four":
        return 4
    elif text == "five":
        return 5
    elif text == "six":
        return 6
    elif text == "seven":
        return 7
    elif text == "eight":
        return 8
    elif text == "nine":
        return 9

for line in data:
    # for every line in the text file
    # print(line)
    if (firstDigit == 0):
        firstNum = re.search('one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9', line).group()
        if (firstNum.isdigit()):
            firstDigit = int(firstNum)
            print("first digit aquired via digit: ", firstDigit)
        elif (not firstNum.isdigit()):
            firstDigit = textToNum(re.search('one|two|three|four|five|six|seven|eight|nine', firstNum).group())
            print("first digit aquired via word: ", firstDigit)

    revLine = line[::-1]
    # print(revLine)
    lastNum = re.search('eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9', revLine).group()
    if (lastNum.isdigit()):
        lastDigit = int(lastNum)
        print("last digit aquired via digit: ", lastDigit)
    elif (not lastNum.isdigit()):
        lastDigit = textToNum(re.search('eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', lastNum).group()[::-1])
        print("last digit aquired via word: ", lastDigit)
    elif(lastDigit == 0):
        lastDigit = firstDigit
        print("only one digit found: ", firstDigit, lastDigit)

    sumVals = sumVals + digitCombiner(firstDigit, lastDigit)
    # print("digits: ", firstDigit, lastDigit)
    # print("number: ", digitCombiner(firstDigit, lastDigit))
    # print("total: ", sumVals)
    # print("\n")
    firstDigit = 0
    lastDigit = 0

print("grand total: ", sumVals)