# NG
###########################################################
# AtCoder Beginner Contest 131
# C - Anti-Division
# https://atcoder.jp/contests/abc131/tasks/abc131_c
###########################################################
# import math
import sys
import fractions
A, B, C, D = map(int, sys.stdin.readline().split())
multi = C * D
multiGcd = int((C * D) // fractions.gcd(C, D))

nC = int((A - 1) // C)
nD = int((A - 1) // D)
mC = int(B // C)
mD = int(B // D)

nM = int((A - 1) // multi)
mM = int(B // multi)

wC = mC - nC
wD = mD - nD
wM = mM - nM
wCD = wC + wD - wM

nGcd = int((A - 1) // multiGcd)
mGcd = int(B // multiGcd)
wGcD = mGcd - nGcd

ans = B - (A - 1) - wCD
if multiGcd != multi:
    ans += wGcD
print(ans)
