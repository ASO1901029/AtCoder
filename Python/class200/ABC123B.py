A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

import itertools

ls = [A, B, C, D, E]
p = list(itertools.permutations(ls, 5))
ans = 124*5
for i,v in enumerate(p):
    t = 0
    for j in range(5):
        if t%10 != 0:
            t += 10- t%10
        t += v[j]
    ans = min(t,ans)
print(ans)