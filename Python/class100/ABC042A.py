a = map(int, input().split(" "))
cnt5 = 0
cnt7 = 0
for n in a:
    if n == 5:
        cnt5 += 1
    if n == 7:
        cnt7 += 1
if cnt5 == 2 and cnt7 == 1:
    print("YES")
else:
    print("NO")
