###########################################################
# AtCoder Beginner Contest 143
# B - TAKOYAKI FESTIVAL 2019
# https://atcoder.jp/contests/abc143/tasks/abc143_b
###########################################################
N = int(input())
d_list = list(map(int,input().split()))
ans = 0
for i in range(len(d_list)-1):
    for j in range(i+1,len(d_list)):
        ans += d_list[i] * d_list[j]
print(ans)