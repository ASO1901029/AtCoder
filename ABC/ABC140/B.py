N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
ans = b_list[a_list[0]-1]
for i in range(1, N):
    ans += b_list[a_list[i]-1]
    if a_list[i-1]+1 == a_list[i]:
        ans += c_list[a_list[i-1]-1]
print(ans)
