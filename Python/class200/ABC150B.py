_ = int(input())
s = str(input())

ans = 0
for i in range(len(s)-2):
    ans += "ABC" == '{}'.format(s[i:i+3])

print(ans)