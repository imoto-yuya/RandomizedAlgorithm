import random

def getIndex(weight):
    weightSum = sum(weight)
    randomValue = random.randrange(weightSum)

    cumulativeSum = 0
    index = -1
    for w in weight:
        cumulativeSum += w
        if randomValue < cumulativeSum:
            index = weight.index(w)
            break
    return index

if __name__ == '__main__':
    itemSize = 100
    weight = [itemSize - i for i in range(itemSize)]
    needNum = 10
    indexList = []
    while len(indexList) < needNum:
        index = getIndex(weight)
        if index not in indexList:
            indexList.append(index)
    indexList.sort()
    print(indexList)
