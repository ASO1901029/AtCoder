###########################################################
# AtCoder Beginner Contest 045
# B - 3人でカードゲームイージー / Card Game for Three (ABC Edit)
# https://atcoder.jp/contests/abc045/tasks/abc045_b
###########################################################
s = {}
s['a'] = list(input())
s['b'] = list(input())
s['c'] = list(input())

now = 'a'
while s[now]:
    now = s[now].pop(0) #pop()だと後から取ってしまう
print(now.upper())
