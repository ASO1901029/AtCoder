###########################################################
# AtCoder Beginner Contest 130
# B - Bounding
# https://atcoder.jp/contests/abc130/tasks/abc130_b
###########################################################
N,X = map(int,input().split())
L = list(map(int,input().split()))
now = 0
cnt = 1
for i in range(len(L)):
    now += L[i]
    if now > X:
        break
    cnt+=1
print(cnt)
