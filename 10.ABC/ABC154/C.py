N = int(input())
a = list(map(int, input().split()))
s = set(a)

print("YNEOS"[len(a) != len(s)::2])
