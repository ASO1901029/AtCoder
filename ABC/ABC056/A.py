###########################################################
# AtCoder Beginner Contest 056
# A - HonestOrDishonest
# https://atcoder.jp/contests/abc056/tasks/abc056_a
###########################################################
a, b = input().split()
# 両方が同じ場合はTopCoDeerくんは正直者である。
print(["D", "H"][a == b])  # リスト["D","H"]を生成し、条件がTrueの場合1,Falseなら0番目が出力される
