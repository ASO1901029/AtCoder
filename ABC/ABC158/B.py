N, A, B = map(int, input().split())

v = N // (A + B)
amari = N % (A + B)
r = v * A
if amari > A:
    r += A
else:
    r += amari

print(r)
