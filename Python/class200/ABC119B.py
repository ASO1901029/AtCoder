N = int(input())
rate = 380000.0
ans = 0
for i in range(N):
    dama = input().split()
    amount = float(dama[0])
    if dama[1] == "JPY":
        ans += amount
    else:
        ans += rate * amount
print(ans)
