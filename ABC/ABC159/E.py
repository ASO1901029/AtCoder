# NG
def white_count(y, x, cnt):
    q = ()
    if field[y][x] != "0":
        cnt += 1
        field[y][x] = cnt
    else:
        return
    for n_y, n_x in zip([1, 0, -1, 0], [0, 1, 0, -1]):
        t_y = y + n_y
        t_x = x + n_x
        if 0 <= t_y < H and 0 <= t_x < W:
            white_count(t_y, t_x, cnt)
    return cnt


H, W, K = map(int, input().split())
field = []
for i in range(H):
    field.append(list(input()))

print(field)
for i in range(H - 1):
    for j in range(W - 1):
        white_count(i, j, 0)
