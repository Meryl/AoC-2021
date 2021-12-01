increases = 0
decreases = 0

with open('input/dayone.txt', 'r') as inputFile:
    lines = [int(x) for x in inputFile.read().splitlines()]

    for i, line in enumerate(lines):
        if (i > 2):
            if (sum(lines[i - 3 : i]) < sum(lines[i - 2 : i + 1])):
                increases += 1
            else:
                decreases += 1

print("{} increases, {} decreases".format(increases, decreases))