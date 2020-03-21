###########################################################
# AtCoder Beginner Contest 129
# C - Typical Stairs
# https://atcoder.jp/contests/abc129/tasks/abc129_c
###########################################################
import sys

N, W = sys.stdin.readline().split()
aArr = list()
ans = 0
tmp = int(N)
MOD = 10 ** 9 + 7
aArr = set(map(int, sys.stdin))

tmp = 0
tmpB = 0
ans = 1
for i in range(int(N)):
    if i in aArr:
        tmp = 0
    elif i < 2:
        tmp = 1
    else:
        tmp = ans
    ans = (tmp + tmpB) % MOD
    tmpB = tmp
print(ans)
