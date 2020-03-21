###########################################################
# AtCoder Beginner Contest 047
# A - キャンディーと2人の子供 / Fighting over Candies
# https://atcoder.jp/contests/abc047/tasks/abc047_a
###########################################################
l = list(map(int, input().split()))
l.sort()
if l[2] == l[0] + l[1]:
    print("Yes")
else:
    print("No")
