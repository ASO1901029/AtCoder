H = int(input())
t = H
depth = 0
ans = 0
while t >= 1:
    ans += 2**depth
    t //= 2
    depth += 1
print(ans)