N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
d = {'r':P,'s':R,'p':S}
ans = 0
for i,c in enumerate(T):
    if i < K or c != T[i-K]:
        ans += d[c]
        continue
    else:
        T[i] = '_'
print(ans)