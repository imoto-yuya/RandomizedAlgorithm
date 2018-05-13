import random
import matplotlib.pyplot as plt

class weight():
    def __init__(self, weightList):
        cumulativeWeight = 0
        self.cumulativeWeightList = []
        for weight in weightList:
            cumulativeWeight += weight
            self.cumulativeWeightList.append(cumulativeWeight)

    def getIndex(self):
        randomValue = random.randrange(self.cumulativeWeightList[-1])

        index = -1
        for cumulativeWeight in self.cumulativeWeightList:
            if randomValue < cumulativeWeight:
                index = self.cumulativeWeightList.index(cumulativeWeight)
                break
        return index

    def getIndexList(self, needNum):
        indexList = []
        # 必要な個数が揃うまで繰り返す
        while len(indexList) < needNum:
            index = self.getIndex()
            # 重複した場合スキップする
            if index not in indexList:
                indexList.append(index)
        indexList.sort()
        return indexList

if __name__ == '__main__':
    itemSize = 100
    needNum = 10
    weightList = [itemSize - i for i in range(itemSize)]
    w = weight(weightList)

    loop = 100000
    sumList = [0 for i in range(itemSize)]
    for i in range(loop):
        indexList = w.getIndexList(needNum)
        for index in indexList:
            sumList[index] += 1

    cumulativeWeight = 0
    for i in range(itemSize):
        cumulativeWeight += i + 1
    print(cumulativeWeight)

    print('index\tweight\tweight_ratio\tfrequency\tprobability')
    for i in range(len(sumList)):
        print(str(i) + '\t' + str(weightList[i]) + '\t' + str(round(weightList[i]/cumulativeWeight*100, 3)) + '\t\t' + str(sumList[i]) + '\t\t' + str(round(sumList[i]/loop*100, 3)))
    indexList = [i for i in range(itemSize)]
    plt.plot(indexList, sumList)
    plt.show()
