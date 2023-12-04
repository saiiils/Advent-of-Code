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

file = open("inputs/input_day2.txt", "r")
data = file.readlines()
file.close()

