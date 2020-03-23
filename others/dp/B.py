N,K = map(int,input().split())
h = list(map(int,input().split()))
dp = [0]*N
dp[1] = abs(h[1]-h[0])
for i in range(1,N):
    for j in range(i+1,N):
        dp[j] = min(dp[i-1],dp[i-1]+abs(h[i]-h[j]))

print(dp)