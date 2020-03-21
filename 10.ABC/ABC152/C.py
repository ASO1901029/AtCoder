N = int(input())
p_list = list(map(int,input().split()))
m = N+1
cnt = 0
for i in range(N):
    if p_list[i] < m:
        cnt+=1
        m = p_list[i]
print(cnt)