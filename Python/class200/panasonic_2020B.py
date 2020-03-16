H, W = map(int, input().split())
l = (W+1)//2
m = W//2

ans = (l+m) * (H//2)
if H%2 == 1:
    ans += l
if H == 1 or W == 1:
    ans = 1
print(ans)