###########################################################
# AtCoder Beginner Contest 046
# B - AtCoDeerくんとボール色塗り / Painting Balls with AtCoDeer
# https://atcoder.jp/contests/abc046/tasks/abc046_b
###########################################################
N,K = map(int,input().split())
ans = K
for i in range(1,N):
    ans *= K-1
print(ans)
