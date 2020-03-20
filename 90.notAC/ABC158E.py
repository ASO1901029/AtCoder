# NG
N, P = map(int, input().split())
S = input()

cnt = 0
t = P
l = set()
l.add('0')
while len(str(t)) <= 2 * 10 ** 5:
    l.add(str(t))
    t += P
print(max(l))
for i in range(len(S)):
    for j in range(i,len(S)):
        t = str(int(S[i:j+1]))
        print(t)
        if t in l:
            cnt += 1

print(cnt)
