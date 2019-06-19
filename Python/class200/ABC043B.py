###########################################################
# AtCoder Beginner Contest 043
# B - バイナリハックイージー / Unhappy Hacking (ABC Edit)
# https://atcoder.jp/contests/abc043/tasks/abc043_b
###########################################################
str = input()
output = ""
for n in str:
    if(n=="0"):
        output+="0"
    elif(n=="1"):
        output+="1"
    elif(n=="B"):
        output = output[:-1]
print(output)
