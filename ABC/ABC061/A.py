###########################################################
# AtCoder Beginner Contest 061
# A - Between Two Integers
# https://atcoder.jp/contests/abc061/tasks/abc061_a
###########################################################

A,B,C = map(int,input().split())
print(["No","Yes"][A<=C and C<=B])
