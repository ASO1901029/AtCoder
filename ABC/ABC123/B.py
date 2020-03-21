A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
ls = [A,B,C,D,E]

last = -1
amari = 10
tmp = -1
for i in range(5):
    if ls[i] %10 != 0:
        if amari > ls[i] % 10:
            amari = ls[i] % 10
            tmp = i
        ls[i] += 10 -ls[i] % 10

print(sum(ls)-(10-amari))
