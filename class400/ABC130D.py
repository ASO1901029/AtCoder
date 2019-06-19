N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 0
ans = 0
s = 0

while True:
    while r < N and s < K:
        s += A[r]
        r += 1
    if s >= K:
        ans += N - r + 1
    s -= A[l]
    l += 1
    if l == N:
        break

print(ans)