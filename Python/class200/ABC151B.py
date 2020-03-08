N, K, M = map(int, input().split())
a_list = list(map(int, input().split()))
s = sum(a_list)
m = M * N

ans = max(m - s, 0)
if ans > K:
    ans = -1
print(ans)

