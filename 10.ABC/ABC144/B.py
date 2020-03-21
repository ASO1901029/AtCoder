N = int(input())
qq = set()
for i in range(1, 10):
    for j in range(1, 10):
        qq.add(i * j)
print('YNeos'[not N in qq::2])
