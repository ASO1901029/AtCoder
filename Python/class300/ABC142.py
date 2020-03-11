N = int(input())
A = list(map(int,input().split()))
ls = [0]*N
for i,x in enumerate(A):
    ls[x-1] = str(i+1)
print(' '.join(ls))
