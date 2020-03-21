A = []
bingo = []
for i in range(3):
    A.append(list(map(int, input().split())))
    bingo.append([False] * 3)

N = int(input())

for i in range(N):
    b = int(input())
    for j in range(3):
        if b in A[j]:
            idx = A[j].index(b)
            bingo[j][idx] = True

# check
migiue = True
migisita = True
okFlg = False
for i in range(3):
    tate = True
    yoko = True
    for j in range(3):
        if bingo[i][j] == False:
            yoko = False
        if bingo[j][i] == False:
            tate = False
    if tate or yoko:
        okFlg = True
        break
    if bingo[i][i] == False:
        migisita = False
    if bingo[i][-i - 1] == False:
        migiue = False

if migiue or migisita:
    if okFlg == False:
        okFlg = True
print('YNeos'[not okFlg::2])
