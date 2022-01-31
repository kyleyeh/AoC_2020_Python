

def partA(lines):
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            if (lines[i] + lines[j] == 2020):
                return lines[i]*lines[j]







def partB(lines):
    for i in range(0, len(lines)):
        for j in range (i+1, len(lines)):
            for k in range(j+1, len(lines)):
                if (lines[i] + lines[j] + lines[k] == 2020):
                    return lines[i]*lines[j]*lines[k]

def readIntegers(pathToFile):
    with open(pathToFile) as f:
        a = [int(x) for x in f.read().split()]
    return a
    
smallList = readIntegers("inputs.txt")
print(smallList)

print("***")
smallest = smallList[0]
nextSmallest = smallList[0]
thirdSmallest = smallList[0]
for num in smallList:
    if (num < smallest):
        thirdSmallest = nextSmallest
        nextSmallest = smallest
        smallest = num
    elif (num < nextSmallest):
        thirdSmallest = nextSmallest
        nextSmallest = num
    elif (num < thirdSmallest):
        thirdSmallest = num
print(smallest * nextSmallest * thirdSmallest)
print("***")

print(partA(lines))
print(partB(lines))
