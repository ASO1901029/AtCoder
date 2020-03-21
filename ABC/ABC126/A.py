###########################################################
# AtCoder Beginner Contest 126
# A - Changing a Character
# https://atcoder.jp/contests/abc126/tasks/abc126_a
###########################################################
N, K = map(int, input().split(" "))
S = str(input())

print(S[:K-1]+S[K-1].lower()+S[K:])