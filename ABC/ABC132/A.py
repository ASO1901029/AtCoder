###########################################################
# AtCoder Beginner Contest 132
# A - Fifty-Fifty
# https://atcoder.jp/contests/abc132/tasks/abc132_a
###########################################################
S = input()
sList = list(S)
sList.sort()
# 前後で2文字ずつならソート後は0番目と2番目は別の文字のはず
c1 = sList.count(sList[0])
c2 = sList.count(sList[2])
print(["No", "Yes"][c1 == 2 and c2 == 2])
