X = int(input())
ans = 1
for i in range(2,X):
    j = 2
    if i**j > X:
        continue
    while i**j <= X:
        j+=1
    ans = max(ans,i**(j-1))
print(ans)
