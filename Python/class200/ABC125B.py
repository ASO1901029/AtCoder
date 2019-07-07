###########################################################
# AtCoder Beginner Contest 125
# B - Resale
# https://atcoder.jp/contests/abc125/tasks/abc125_b
###########################################################
N = int(input())
Vlist = list(map(int,input().split()))
Clist = list(map(int,input().split()))
saList = []
for i in range(len(Vlist)):
    saList.append(Vlist[i] - Clist[i])
print(saList[saList > 0].sum())