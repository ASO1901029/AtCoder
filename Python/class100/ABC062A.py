###########################################################
# AtCoder Beginner Contest 062
# A - Grouping
# https://atcoder.jp/contests/abc062/tasks/abc062_a
###########################################################
x,y = map(int,input().split())
isOk=False
listA = [1,3,5,7,8,10,12]
listB = [4,6,9,11]
if x==y:
    isOk=True
elif x in listA and y in listA:
    isOk=True
elif x in listB and y in listB:
    isOk=True
print(["No","Yes"][isOk])
