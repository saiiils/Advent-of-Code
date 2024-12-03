# Advent of Code 2024
# Day 3: Mull It Over

# regex mul\([0-9]+,[0-9]+\)

import re

file = open("2024/inputs/input_day3", "r")

pattern = r'\bmul\([0-9]+,[0-9]+\)\b'
mults = re.findall(pattern, file.read())

file.close()

print(mults)

for pair in mults:
    