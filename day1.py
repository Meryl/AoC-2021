def partOne():
    increases = 0
    decreases = 0
    prev      = None

    # Open the input file, use with so it's closed automatically
    with open('input/day1.txt', 'r') as inputFile:
        # Split on newlines, then apply int(x) for each line
        lines = [int(x) for x in inputFile.read().splitlines()]

        # enumerate() is used for easy access to the index, basically equivalent
        # to foreach ($list as $i => $line) with $list being an array that is a list
        for i, line in enumerate(lines):
            if (i > 0):
                if (line > prev):
                    increases += 1
                else:
                    decreases += 1

            prev = line

    print("Simple comparison: {} increases, {} decreases".format(increases, decreases))

def partTwo():
    increases = 0
    decreases = 0

    with open('input/day1.txt', 'r') as inputFile:
        lines = [int(x) for x in inputFile.read().splitlines()]

        for i, line in enumerate(lines):
            if (i > 2):
                if (sum(lines[i - 3 : i]) < sum(lines[i - 2 : i + 1])):
                    increases += 1
                else:
                    decreases += 1

    print("Rolling window   : {} increases, {} decreases".format(increases, decreases))

partOne()
partTwo()