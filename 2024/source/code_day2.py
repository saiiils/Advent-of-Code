# Advent of Code 2024
# Day 2: Red-Nosed Reports

import re
import numpy

file = open("2024/inputs/input_day2", "r")
data = file.readlines()
file.close()

safeReports = 0

def checkOrder(nums):
    sortNums = nums[:]
    sortNums.sort()
    revSortNums = sortNums[::-1]

    if nums == sortNums:
        # print("forward: ", nums)
        return True
    elif nums == revSortNums:
        # print("reverse: ", nums)
        return True
    else:
        # print("not sorted")
        return False

def checkDiff(nums):
    diffs = numpy.diff(nums)
    # print(diffs)
    safety = False
    for i in diffs:
        if 1 <= abs(i) <= 3:
            # print("good diffs: ", diffs)
            # print(i)
            safety = True
        else:
            safety = False
            break
    # if not safety:
    #     print("bad diffs: ", diffs)

    return safety

def sublists(nums):
    n = len(nums)
    sublists = []

    for i in range(n):
        appendList = nums[:]
        appendList.pop(i)
        sublists.append(appendList)

    # print(sublists)
    return sublists

def checkSafety(nums):
    return checkOrder(nums) and checkDiff(nums)

def problemDampener(subLists):
    print("hello")

for line in data:
    numbers = [int(word) for word in line.split() if word.isdigit()]
    sublist = sublists(numbers)

    subSafety = False
    for sub in sublist:
        if checkSafety(sub):
            subSafety = True

    if checkSafety(numbers) or subSafety:
        # print("safe report")
        safeReports += 1
    # else:
    #     print("unsafe report")
    #     None

    # print("\n")

print(safeReports)