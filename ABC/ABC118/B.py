n, m = map(int, input().split())
a_list = []
for i in range(n):
    a_list.append(set(map(int, input().split()[1:])))

all_like_list = a_list[0]
for i in range(1, len(a_list)):
    all_like_list = all_like_list.intersection(a_list[i])
print(len(all_like_list))
