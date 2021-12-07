horizontalPositions = []
highest = 0

with open('input/day7.txt', 'r') as inputFile:
    data = list(map(int, inputFile.read().split(',')))

    for position in data:
        highest = highest if highest > position else position
        horizontalPositions.append(position)

def partOne(costFunction = lambda n: n):
    fuelCosts = []
    lowest = False
    for i in range(0, highest + 1):
        fuelCost = 0
        for position in horizontalPositions:
            n = abs(i - position)
            fuelCost += int(costFunction(n))
        lowest = lowest if lowest != False and fuelCost > lowest else fuelCost
        fuelCosts.append(fuelCost)

    return lowest

def partTwo():
    return partOne(lambda n: ((n ** 2) + n) / 2)

print("Part one: {}".format(partOne(lambda n: n)))
print("Part two: {}".format(partTwo()))