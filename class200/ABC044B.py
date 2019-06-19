from collections import Counter

w = input()
c = Counter(list(w))
isBeautiful = True
for i in c.values():
    if i % 2:
        isBeautiful = False
        break
if isBeautiful:
    print("Yes")
else:
    print("No")
