# NG
###########################################################
# AtCoder Beginner Contest 133
# C - Remainder Minimization 2019
# https://atcoder.jp/contests/abc133/tasks/abc133_c
###########################################################
L, R = map(int, input().split())
l = L % 2019
ans = l * (l + 1)
Lw = int(L / 2019)
Rw = int(R / 2019)
if Rw - Lw >= 1:
    ans = 0
print(ans)
