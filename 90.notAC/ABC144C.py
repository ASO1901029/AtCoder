###########################################################
# AtCoder Beginner Contest 144
# C - Walk on Multiplication Table
# https://atcoder.jp/contests/abc144/tasks/abc144_c
###########################################################
N = int(input())
max = int(N**0.5)
a = max-1
for i in range(max,0,-1):
    v = N % i
    if v == 0:
        mult = N / i
        a = mult + i
        break
print(int(a-2))