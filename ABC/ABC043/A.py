###########################################################
# AtCoder Beginner Contest 043
# A - キャンディーとN人の子供イージー / Children and Candies (ABC Edit)
# https://atcoder.jp/contests/abc043/tasks/abc043_a
###########################################################
n = int(input())
candy = 0
for i in range(n+1):
    candy += i
print(candy)
