#NG
n, a, b = map(int, input().split())

mod = 10**9+7
mod_table = [0] * n
sum_table = [0] * n

mod_table[0] = n
sum_table[0] = n

x = n - 1
tmp_u = n
tmp_d = 1
for i in range(1, n):
    tmp_u = int((tmp_u * x) % mod)
    tmp_d = int((tmp_d * i + 1) % mod)
    t = tmp_u / tmp_d
    x -= 1
    mod_table[i] = int(t % mod)
    sum_table[i] = int((sum_table[i - 1] + mod_table[i]) % mod)

print(mod_table)
print(sum_table)
ans = sum_table[-1] - mod_table[a - 1] - mod_table[b - 1]
print(ans)
