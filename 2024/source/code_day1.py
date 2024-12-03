# Advent of Code 2024
# Day 1: Historian Hysteria

file = open("2024/inputs/input_day1", "r")
data = file.readlines()
file.close()

firstNums = []
secondNums = []
diffNums = []
simScore = 0

for line in data:
    numbers = [int(word) for word in line.split() if word.isdigit()]
    firstNums.append(numbers[0])
    secondNums.append(numbers[1])

for num in firstNums:
    simScore += num * secondNums.count(num)

firstNums.sort()
secondNums.sort()

for first, second in zip(firstNums, secondNums):
    diffNums.append(abs(first - second))

print("Total distance: ", sum(diffNums))
print("Similarity score: ", simScore)