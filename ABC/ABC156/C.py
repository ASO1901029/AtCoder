N = int(input())
X = list(map(int, input().split()))
X.sort()
ans = 999999999
for i in range(1,100):
    tmp = 0
    for j in X:
        tmp += (i-j)**2
    if tmp < ans:
        ans = tmp
print(ans)



# N = int(input())
# X = list(map(int, input().split()))
# X.sort()
# cost = [0] * len(X)
# for i, v in enumerate(X):
#     if i == 0:
#         cost[i] = v
#     else:
#         cost[i] = cost[i - 1] + v
# print(cost)