from collections import defaultdict

def partOne():
    with open('input/day5.txt', 'r') as inputFile:
        lines = [[[int(num) for num in coord.split(',')] for coord in line.split(' -> ')] for line in inputFile.read().splitlines()]

        map = defaultdict(int)

        for line in list(filter(lambda l: l[0][0] == l[1][0] or l[0][1] == l[1][1], lines)):
            begin = line[0]
            end   = line[1]

            for x in range(min(begin[0], end[0]), max(begin[0], end[0]) + 1):
                for y in range(min(begin[1], end[1]), max(begin[1], end[1]) + 1):
                    map[(x,y)] += 1

        return lines, map

def partTwo(lines, map):
    for line in list(filter(lambda l: l[0][0] != l[1][0] and l[0][1] != l[1][1], lines)):
        if line[0][0] < line[1][0]:
            begin = line[0]
            end   = line[1]
        else:
            begin = line[1]
            end =   line[0]

        if begin[1] < end[1]:
            dir = 1
        else:
            dir = -1

        y = begin[1]
        for x in range(begin[0], end[0] + 1):
            map[(x,y)] += 1
            y += dir

    return map
    

lines, map = partOne()
print(sum(1 for val in map.values() if val > 1))
map = partTwo(lines, map)
print(sum(1 for val in map.values() if val > 1))