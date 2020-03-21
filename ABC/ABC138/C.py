import bisect
N = int(input())
v = list(map(int,input().split()))
v.sort()

while len(v) > 1:
    l = v.pop(0)
    r = v.pop(0)
    t = (l+r)/2
    bisect.insort(v,t)
print(v[0])