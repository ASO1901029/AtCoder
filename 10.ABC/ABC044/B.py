###########################################################
# AtCoder Beginner Contest 044
# B - 美しい文字列 / Beautiful Strings
# https://atcoder.jp/contests/abc044/tasks/abc044_b
###########################################################
from collections import Counter

w = input()
c = Counter(list(w))
isBeautiful = True
for i in c.values():
    if i % 2:
        isBeautiful = False
        break
if isBeautiful:
    print("Yes")
else:
    print("No")
