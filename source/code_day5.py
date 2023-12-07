# Advent of Code 2023
# Day 5: If You Give A Seed A Fertilizer

import re

file = open("inputs/input_day5", "r")
data = file.read().split("\n\n")
file.close()

# 0: seeds
# 1: seed to soil
# 2: soil to fertilizer
# 3: fertilizer to water
# 4: water to light
# 5: light to temp
# 6: temp to humid
# 7: humid to loc

def partOne():

    # way of pulling nums from a string without using regex
    # map(function, iterable)
    # list(map(int,data[0].split(":")[1].strip().split()))
    # from inside to out:
    # get data[0] aka seeds line, split at ':' and get the second string which holds the numbers.
    # strip the whitespace from the top and tail, then split by word aka numbers.
    # turn those string numbers into int, then put it into a list.
    seeds = list(map(int,data[0].split(":")[1].strip().split()))

    mapMappings = {}

    # get data following seeds, maps
    for maps in data[1:]:

        mapData = maps.splitlines()

        # first split breaks off map: word, next split breaks "seed"-to-"soil"
        # ends up with: ['seed', 'soil'], ['soil', 'fertilizer'], etc.
        mapType = tuple(mapData[0].split()[0].split("-to-"))
        mapMappings[mapType] = []

        for line in mapData[1:]:
            mapMappings[mapType].append(list(map(int,line.split())))


partOne()