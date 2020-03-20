N, K = map(int, input().split())
A = list(map(int, input().split()))

one_count = {}
for i in range(len(bin(K))-2):
    one_count.setdefault(i,0)

for i in range(N):
    for j in range(len(bin(A[i])) - 2):
        one_count.setdefault(j, 0)
        if (A[i] >> j) & 1 == 1:
            one_count[j] += 1
ans = 0
k = K
for i in list(one_count.keys())[::-1]:
    if k > 2**i:
        k-=2**i
        t = max(one_count[i], N - one_count[i])
    else:
        t = one_count[i]
    ans += t * 2 ** i
print(ans)
