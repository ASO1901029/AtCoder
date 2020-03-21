N = int(input())
a_list = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans += 1/a_list[i]
ans = 1/ ans
print(ans)