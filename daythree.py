def listToBinaryString(list):
    return ''.join(str(x) for x in list)

def getCommonBit(bitlist, pos):
    bits = list(map(lambda a: a[pos], bitlist))

    return "0" if bits.count("0") > bits.count("1") else "1"

def getUncommonBit(bitlist, pos):
    bits = list(map(lambda a: a[pos], bitlist))

    return "1" if bits.count("1") < bits.count("0") else "0"

def filterByBit(list, bit, pos):
    filtered = []

    for item in list:
        if (item[pos] == bit):
            filtered.append(item)

    return filtered

def reduceByCommonBit(list, pos = 0):
    bit = getCommonBit(list, pos)
    list = filterByBit(list, bit, pos)

    if (len(list) > 1):
        return reduceByCommonBit(list, pos + 1)
    else:
        return list[0]

def reduceByUncommonBit(list, pos = 0):
    bit = getUncommonBit(list, pos)
    list = filterByBit(list, bit, pos)
    
    if (len(list) > 1):
        return reduceByUncommonBit(list, pos + 1)
    else:
        return list[0]

def partOne():
    with open('input/daythree.txt', 'r') as inputFile:
        lines = inputFile.read().splitlines()
        byteLen = len(lines[0])
        totalLines = len(lines)
        totals = [0 for _ in range(0, byteLen)]

        for line in lines:
            bits = list(line)
            for i, bit in enumerate(bits):
                if bit == "1":
                    totals[i] += 1

        for i, num in enumerate(totals):
            if num > (totalLines / 2):
                totals[i] = 1
            else:
                totals[i] = 0

        gammaRate = int(listToBinaryString(totals), 2)
        epsilonRate = gammaRate ^ ((2 ** byteLen) - 1)

    return gammaRate, epsilonRate

def partTwo():
    with open('input/daythree.txt', 'r') as inputFile:
        lines = inputFile.read().splitlines()

        return [int(reduceByCommonBit(lines), 2), int(reduceByUncommonBit(lines), 2)]

gammaRate, epsilonRate = partOne()
print("Gamma Rate: {}, Epsilon Rate: {}, Power Consumption: {}".format(gammaRate, epsilonRate, gammaRate * epsilonRate))

oxygenGeneratorRating, CO2ScrubberRating = partTwo()
print("Oxygen Scrubber Rating: {}, CO2 Scrubber Rating: {}, Life Support Rating: {}".format(oxygenGeneratorRating, CO2ScrubberRating, oxygenGeneratorRating * CO2ScrubberRating))