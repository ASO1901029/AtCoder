a = range(1, int(input())+1)
b = sorted(a, key=lambda _:[(s, -int(p)) for s, p in[input().split()]])
print(*b)
