###########################################################
# AtCoder Beginner Contest 132
# C - Divide the Problems
# https://atcoder.jp/contests/abc132/tasks/abc132_c
###########################################################
N = int(input())
dList = list(map(int,input().split()))
dList.sort()
# 中央の添字（偶数個の場合はその中央左）
mid = (N-1)//2
# 中央とその右の差を計算する
sa = dList[mid+1] - dList[mid]
print(sa)
