firstDigit = 0
lastDigit = 0
sumVals = 0

file = open("inputs/input_day1.txt", "r")
data = file.readlines()
file.close()

def digitCombiner(tens, ones):
    calibVal = (tens * 10) + ones
    print(calibVal)
    return calibVal

for line in data:
    # for every line in the text file
    for c in line:
        # for every character in the current line
        if (c.isdigit() and firstDigit == 0):
            firstDigit = int(c)
            print("got first digit: ", firstDigit)
        elif (c.isdigit() and firstDigit != 0):
            lastDigit = int(c)
            print("got new digit: ", lastDigit)
    if (lastDigit == 0):
        lastDigit = firstDigit
        print("only one digit")

    # combine the digits
    sumVals = sumVals + digitCombiner(firstDigit, lastDigit)
    firstDigit = 0
    lastDigit = 0
    print("NEW LINE")
    
print(sumVals)