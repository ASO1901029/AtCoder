###########################################################
# AtCoder Beginner Contest 131
# D - Megalomania
# https://atcoder.jp/contests/abc131/tasks/abc131_d
###########################################################
N = int(input())
works = []
for i in range(N):
    works.append(list(map(int, input().split())))
works = sorted(works, key=lambda x: (x[1], x[0]))
time = 0
isFail = False
for i in range(N):
    time += works[i][0]
    if time > works[i][1]:
        isFail = True
        break
print("YNeos"[isFail::2])
