###########################################################
# AtCoder Beginner Contest 056
# A - HonestOrDishonest
# https://atcoder.jp/contests/abc056/tasks/abc056_a
###########################################################
a, b = input().split()
print(["D", "H"][a == b])  # 両方が同じ場合はTopCoDeerくんは正直者である。
