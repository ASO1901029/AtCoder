a, b, x = map(int, input().split())
m = a // x  # 切り捨て
n = b // x
ans = n - m
if a % x == 0:
    ans += 1
print(ans)
