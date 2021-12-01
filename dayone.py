increases = 0
decreases = 0
prev      = None

# Open the input file, use with so it's closed automatically
with open('input/dayone.txt', 'r') as inputFile:
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

print("{} increases, {} decreases".format(increases, decreases))