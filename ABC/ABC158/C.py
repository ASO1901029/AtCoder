import math

A,B = map(int,input().split())
ans = -1
for i in range(10,10000):
    a = math.floor(i * 0.08)
    b = math.floor(i * 0.1)
    if a == A and b == B:
        ans = i
        break

print(ans)