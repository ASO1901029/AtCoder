###########################################################
# AtCoder Beginner Contest 060
# A - Shiritori
# https://atcoder.jp/contests/abc060/tasks/abc060_a
###########################################################
A, B, C = input().split()
print(["NO", "YES"][A[-1] == B[0] and B[-1] == C[0]])
