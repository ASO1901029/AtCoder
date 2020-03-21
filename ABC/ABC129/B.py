###########################################################
# AtCoder Beginner Contest 129
# B - Balance
# https://atcoder.jp/contests/abc129/tasks/abc129_b
###########################################################
N = input()
W = list(map(int, input().split()))
ans = sum(W)
for i in range(int(N)):
    sumA = sum(W[:i+1])
    sumB = sum(W[i+1:])
    temp = abs(sumA-sumB)
    if ans > temp:
        ans = temp
print(ans)