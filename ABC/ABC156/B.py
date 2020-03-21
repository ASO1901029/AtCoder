N,K = map(int,input().split())
cnt = 1
tmp = K
while tmp <= N:
    tmp *= K
    cnt+=1
print(cnt)