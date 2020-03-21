###########################################################
# AtCoder Beginner Contest 048
# B - Between a and b ...
# https://atcoder.jp/contests/abc048/tasks/abc048_b
###########################################################
a, b, x = map(int, input().split())
m = a // x  # 切り捨て
n = b // x
ans = n - m
if a % x == 0:
    ans += 1
print(ans)
