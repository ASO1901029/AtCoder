###########################################################
# AtCoder Beginner Contest 131
# B - Bite Eating
# https://atcoder.jp/contests/abc131/tasks/abc131_b
###########################################################
N, L = map(int, input().split())
ajiList = []
absList = []
for i in range(N):
    ajiList.append(i + L)
    absList.append(abs(i + L))
s = sum(ajiList)
m = min(absList)
if s > 0:
    ans = s - min(absList)
else:
    ans = s + min(absList)
print(ans)
