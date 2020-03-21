import numpy as np

N = int(input())
A = list(map(int, input().split()))

A = np.array(A)
mod = 10 ** 9 + 7
ans = 0
for i in range(60):
    b = np.count_nonzero(A >> i & 1)
    ans += 2 ** i * b * (N - b)
    ans %= mod
print(ans)