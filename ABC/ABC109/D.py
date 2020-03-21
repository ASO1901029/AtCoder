# 解説AC
H,W = map(int,input().split())
field = []

for i in range(H):
    coins = list(map(int,input().split()))
    field.append(coins)

field_route = []
is_left_to_right = False
for i in range(H):
    is_left_to_right = not is_left_to_right
    for j in range(W):
        if is_left_to_right:
            field_route.append((j,i))
        else:
            field_route.append((W-j-1,i))


ans_ls = []
for i,next_xy in enumerate(field_route[:-1]):
    tx,ty = next_xy
    x,y = field_route[i+1]
    if field[ty][tx] == 0:
        tx,ty = x,y
        continue
    if field[ty][tx] %2 == 1:
        field[y][x] += 1
        ans_ls.append([ty+1,tx+1,y+1,x+1])
    tx,ty = x,y
print(len(ans_ls))
for l in ans_ls:
    print(l[0],l[1],l[2],l[3])