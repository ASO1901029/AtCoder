N,M = map(int,input().split())
d = {}
ac_count = 0
wa_count = 0
for i in range(M):
    q,s = input().split()
    if not s in d.keys():
        d[q] = ''
    if d[q] == 'AC':
        continue
    d[q] = s
    if s == 'WA':
        wa_count += 1
    else:
        ac_count += 1
print(ac_count,wa_count)
