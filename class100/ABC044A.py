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
