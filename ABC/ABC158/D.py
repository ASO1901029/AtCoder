S = input()
Q = int(input())

is_reverse = False
sento = []
matubi = []
for i in range(Q):
    s = input().split()
    if s[0] == '1':
        is_reverse = not is_reverse
    else:
        if (s[1] == '1' and not is_reverse) or (s[1] == '2' and is_reverse):
            sento.append(s[2])
        else:
            matubi.append(s[2])

ans = ''.join(sento[::-1]) + S + ''.join(matubi)
if is_reverse:
    ans = ans[::-1]
print(ans)