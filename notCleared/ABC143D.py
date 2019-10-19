# LTE
###########################################################
# AtCoder Beginner Contest 143
# D - Triangles
# https://atcoder.jp/contests/abc143/tasks/abc143_d
###########################################################
N = int(input())
L = list(map(int, input().split()))
ans = 0
L.sort(reverse=True)
for i in range(len(L) - 2):
    a = L[i]
    for j in range(i + 1, len(L) - 1):
        b = L[j]
        upperC = a + b
        lowerC = abs(a - b)
        l_in = [i for i in L[j + 1:] if lowerC < i < upperC]
        ans += len(l_in)
print(ans)
