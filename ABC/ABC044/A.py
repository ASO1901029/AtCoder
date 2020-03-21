###########################################################
# AtCoder Beginner Contest 044
# A - 高橋君とホテルイージー / Tak and Hotels (ABC Edit)
# https://atcoder.jp/contests/abc044/tasks/abc044_a
###########################################################
N = int(input())
K = int(input())
X = int(input())
Y = int(input())
sum = 0
if(N>K):
    sum = K*X
    N-=K
    sum += N*Y
else:
    sum = N*X
print(sum)
