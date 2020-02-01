# ABC149 C
import numpy as np
X = int(input())
numList = np.arange(X*2)

for i in range(2,X):
    if numList[i] == False:
        continue
    numList[i:X*2:i] = 0

for i in numList[X:X*2]:
    if i != 0:
        print(i)
        break
