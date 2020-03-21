N = int(input())
a = set()
for i in range(N):
    tmp = int(input())
    if tmp in a:
        a.remove(tmp)
    else:
        a.add(tmp)
print(len(a))
