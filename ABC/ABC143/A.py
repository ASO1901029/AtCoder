###########################################################
# AtCoder Beginner Contest 143
# A - Curtain
# https://atcoder.jp/contests/abc143/tasks/abc143_a
###########################################################
A,B = map(int,input().split())
print([0,A-B*2][0<A-B*2])