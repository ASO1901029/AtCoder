###########################################################
# AtCoder Beginner Contest 131
# A - Security
# https://atcoder.jp/contests/abc131/tasks/abc131_a
###########################################################
S = input()
ans = "Good"
if S[0] == S[1] or S[1] == S[2] or S[2] == S[3] :
    ans = "Bad"
print(ans)