N,K,Q = map(int,input().split())
d = {}
for i in range(Q):
    A = int(input())
    d.setdefault(A,0)
    d[A] += 1
for i in range(1,N+1):
    pt = K-Q
    d.setdefault(i,0)
    pt += d[i]
    print('YNeos'[pt<1::2])