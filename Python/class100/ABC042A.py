###########################################################
# AtCoder Beginner Contest 042
# A - 和風いろはちゃんイージー / Iroha and Haiku (ABC Edition)
# https://atcoder.jp/contests/abc042/tasks/abc042_a
###########################################################
a = map(int, input().split(" "))
cnt5 = 0
cnt7 = 0
for n in a:
    if n == 5:
        cnt5 += 1
    if n == 7:
        cnt7 += 1
if cnt5 == 2 and cnt7 == 1:
    print("YES")
else:
    print("NO")
