A,B = map(int,input().split())
if max(A,B) > min(A,B):
    ans = max(A,B)*2-1
else:
    ans = A*2
print(ans)