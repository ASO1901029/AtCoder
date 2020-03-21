N = int(input())
S = input()

n = N//2

print("YNeos"[S != S[:n]*2::2])