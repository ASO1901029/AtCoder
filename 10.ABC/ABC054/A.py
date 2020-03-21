###########################################################
# AtCoder Beginner Contest 054
# A - One Card Poker
# https://atcoder.jp/contests/abc054/tasks/abc054_a
###########################################################
A, B = map(int, input().split())
if A == 1:
    A += 13
if B == 1:
    B += 13

if A == B:
    print("Draw")
elif A > B:
    print("Alice")
else:
    print("Bob")
