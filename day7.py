horizontalPositions = []

with open('input/day7.txt', 'r') as inputFile:
    data = list(map(int, inputFile.read().split(',')))

    for position in data:
        horizontalPositions.append(position)

def partOne(costFunction = lambda n: n):
    fuelCosts = []
    for i in range(min(horizontalPositions), max(horizontalPositions) + 1):
        fuelCost = 0
        for position in horizontalPositions:
            fuelCost += int(costFunction(abs(i - position)))
        fuelCosts.append(fuelCost)

    return min(fuelCosts)

def partTwo():
    return partOne(lambda n: ((n ** 2) + n) / 2)

print("Part one: {}".format(partOne(lambda n: n)))
print("Part two: {}".format(partTwo()))