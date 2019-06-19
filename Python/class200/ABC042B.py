N,L = map(int,input().split())
strList = []
for i in range(N):
    strList.append(input())
strList.sort()

for str in strList:
    print(str,end="")
