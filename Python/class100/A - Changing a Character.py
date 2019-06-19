inputNum = input()
N, K = map(int, inputNum.split(" "))
S = str(input())
lowerS = S.lower()
ans = S
ans[K] = S[K].lower()
print(ans)
