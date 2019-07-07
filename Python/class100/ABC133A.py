###########################################################
# AtCoder Beginner Contest 133
# A - T or T
# https://atcoder.jp/contests/abc133/tasks/abc133_a
###########################################################
N, A, B = map(int, input().split())
print([N * A, B][B < N * A])
