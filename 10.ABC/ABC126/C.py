N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    tmp = 1 / N  # その目が出る確率
    now = i
    while now < K:
        now *= 2
        tmp /= 2
    ans += tmp  # その目でクリアできる確率
print(ans)
