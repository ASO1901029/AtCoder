N, K = map(int, input().split())
p = list(map(int, input().split()))

s = []
for i in range(K):
    s.append(p[i])

m = sum(s)
t = m
for i in range(K, N):
    t += p[i] - p[i - K]
    if m < t:
        m = t

m += K

print(m / 2)

# N, K = map(int, input().split())
# p = list(map(int, input().split()))
#
# s = []
# for i in range(K):
#     s.append(p[i])
#
# m = sum(s)
# for i in range(K,N):
#     s.pop(0)
#     s.append(p[i])
#     if sum(s) > m:
#         m = sum(s)
#
# m += K
#
# print(m / 2)
