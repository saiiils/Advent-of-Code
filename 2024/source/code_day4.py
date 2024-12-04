# Advent of Code 2024
# Day 4: Ceres Search

with open("2024/inputs/input_day4", "r") as file:
    data = [[(c) for c in line.rstrip()] for line in file]

def validCoord(x, y, xSize, ySize):
    return 0 <= x < xSize and 0 <= y < ySize

# part one done. revist for a recursive solution?
def wordSearch(grid, word):

    count = 0

    firstChar = word[0]
    # lastChar = word[len(word) - 1]
    wordLength = len(word)

    yLen = len(grid)                                    # height of array
    xLen = len(grid[0])                                 # width of array

    # directions = [(0, 1), (1, 0), (-1, 1), (1, 1)]      # right, down, up right, down right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),     # U, D, L, R
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]   # UL, UR, DL, DR

    for i in range(yLen):
        for j in range(xLen):

            # find XMAS, use all 8 directions
            if grid[i][j] == firstChar:
                # print("found ", firstChar, " at: ", j, " ", i)
                # X found, search right, down, up right, down right
                for yDir, xDir in directions:
                    n = i + yDir
                    m = j + xDir
                    match = True
                    for k in range(1, wordLength):
                        if validCoord(n, m, yLen, xLen) and grid[n][m] == word[k]:
                            match = True
                            # print(grid[n][m], " matches ", word[k])
                            # print("direction: ", xDir, ",", yDir)
                        else:
                            # print("no match")
                            match = False
                            break
                        n += yDir
                        m += xDir
                    if match:
                        # print("XMAS!")
                        count += 1

            # # find SAMX, use with just R D UR DR
            # if grid[i][j] == lastChar:
            #     print("found ", lastChar, " at: ", j, " ", i)
            #     # S found, serach right, down, up right, down right
            #     for yDir, xDir in directions:
            #         n = i + yDir
            #         m = j + xDir
            #         match = True
            #         for k in range(wordLength - 2, -1, -1):
            #             print(k)
            #             # print(word[k])
            #             if validCoord(n, m, yLen, xLen) and grid[n][m] == word[k]:
            #                 match = True
            #                 # print(grid[n][m], " matches ", word[k])
            #                 # print("direction: ", xDir, ",", yDir)
            #             else:
            #                 # print("no match")
            #                 match = False
            #                 break
            #             n += yDir
            #             m += xDir
            #         if match:
            #             # print("XMAS!")
            #             count += 1

    return count

print(wordSearch(data, "XMAS"))

def masSearch(grid):

    count = 0
    
    yLen = len(grid)                            # height of array
    xLen = len(grid[0])                         # width of array

    diagOne = [(-1, -1), (1, 1)]                # UL, DR diagonal
    diagTwo = [(-1, 1), (1, -1)]                # UR, DL diagonal

    directions = [[(-1, -1), (1,1)], [(-1, 1), (1, -1)]]

    # if M found, opposite diag should be S and vice versa

    for i in range(yLen):
        for j in range(xLen):
            if grid[i][j] == 'A':
                # print("A matched: ", i, " ", j)
                diagOneValid = False
                diagTwoValid = False
                mChar = False
                sChar = False
                for yDir, xDir in diagOne:                  # check first diagonal
                    if validCoord(i + yDir, j + xDir, yLen, xLen):
                        testChar = grid[i + yDir][j + xDir]
                        if testChar == 'M':
                            # print("M matched: ", i + yDir, " ", j + xDir)
                            mChar = True
                        elif testChar == 'S':
                            # print("S matched: ", i + yDir, " ", j + xDir)
                            sChar = True
                        else:
                            # print("invalid diag")
                            diagOneValid = False
                            break
                    else:
                        break
                    if mChar and sChar:
                            diagOneValid = True

                mChar = False
                sChar = False
                for yDir, xDir in diagTwo:                  # check second diagonal
                    if validCoord(i + yDir, j + xDir, yLen, xLen):
                        testChar = grid[i + yDir][j + xDir]
                        if testChar == 'M':
                            # print("M matched: ", i + yDir, " ", j + xDir)
                            mChar = True
                        elif testChar == 'S':
                            # print("S matched: ", i + yDir, " ", j + xDir)
                            sChar = True
                        else:
                            # print("invalid diag")
                            diagTwoValid = False
                            break
                    else:
                        break
                    if mChar and sChar:
                            diagTwoValid = True

                if diagOneValid and diagTwoValid:
                    # print("XMAS!")
                    count += 1
    return count

print(masSearch(data))