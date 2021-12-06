def listToBinaryString(list):
    return ''.join(str(x) for x in list)

def getCommonBit(bitlist, pos):
    bits = list(map(lambda a: a[pos], bitlist))

    return "0" if bits.count("0") > bits.count("1") else "1"

def getUncommonBit(bitlist, pos):
    bits = list(map(lambda a: a[pos], bitlist))

    return "1" if bits.count("1") < bits.count("0") else "0"

def reduceByCommonBit(bits, pos = 0):
    bit = getCommonBit(bits, pos)
    bits = list(filter(lambda x: x[pos] == bit, bits))

    if (len(bits) > 1):
        return reduceByCommonBit(bits, pos + 1)
    else:
        return bits[0]

def reduceByUncommonBit(bits, pos = 0):
    bit = getUncommonBit(bits, pos)
    bits = list(filter(lambda x: x[pos] == bit, bits))
    
    if (len(bits) > 1):
        return reduceByUncommonBit(bits, pos + 1)
    else:
        return bits[0]

def partOne():
    with open('input/day3.txt', 'r') as inputFile:
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
    with open('input/day3.txt', 'r') as inputFile:
        lines = inputFile.read().splitlines()

        return [int(reduceByCommonBit(lines), 2), int(reduceByUncommonBit(lines), 2)]

gammaRate, epsilonRate = partOne()
print("Gamma Rate: {}, Epsilon Rate: {}, Power Consumption: {}".format(gammaRate, epsilonRate, gammaRate * epsilonRate))

oxygenGeneratorRating, CO2ScrubberRating = partTwo()
print("Oxygen Scrubber Rating: {}, CO2 Scrubber Rating: {}, Life Support Rating: {}".format(oxygenGeneratorRating, CO2ScrubberRating, oxygenGeneratorRating * CO2ScrubberRating))