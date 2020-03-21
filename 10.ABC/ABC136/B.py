n = int(input())

d = 1
ans = 0

while True:
    if d > n:
        break
    else:
        if d * 10 <= n:
            ans += d * 9
        else:
            ans += n - d + 1
    d *= 100
print(ans)