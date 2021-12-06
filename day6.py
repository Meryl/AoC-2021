import numpy as np

with open('input/day6.txt', 'r') as inputFile:
    data = list(map(int, inputFile.read().split(',')))

def passTime(fish, days = 1):
    while days > 0:
        days -= 1
        if fish[0] != 0:
            fish[7] += fish[0]

        fish = np.roll(fish, -1)

    return fish

def partOne():
    fish = np.zeros(9)

    for f in data:
        fish[f] += 1
    
    days = 80
    fish = passTime(fish, days)

    print("fish after {} days: {}".format(days, sum(fish)))

def partTwo():
    fish = np.zeros(9)

    for f in data:
        fish[f] += 1

    days = 256
    fish = passTime(fish, days)

    print("fish after {} days: {}".format(days, sum(fish)))

partOne()
partTwo()