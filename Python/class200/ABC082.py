s = sorted(input())
t = sorted(input(), reverse=True)

print("YNeos"[t <= s::2])
