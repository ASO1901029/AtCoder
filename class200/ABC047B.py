W, H, N = map(int, input().split())
l = d = 0
u = H
r = W
for i in range(N):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        l = max(x, l)
    if a == 2:
        r = min(x, r)
    if a == 3:
        d = max(y, d)
    if a == 4:
        u = min(y, u)

ans = (r - l) * (u - d)
if r - l < 0 or u - d < 0:
    ans = 0
print(max(ans, 0))
