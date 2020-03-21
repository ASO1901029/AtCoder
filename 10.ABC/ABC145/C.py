import itertools, math

N = int(input())
shops = []
for i in range(N):
    shops.append(list(map(int, input().split())))

routes = itertools.permutations(shops, N)
l = list(routes)

total = 0
for route in l:
    tmp = 0
    for i in range(1,len(route)):
        kyori = (route[i][0]-route[i-1][0])**2 + (route[i][1]-route[i-1][1])**2
        tmp += math.sqrt(kyori)
    total += tmp
ans = total/len(l)
print(ans)

