# NG

N = int(input())
K = int(input())
# N, K = 314159, 2
l = len(str(N))
t = 9 ** K

ans = 0
x = 1
if K == 1:
    ans += (l - 1) * t
    ans += int(str(N)[0])
    print(ans)

if K == 2:
    for i in range(K, l - 1):
        x += i

    ans += t * x
    ns = str(N)
    atama = ns[0]

    y = (int(atama)) * 9 ** (K - 1)
    ans += y * (l - 2)

    ans += (int(atama) - 1) * 9 ** (K - 1)
    w = ns[1:K]
    ans += int(w)
    print(ans)
