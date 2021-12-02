distance = 0
depth = 0

with open('input/daytwo.txt', 'r') as inputFile:
    lines = inputFile.read().splitlines()

    for line in lines:
        cmd, amount = line.split()

        if (cmd == "forward"):
            distance += int(amount)
        elif (cmd == "down"):
            depth += int(amount)
        elif (cmd == "up"):
            depth -= int(amount)

print("Horizontal distance {}, depth {}, multiplied {}".format(distance, depth, distance * depth))