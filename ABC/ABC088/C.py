l = []
for i in range(3):
    l.append(list(map(int, input().split())))

a2 = l[0][1] - l[0][0]
a3 = l[0][2] - l[0][0]
b2 = l[1][0] - l[0][0]
b3 = l[2][0] - l[0][0]

is_takahashi_true = True

for i in range(1, 3):
    ta2 = l[i][1] - l[i][0]
    ta3 = l[i][2] - l[i][0]
    tb2 = l[1][i] - l[0][i]
    tb3 = l[2][i] - l[0][i]
    if a2 != ta2 or a3 != ta3 or b2 != tb2 or b3 != tb3:
        is_takahashi_true = False

print("YNeos"[not is_takahashi_true::2])
