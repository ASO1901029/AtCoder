###########################################################
# AtCoder Beginner Contest 130
# C - Rectangle Cutting
# https://atcoder.jp/contests/abc130/tasks/abc130_c
###########################################################
W,H,x,y = map(int,input().split())
w = W/2
h = H/2
ansA,ansB = 0
ansA = W*H/2
if w == x and h == y:
    ansB = 1
print(ansA,ansB)