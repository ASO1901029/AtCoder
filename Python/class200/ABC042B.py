###########################################################
# AtCoder Beginner Contest 042
# B - 文字列大好きいろはちゃんイージー / Iroha Loves Strings (ABC Edition)
# https://atcoder.jp/contests/abc042/tasks/abc042_b
###########################################################

N, L = map(int, input().split())
strList = []
for i in range(N):
    strList.append(input())
strList.sort()

for str in strList:
    print(str, end="")
