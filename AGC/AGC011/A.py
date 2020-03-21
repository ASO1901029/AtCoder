N, C, K = map(int, input().split())
T = []
for i in range(N):
    t = int(input())
    T.append(t)
T.sort()

cnt = 0
tmp = 0
jousha = 0
for t in T:
    jousha += 1
    if jousha == 1:
        tmp = t

    if t - tmp > K:
        cnt += 1
        jousha = 1
        tmp = t
        continue

    if jousha == C:
        tmp = 0
        cnt += 1
        jousha = 0
        continue
if tmp != 0:
    cnt += 1
print(cnt)
