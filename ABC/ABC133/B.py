###########################################################
# AtCoder Beginner Contest 133
# B - Good Distance
# https://atcoder.jp/contests/abc133/tasks/abc133_b
###########################################################
import math

N, D = map(int, input().split())
xList = []
zahyoList = []
for x in range(N):
    xList.append(list(map(int, input().split())))

count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        r = 0
        for n in range(D):
            r += (xList[i][n] - xList[j][n]) ** 2
        if (math.sqrt(r) % 1 == 0):
            count += 1

print(count)
