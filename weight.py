import random

itemSize = 10
weight = [itemSize - i for i in range(itemSize)]
weightSum = sum(weight)
randomValue = random.randrange(weightSum)
print(randomValue)

sum = 0
index = -1
for w in weight:
    sum += w
    if randomValue < sum:
        index = weight.index(w)
        break
print(index)