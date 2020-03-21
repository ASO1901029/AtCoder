N = int(input())
d = {}
ans = 0
for i in range(N):
    s = input()
    s = "".join(sorted(list(s)))
    d.setdefault(s, -1)
    d[s] += 1
    ans += d[s]
print(ans)
