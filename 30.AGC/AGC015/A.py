N, A, B = map(int, input().split())
ans = (B - A) * (N - 2) + 1
if A > B or (A != B and N <= 1):
    print(0)
else:
    print(ans)
