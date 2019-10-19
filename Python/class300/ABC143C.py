###########################################################
# AtCoder Beginner Contest 143
# C - Slimes
# https://atcoder.jp/contests/abc143/tasks/abc143_c
###########################################################
N = int(input())
S = list(input())
tmpList = [S[0]]
ans = 1
for char in S:
    if tmpList[-1] == char:
        continue
    tmpList.append(char)
    ans+=1
print(ans)
