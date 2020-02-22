N = int(input())

dic = {}
m = 1
for i in range(N):
    st = input()
    if st not in dic:
        dic[st] = 1
    else:
        dic[st] += 1
        if dic[st] > m:
            m = dic[st]

ans = []
for s in dic:
    if dic[s] == m:
        ans.append(s)
ans.sort()
for i in range(len(ans)):
    print(ans[i])


