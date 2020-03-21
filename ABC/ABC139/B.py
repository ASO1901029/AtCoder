A,B = map(int,input().split())
if B == 1:
    print(0)
else:
    ans = 1
    B -= A
    while B > 0:
        B -= A-1
        ans += 1
    print(ans)
