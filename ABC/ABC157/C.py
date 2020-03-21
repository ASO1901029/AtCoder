N, M = map(int, input().split())
s_list = []
c_list = []
isFirstZero = True
for i in range(M):
    s, c = map(int, input().split())
    s_list.append(s - 1)
    c_list.append(c)
    if s == 1:
        isFirstZero = False
l = [-1] * N
isNG = False
if M == 0 and N == 1:
    print(0)
else:
    for i in range(M):
        if s_list[i] == 0 and c_list[i] == 0 and not(N == 1 and c_list[0] == 0):
            isNG = True
            break
        if l[s_list[i]] == -1:
            l[s_list[i]] = c_list[i]
        else:
            if l[s_list[i]] != c_list[i]:
                isNG = True
                break
    if isFirstZero and not (len(l) == 1 and l[0] == 0):
        l[0] = 1
    elif l[0] == -1:
        isNG = True
    if isNG:
        print(-1)
    else:
        for i in range(N):
            if l[i] == -1:
                l[i] = 0
            print(l[i], end="")
