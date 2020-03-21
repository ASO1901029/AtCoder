# NG
# 範囲で色を反転させることができる（読み違えていた）
# import sys
# sys.setrecursionlimit(120*120)
# def dfs(x,y,cnt,now):
#     # 壁の場合数える
#     if field[y][x] != now:
#         now = [".","#"][now == "."]
#         cnt += 1
#         print(cnt)
#     if x == W-1 and y == H-1:
#         # counts.append(cnt)
#         return
#     # 一番右じゃないなら右へ進ませる
#     if x+1 < W:
#         dfs(x+1,y,cnt,now)
#     # 一番下じゃないなら下へ進ませる
#     if y+1 < H:
#         dfs(x,y+1,cnt,now)
#
# H,W = map(int,input().split())
# field = []
# counts = []
# for i in range(H):
#     field.append(list(input()))
# now = '.'
# dfs(0,0,0,now)
# print(min(counts))