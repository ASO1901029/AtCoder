A, B, M = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
m_list = []
for i in range(M):
    m_list.append(list(map(int, input().split())))

ans = min(a_list) + min(b_list)
for i in range(len(m_list)):
    price = a_list[m_list[i][0]-1] + b_list[m_list[i][1]-1] - m_list[i][2]
    ans = min(ans,price)

print(ans)

