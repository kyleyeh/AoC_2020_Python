def partA(lines):
    count = 0
    for line in lines:
        fields = line.split(' ')
        min, max = [int(x) for x in fields[0].split("-")]
        char = fields[1][0:-1]
        if (fields[2].count(char) >= int(min) and fields[2].count(char) <= int(max)):
            count += 1
    return count


def partB(lines):
    count = 0
    for line in lines:
        fields = line.split(' ')
        spot1, spot2 = [int(x) for x in fields[0].split("-")]
        char = fields[1][0:-1]
        inCount = 0
        if (fields[2][spot1-1] == char):
            inCount += 1
        if (fields[2][spot2-1] == char):
            inCount += 1
        count += inCount%2
    return count

def readIntegers(pathToFile):
    with open(pathToFile) as f:
        a = [int(x) for x in f.read().split()]
    return a

def readStrings(pathToFile):
    with open(pathToFile) as f:
        a = f.read().splitlines()
    return a
    
lines = readStrings("inputs.txt")
print(lines)


print(partA(lines))
print(partB(lines))
