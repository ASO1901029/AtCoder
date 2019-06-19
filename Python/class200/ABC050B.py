N = input()
T = list(map(int, input().split()))
M = input()
sum = sum(T) #合計を保持しておく
PX = []
ansList = list()
for i in range(int(M)):
    PX.append(list(map(int, input().split())))
for i in range(int(M)):
    ansList.append(sum - (T[PX[i][0]-1] - PX[i][1])) #合計からジュースに対応するTの差分だけ減算する
    print(ansList[i])
