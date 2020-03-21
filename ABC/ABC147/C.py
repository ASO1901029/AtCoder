# bit全探索
N = int(input())
human = []
for i in range(N):
    A = int(input())
    hatugen = {}
    for j in range(A):
        x, y = map(int, input().split())
        hatugen[x] = y
    human.append(hatugen)

cnt = 0
for i in range(2 ** N):
    is_ok = True
    for j in range(N):
        if (i >> j) & 1:
            for K, V in zip(human[j].keys(), human[j].values()):
                k = K - 1
                if V ^ ((i >> k) & 1):
                    is_ok = False
                    break
    if is_ok:
        cnt = max(cnt, bin(i).count('1'))

print(cnt)
