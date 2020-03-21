###########################################################
# AtCoder Beginner Contest 51
# C - Back and Forth
# https://atcoder.jp/contests/abc051/tasks/abc051_c
###########################################################
sx, sy, tx, ty = map(int, input().split())
nx = ny = 0
dx = tx - sx
dy = ty - sy

ans = "R" * dx + "U" * dy + "L" * dx + "D" * dy  # 1回目
ans += "D" + "R" * (dx + 1) + "U" * (dy + 1) + "LU" + "L" * (dx + 1) + "D" * (dy + 1) + "R"  # 2回目
print(ans)
