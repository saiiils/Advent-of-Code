# Advent of Code 2024
# Day 3: Mull It Over

# regex mul\([0-9]+,[0-9]+\)

import re

file = open("2024/inputs/input_day3", "r")

pattern = r'mul\([0-9]+,[0-9]+\)'

mults = re.split("(do\(\)|don't\(\))", file.read())

file.close()

multEnable = True
sum = 0

for split in mults:

    if split == "do()":
        multEnable = True
    elif split == "don't()":
        multEnable = False
    else:
        print("doing math")

    if multEnable:
        mults = re.findall(pattern, split)
        for mul in mults:
            numbers = list(map(int, re.findall(r'\d+', mul)))
            sum += numbers[0] * numbers[1]

# mults = re.findall(pattern, file.read())

# for pair in mults:
#     numbers = list(map(int, re.findall(r'\d+', pair)))
#     sum += numbers[0] * numbers[1]
    
print(sum)