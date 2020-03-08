A, B = map(int, input().split())
ans = A * B
if not (1 <= A <= 9 and 1 <= B <= 9):
    ans = -1
print(ans)
