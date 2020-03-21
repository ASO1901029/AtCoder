###########################################################
# AtCoder Beginner Contest 132
# B - Ordinary Number
# https://atcoder.jp/contests/abc132/tasks/abc132_b
###########################################################
n = int(input())
pList = list(map(int, input().split()))
c = 0
for i in range(1, n - 1):
    # 比較する対象の3つだけを取り出す
    tList = [pList[i - 1], pList[i], pList[i + 1]]
    tList.sort()
    # 取り出した物のソート後[1]がもとのリスト[i]の場合、2番目に小さい
    if pList[i] == tList[1]:
        c += 1
print(c)
