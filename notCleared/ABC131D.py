# NG
###########################################################
# AtCoder Beginner Contest 131
# D - Megalomania
# https://atcoder.jp/contests/abc131/tasks/abc131_d
###########################################################
import sys

N = int(input())
AList = []
BList = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    AList.append(A)
    BList.append(B)
sAList = sorted(AList, key=lambda k:BList, reverse=True)
sBList = sorted(BList)

temp = 0
isNG = False
for i in range(N):
    temp += AList[i]
    if temp > BList[i]:
        isNG = True
        break
print(["Yes","No"][isNG])
