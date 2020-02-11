N = int(input())
S = input()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_alpha = alpha[N:] + alpha[:N]
ans = ""
for i in range(len(S)):
    idx = alpha.index(S[i])
    ans += new_alpha[idx]
print(ans)