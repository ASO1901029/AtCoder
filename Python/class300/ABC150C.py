import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
l = []
for i in range(N):
    l.append(i + 1)

# 重複なしのあらゆる並び
l = list(map(list, itertools.permutations(l)))
print(abs(l.index(P) - l.index(Q)))
