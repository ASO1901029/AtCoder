N, M = map(int, input().split())
question = {}
wa = {}
ac_count = 0
wa_count = 0
for i in range(M):
    q, s = input().split()
    question.setdefault(q, '')
    wa.setdefault(q, 0)
    if s == 'AC':
        if question[q] == 'AC':
            continue
        else:
            question[q] = 'AC'
            ac_count += 1
            wa_count += wa[q]
    else:
        wa[q] += 1
print(ac_count, wa_count)
